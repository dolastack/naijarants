from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Rant, Comment

class RantForm(ModelForm):
   # required_css_class = 'required'
    title = forms.CharField( widget=forms.TextInput(
        attrs = {
            "class" : "form-control",
           
        }
    ))
    body = forms.CharField(widget=forms.Textarea(
        attrs = {
            "class": "form-control",
           
        }
    ))
    """ category = forms.CharField(widget=forms.Select(
        attrs = {
            "class" : "dropdown-item"
        }
    ), choices=CATIGORIES) """
    files = forms.FileField(widget=forms.FileInput(
        attrs = {
            "class" : "custom-file"
        }
    ))
    class Meta:
        model = Rant
        fields = ("title", "body", "files", "category")
        labels = { 'body' : _('Rant'),
                   'title': _('Title')
                   }
class CommentForm(ModelForm):
    required_css_class = 'required'
    name = forms.CharField( widget=forms.TextInput(
        attrs = {
            "class" : "form-control",
        }
    ))
    body = forms.CharField( widget=forms.Textarea(
        attrs = {
            "class" : "form-control",
        }
    ))
    class Meta:
        model = Comment
        fields = ('name', 'body')
