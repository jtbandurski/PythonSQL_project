from django.shortcuts import render, redirect

from .models import Posts, Habbits, HabbitsTracker, Motivations,UsersList


# Create view
# Get and display Posts
def index(request):
    posts_lists = Posts.objects.raw('SELECT * FROM posts ORDER BY publish_date DESC LIMIT 10')
    context = {'posts': posts_lists}
    return render(request,'habits/index.html',context)

def login(request):
    context = {}
    if request.method =='POST':
        email    = request.POST.get('email')
        password = request.POST.get('password')
        users = UsersList.objects.filter(email=email, password=password)
      
        if not users:
            context = {'message':'wrong email or password'}
        else:
            return redirect(index)
  
   
    return render(request, 'login.html',context)

# Track habbits progress
def add_progress(request):
    # ADD AUTHENTICATION AND USER DETAILS

    habits_list = Habbits.objects.raw('SELECT * FROM habbits WHERE user_id=0')
    context = {'habits': habits_list}
    return render(request, 'habits/add_progress.html', context)

# handling action from the form
def add_progress_submission(request):
    # ADD AUTHORIZATION AND USER DETAILS

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
    #ADD AUTHENTICATION AND USER DETAILS

    habits_list = Habbits.objects.raw('SELECT * FROM habbits WHERE user_id=0')
    context = {'habits': habits_list}
    return render(request, 'habits/my_habits.html',context)


#M otivations page

def motivations(request):
    #ADD AUTHENTICATION AND USER DETAILS

    motivations_list = Motivations.objects.raw('SELECT * FROM motivations WHERE user_id=0')
    context = {'motivations': motivations_list}
    return render(request,'habits/motivations.html',context)