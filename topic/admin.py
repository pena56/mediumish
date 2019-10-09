from django.contrib import admin
from .models import Topic

# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}

admin.site.register(Topic, TopicAdmin)
