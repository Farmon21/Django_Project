from asyncio import Task
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'