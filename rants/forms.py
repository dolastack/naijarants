from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Rant, Comment

class RantForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Rant
        fields = ("title", "body", "category")
        labels = { 'body' : _('Rant'),
                   'title': _('Title')
                   }
class CommentForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Comment
        fields = ('name', 'body')
