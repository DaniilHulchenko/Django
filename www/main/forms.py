from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class RegisterUserForm(UserCreationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'id':'user','name':"user", 'placeholder':"Username"}))
    email=forms.CharField(label='Email',widget=forms.TextInput(attrs={'id':'user','name':"email", 'placeholder':"Email"}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'id':'pass','name':"pass", 'placeholder':"Password"}))
    password2=forms.CharField(label='Password confirm',widget=forms.PasswordInput(attrs={'id':'pass','name':"pass", 'placeholder':"Password confirm"}))
    class Meta:
        model=User
        fields = ('username','email', 'password1','password2')
        widgets={
            'username':TextInput(attrs={'id':'user','name':"user", 'placeholder':"Username"}),
            'email':TextInput(attrs={'id':'email','name':"email", 'placeholder':"Email"}),
            'password1':TextInput(attrs={'id':'pass','name':"pass", 'placeholder':"Password"}),
            'password2':TextInput(attrs={'id': 'pass','name':"pass", 'placeholder':"Password confirm"})
        }

class LoginUserForm(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'id':'user','name':"user", 'placeholder':"Username"}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'pass', 'name': "user", 'placeholder': "Password"}))
    username = forms.CharField(label=(), widget=forms.TextInput(attrs={'id': 'user', 'name': "user", 'placeholder': "Username"}))
    password = forms.CharField(label=(), widget=forms.PasswordInput(attrs={'id': 'pass', 'name': "user", 'placeholder': "Password"}))

class EditAccountDetails(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"id": 'user'}))
    # class Meta:
    #     fields=''
