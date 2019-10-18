from django.urls import path
from django.views.generic import TemplateView

from .views import CreateUserView, UpdateUserView, DeleteUserView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('@<str:username><int:pk>/edit/', UpdateUserView.as_view(), name='update_user'),
    path('delete/<slug:slug>/', DeleteUserView.as_view(), name='delete_user'),
]
