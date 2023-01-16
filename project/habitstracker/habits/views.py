from django.shortcuts import render

from .models import Posts

# Create view
# Get and display Posts
def index(request):
    posts_lists = Posts.objects.order_by('-publish_date')[:10]
    context = {'posts': posts_lists}
    return render(request,'habits/index.html',context)

def login(request):
    
    return render(request, 'login.html')