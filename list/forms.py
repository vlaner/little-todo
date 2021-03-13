from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import ToDoListModel


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ToDoListModelForm(ModelForm):
    class Meta:
        model = ToDoListModel
        fields = ['title']
