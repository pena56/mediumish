from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Topic

# Create your views here.
class TopicView(ListView):
    model = Topic
    template_name = 'topics.html'
    context_object_name = 'topics'


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic.html'
    context_object_name = 'topic'

    # def get_context_data(self):
    #     context = super(TopicDetailView, self).get_context_data(**kwargs)
    #     return context