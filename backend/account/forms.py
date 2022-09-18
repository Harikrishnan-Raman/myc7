from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

ROLES = [
    ('instructor', 'Instructor'),
    ('student', 'Student'),
    ('admin', 'Admin'),
    ]

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    role = forms.CharField(
        label='What is your Role?',
            widget=forms.Select(choices=ROLES))

    universityID = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role', 'universityID')