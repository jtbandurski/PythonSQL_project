from django.urls import path

from . import views



urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('analysis/',views.analysis, name='analysis'),
    #path('analysis/?habit_id=',views.analysis, name='analysis'),
    path('profile/',views.profile, name='profile'),
    path('add_progress/',views.add_progress, name='add_progress'),
    path('add_progress/submission/',views.add_progress_submission,name='add_progress_submission'),
    path('my_habits/',views.my_habits, name='my_habits'),
    path('motivations/',views.motivations, name='motivations'),
    path('add_habit/',views.add_habit, name='add_habit'),
    path('add_habit/<id>/',views.add_habit, name='add_habit'),
    path('delete_habit/<id>/',views.delete_habit, name='delete_habit'),
    path('comment/submission/',views.add_comment_submission, name='add_commentssubmission/'),
    path('dislike/<int:post_id>/',views.dislike, name='dislike'),
    path('like/<int:post_id>/',views.like, name='like'),
    path('motivations/submission/',views.add_motivation_submission, name='add_motivation_submission'),
    path('delete_motivation/<id>',views.delete_motivation, name='delete_motivation'),

]