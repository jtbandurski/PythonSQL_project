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
    path('add_habit/',views.add_habit, name='add_habit'),
    path('add_habit/submission/',views.add_habit_submission, name='add_habitsubmission/'),
    path('comment/submission/',views.add_comment_submission, name='add_commentssubmission/'),
    path('dislike/<int:post_id>/',views.dislike, name='dislike'),
    path('like/<int:post_id>/',views.like, name='like'),
    path('motivations/submission/',views.add_motivation_submission, name='add_motivation_submission'),
]