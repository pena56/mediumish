from django.urls import path

from .views import TopicView, TopicDetailView

urlpatterns = [
    path('', TopicView.as_view(), name='topics'),
    path('<slug:slug>', TopicDetailView.as_view(), name='topic'),
]
