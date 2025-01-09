from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput


class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=DateInput(attrs={'type': 'text', 'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y'],  # Specify the desired input format
        label="Date of Birth",  # Add a label
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'date_of_birth', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
