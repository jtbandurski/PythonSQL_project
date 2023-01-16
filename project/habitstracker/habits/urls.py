from django.urls import path

from . import views



urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('add_progress/',views.add_progress, name='add_progress'),
    path('add_progress/submission/',views.add_progress_submission,name='add_progress_submission'),
    path('my_habits/',views.my_habits, name='my_habits'),
    path('motivations/',views.motivations, name='motivations'),
]