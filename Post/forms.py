from django import forms
from django.forms import ModelForm
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = users
        fields = '__all__'