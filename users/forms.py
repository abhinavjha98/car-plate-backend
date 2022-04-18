from dataclasses import fields
from pyexpat import model
from django import *
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    model = CustomUser
    fields = "__all__"