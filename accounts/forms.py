from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name')
