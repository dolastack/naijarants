from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class AliasForm(ModelForm):
    required_css_class = 'required'
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username",)
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.validationError
        return['password2']
