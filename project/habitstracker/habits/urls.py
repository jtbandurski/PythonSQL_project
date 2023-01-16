from django.urls import path

from . import views

app_name = 'habits'

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('add_progress/',views.add_progress, name='add_progress'),
    path('add_progress/submission/',views.add_progress_submission,name='add_progress_submission'),
]