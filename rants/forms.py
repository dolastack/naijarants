from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Rant

class RantForm(ModelForm):
    class Meta:
        model = Rant
        fields = ("title", "body", "category")
