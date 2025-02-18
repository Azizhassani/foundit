from django import forms
from .models import founditem
from django.contrib.auth.models import User


class foundForm(forms.ModelForm):
    class Meta:
        model = founditem
        fields = ['name','description','date_lost','location']


class registerform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Hided

    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 


