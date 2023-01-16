from django.shortcuts import render, redirect

from .models import Posts, Habbits, HabbitsTracker, Motivations,UsersList
from django.contrib.sessions.backends.base import SessionBase


# Create view
# Get and display Posts
session = SessionBase()
def checkLogin():
    if  'user_id' not in session or  'user_Name' not in session: 
        return False
    return True

def register(request):
    context = {}
    if request.method =='POST':
        fname      = request.POST.get('fname')
        lname      = request.POST.get('lname')
        occupation = request.POST.get('occupation')
        uname      = request.POST.get('uname')
        email      = request.POST.get('email')
        password   = request.POST.get('password')

        try:
            add_user= UsersList(first_name = fname,last_name=lname,occupation = occupation,user_name = uname, email=email,password=password)
            add_user.save()
            return redirect(login)
        except IntegrityError:
            context = {'message':'Data is not saved!'}

    return render(request,'register.html',context)


def index(request):
    # Check Auth
    if not checkLogin():
        return redirect(login)

    posts_lists = Posts.objects.raw('SELECT * FROM posts ORDER BY publish_date DESC LIMIT 10')
    context = {'posts': posts_lists}
    return render(request,'habits/index.html',context)



def login(request):
    context = {}
    if request.method =='POST':
        email    = request.POST.get('email')
        password = request.POST.get('password')
        users = UsersList.objects.filter(email=email, password=password).first()
      
        if not users:
            context = {'message':'wrong email or password'}
        else:
            session['user_id']   = users.user_id
            session['user_Name'] = users.user_name
           
            print(session)
            print( session['user_Name'])
            return redirect(index)
    
    return render(request, 'login.html',context)

def logout(request):
    session.clear()
    return redirect(login)

# Track habbits progress
def add_progress(request):
     # Check Auth
    if not checkLogin():
        return redirect(login)
    # ADD AUTHENTICATION AND USER DETAILS

    habits_list = Habbits.objects.raw('SELECT * FROM habbits WHERE user_id=0')
    context = {'habits': habits_list}
    return render(request, 'habits/add_progress.html', context)

# handling action from the form
def add_progress_submission(request):
     # Check Auth
    if not checkLogin():
        return redirect(login)

    if request.method == "POST":
        
        habit_id = request.POST["selected_habit"]
        amount = request.POST["amount"]
        date = request.POST["date"]
        add = HabbitsTracker(habbit = habit_id,habbit_type=1,date = date,yes_no_value= None, success_amount_value=amount)
        add.save()

        posts_lists = Posts.objects.order_by('-publish_date')[:10]
        context = {'posts': posts_lists}

        return render(request,'habits/index.html',context)
    return redirect('/habits/add_progress')


# My Habits page
def my_habits(request):
     # Check Auth
    if not checkLogin():
        return redirect(login)

    habits_list = Habbits.objects.raw('SELECT * FROM habbits WHERE user_id=0')
    context = {'habits': habits_list}
    return render(request, 'habits/my_habits.html',context)

#M otivations page
def motivations(request):
    #ADD AUTHENTICATION AND USER DETAILS
    # Check Auth
    if not checkLogin():
        return redirect(login)

    motivations_list = Motivations.objects.raw('SELECT * FROM motivations WHERE user_id=0')
    context = {'motivations': motivations_list}
    return render(request,'habits/motivations.html',context)