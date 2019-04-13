from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group


class SignUpForm(ModelForm):
    """Formulaire de login"""

    class Meta():
        model = User
        fields = ['username', 'password', 'email',]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),

        }


class LoginForm(ModelForm):
    """Formulaire de login"""

    class Meta():
        model = User
        fields = ['username', 'password', ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }
