from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserSignupForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(min_length=8, max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, max_length=50, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['image']