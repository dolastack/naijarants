from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Rant

class RantForm(ModelForm):
    class Meta:
        model = Rant
        fields = ("title", "body", "category")
        labels = { 'body' : _('Rant'),
                   'title': _('Rant Title')
                   }
        help_texts = { 'body': _('400 Characters'),
                      }
