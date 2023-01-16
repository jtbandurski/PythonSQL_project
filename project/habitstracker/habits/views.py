from django.shortcuts import render, redirect

from .models import Posts, Habbits


# Create view
# Get and display Posts
def index(request):
    posts_lists = Posts.objects.order_by('-publish_date')[:10]
    context = {'posts': posts_lists}
    return render(request,'habits/index.html',context)

def login(request):
    
    return render(request, 'login.html')

# Track habbits progress
def add_progress(request):
    # ADD AUTHENTICATION AND USER DETAILS

    habits_list = Habbits.objects.all().filter(user=1)
    context = {'habits': habits_list}
    return render(request, 'habits/add_progress.html', context)

def add_progress_submission(request):
    # ADD AUTHORIZATION AND USER DETAILS
    if request.method == "POST":
        
        habit_id = request.POST["selected_habit"]
        amount = request.POST["amount"]
        date = request.POST["date"]
        add = HabbitsTracker(habbit = habit_id,habbit_type=1,quantity=quantity,date = date,yes_no_value= None, success_amount_value=amount)
        add.save()

        posts_lists = Posts.objects.order_by('-publish_date')[:10]
        context = {'posts': posts_lists}

        return render(request,'habits/index.html',context)
    return redirect('/habits/add_progress')