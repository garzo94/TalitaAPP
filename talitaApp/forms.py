from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
    widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
    widget=forms.PasswordInput)
    username = forms.CharField(label='usuario',
    help_text=""
    )
    class Meta:
        model = User
        fields = ('username', 'email')