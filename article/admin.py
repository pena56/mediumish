from django.contrib import admin
from mediumeditor.admin import MediumEditorAdmin

from .models import Article
# Register your models here.

@admin.register(Article)
class ArticleAdmin(MediumEditorAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title',]}
    mediumeditor_fields = ('body',)


# admin.site.register(Article, ArticleAdmin)
