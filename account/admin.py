from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.forms import CustomUserChangeForm, CustomUserCreationForm
from account.models import CustomUser

# Register your models here.
class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # list_display = ['first_name', 'last_name', 'profile_pic', 'email']

admin.site.register(CustomUser, CustomAdmin)
