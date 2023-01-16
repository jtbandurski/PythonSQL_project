from django.shortcuts import render

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