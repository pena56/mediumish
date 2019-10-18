from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from account.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'password1', 'password2', )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'bio', 'profile_pic',)


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'facebook_profile', 'twitter_profile', 'username',)

