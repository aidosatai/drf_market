from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import CustomUser

from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'phone',
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'phone',
        )
