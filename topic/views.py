from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Topic
from article.models import Article

# Create your views here.
class TopicView(ListView):
    model = Topic
    template_name = 'topics.html'
    context_object_name = 'topics'


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(
            Q(topic__slug__contains=self.kwargs['slug']) &
            Q(status='published')
        )
        return context
    