from django.urls import path

from .views import (
    IndexView, 
    ArticleDetailView, 
    NewArticleView, 
    AuthorProfileView, 
    SearchView, 
    MyStoriesView, 
    EditArticleView,
    DeleteArticleView,
    MySettingsView,
    ResponseView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('me/stories/', MyStoriesView.as_view(), name='my_stories'),
    path('search/', SearchView.as_view(), name='search'),
    path('new/', NewArticleView.as_view(), name='new_article'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article'),
    path('@<str:username><int:pk>/', AuthorProfileView.as_view(), name='profile'),
    path('<slug:slug>/edit/', EditArticleView.as_view(), name='edit_article'),
    path('<slug:slug>/delete/', DeleteArticleView.as_view(), name='delete_article'),
    path('me/settings/', MySettingsView.as_view(), name='settings'),
    path('response/<int:pk>/', ResponseView.as_view(), name='response'),
]
