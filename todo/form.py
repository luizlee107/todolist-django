from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields = ['title','finished']


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1','password2']