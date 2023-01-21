from django.shortcuts import render, redirect

from .models import Posts, Habbits, HabbitsTracker, Motivations,UsersList
from django.contrib.sessions.backends.base import SessionBase
from django.db import connections



# Create view
# Get and display Posts
session = SessionBase()
def checkLogin():
    if  'user_id' not in session or  'user_Name' not in session: 
        return False
    return True

# handling register
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

    posts_lists = Posts.objects.raw('''SELECT p.post_id, p.publish_date as post_date, p.content as post_content, u.user_name as post_user,
                                                c.publish_date as comment_date, c.content as comment_content, v.user_name as comment_user
                                        FROM posts as p
                                        JOIN users_list as u ON p.user_id=u.user_id 
                                        JOIN comments as c ON p.post_id=c.post_id
                                        join users_list as v on c.user_id=v.user_id
                                        ORDER BY p.publish_date DESC LIMIT 10''')
    for p in posts_lists:
        print(vars(p))
    context = {'posts': posts_lists}
    return render(request,'habits/index.html',context)


# handling login
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

# handling logout
def logout(request):
    session.clear()
    return redirect(login)

# Track habbits progress
def add_progress(request):
     # Check Auth
    if not checkLogin():
        return redirect(login)

    user_id = session['user_id']
    habits_list = Habbits.objects.raw('''SELECT * FROM habbits WHERE user_id = %s''',[user_id])
    context = {'habits': habits_list}
    return render(request, 'habits/add_progress.html', context)

# handling logging habbits
def add_progress_submission(request):
     # Check Auth
    if not checkLogin():
        return redirect(login)

    if request.method == "POST":
        
        habit_id = request.POST["selected_habit"]
        amount = request.POST["amount"]
        date = request.POST["date"]
        cursor = connections['default'].cursor()
        # get next id
        habbits_tracker = Habbits.objects.raw('''SELECT * FROM habbits_tracker''')
        next_id = len(habbits_tracker)
        # insert
        cursor.execute("INSERT INTO habbits_tracker VALUES( %s , %s, %s, %s, %s, %s)", [next_id, habit_id, 1, date, None, amount])
        
        return redirect('/habits')
    return redirect('/habits/add_progress')


# My Habits page
def my_habits(request):
     # Check Auth
    if not checkLogin():
        return redirect(login)

    user_id = session['user_id']
    habits_list = Habbits.objects.raw('''SELECT * FROM habbits WHERE user_id = %s''',[user_id])
    context = {'habits': habits_list}
    return render(request, 'habits/my_habits.html',context)

# Motivations page
def motivations(request):
    # Check Auth
    if not checkLogin():
        return redirect(login)

    user_id = session['user_id']
    motivations_list = Motivations.objects.raw('''SELECT * FROM motivations WHERE user_id = %s''',[user_id])
    context = {'motivations': motivations_list}
    return render(request,'habits/motivations.html',context)

# Adding habits
def add_habit(request):
    # Check Auth
    if not checkLogin():
        return redirect(login)

    return render(request, 'habits/add_habit.html')

# Handle adding habits
def add_habit_submission(request):
     # Check Auth
    if not checkLogin():
        return redirect(login)

    if request.method == "POST":
        
        user_id = session["user_id"]
        habit_desc = request.POST["habit_desc"]
        habit_name = request.POST["habit_name"]
        success_activity = request.POST["success_activity"]
        success_range = request.POST["success_range"]
        success_amount = request.POST["success_amount"]
        success_unit = request.POST["success_unit"]
        habit_days_target = request.POST["habit_days_target"]

        cursor = connections['default'].cursor()
        # get next id
        habbits = Habbits.objects.raw('''SELECT * FROM habbits''')
        next_id = len(habbits)
        # insert
        cursor.execute("INSERT INTO habbits VALUES( %s , %s, %s, %s, %s, %s, %s, %s, %s, %s)", [next_id, user_id, 1, habit_desc, habit_name, 
                                                                                                        habit_days_target, success_activity, success_range,
                                                                                                        success_amount, success_unit])
        
        return redirect('/habits')
    return redirect('/habits/add_habit')

