from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'password1', 'password2', )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'bio', 'profile_pic',)
