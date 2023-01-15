from django.urls import path

from . import views

app_name = 'habits'

urlpatterns = [
    path('',views.index, name='index')
]