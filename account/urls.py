from django.urls import path
from django.views.generic import TemplateView

from .views import CreateUserView, UpdateUserView, DeleteUserView, ProfileView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('delete/<slug:slug>/', DeleteUserView.as_view(), name='delete_user'),
]
