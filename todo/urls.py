from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.task,name='todo'),
    path('delete_task/<int:pk>',views.delete_task,name='delete-task'),
    path('update_task/<int:pk>',views.update_task,name='update-task'),



]