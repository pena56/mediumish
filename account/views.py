from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from account.forms import CustomUserCreationForm
from account.models import CustomUser


class CreateUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class UpdateUserView(UpdateView):
    model = CustomUser
    fields = ['email', 'first_name', 'last_name', 'profile_pic', 'bio', 'facebook_profile', 'twitter_profile']
    template_name = 'update_user.html'
    success_url = reverse_lazy('profile')


class DeleteUserView(DeleteView):
    model = CustomUser
    template_name = 'delete_user.html'
    success_url = reverse_lazy('home')
    