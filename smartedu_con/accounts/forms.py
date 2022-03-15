from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User

class Loginform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput())


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]        