from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from account.forms import CustomUserCreationForm
from account.models import CustomUser


class CreateUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class UpdateUserView(UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'profile_pic', 'bio',]
    template_name = 'update_user.html'
    # success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.id != self.request.user.id:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class DeleteUserView(DeleteView):
    model = CustomUser
    template_name = 'delete_user.html'
    success_url = reverse_lazy('home')
    