from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/', include('django.contrib.auth.urls')),
    path('u/', include('account.urls')),
    path('topics/', include('topic.urls')),
    path('', include('article.urls')),
]
