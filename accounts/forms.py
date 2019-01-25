from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account
from django.contrib.auth.models import AbstractUser

class EditProfileForm(UserChangeForm):

    class Meta:
        model = AbstractUser
        fields=( 
            'email',
            'first_name',
            'last_name',
            'password'
        )


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name', 'user_type')
