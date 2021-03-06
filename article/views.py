from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from .models import Article
from .forms import ArticleCreateForm, ArticleEditForm
from account.models import CustomUser
from account.forms import UserSettingsForm
from response.models import Response

# Create your views here.


class IndexView(ListView):
    queryset = Article.objects.filter(status='published').order_by('-id')
    template_name = 'index.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['responses'] = Response.objects.filter(article=article).order_by('-id')
        context['related'] = list(Article.objects.filter(
            Q(topic=article.topic) &
            Q(status='published')
        ).order_by('-id')[:3])

        if article in context['related']:
            context['related'].remove(article)

        return context


class AuthorProfileView(DetailView):
    model = CustomUser
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(
            Q(author=kwargs['object']) & 
            Q(status='published')
        )
        return context


class NewArticleView(LoginRequiredMixin, CreateView):
    form_class = ArticleCreateForm
    template_name = 'new_article.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        articles = Article.objects.filter(
            Q(
                Q(title__icontains=query) |
                Q(author__username__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query)
            ) & Q(status='published')
        )

        return render(request, 'search.html', {'articles': articles})


class MyStoriesView(LoginRequiredMixin, View):
    def get(self, request):
        drafts = Article.objects.filter(Q(author=request.user) & Q(status='draft'))
        published = Article.objects.filter(Q(author=request.user) & Q(status='published'))

        context = {
            'drafts': drafts,
            'published': published,
        }

        return render(request, 'stories.html', context)


class EditArticleView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleEditForm
    template_name = 'edit_article.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('my_stories')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class MySettingsView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        form = UserSettingsForm(instance=user)
        return render(request, 'settings.html', {'form': form})

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        form = UserSettingsForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('settings')
        else:
            return redirect('settings')


class ResponseView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        fan = request.user
        article = Article.objects.get(id=kwargs['pk'])
        response = request.POST['response']
        Response.objects.create(article=article, fan=fan, response=response)
        return HttpResponseRedirect(article.get_absolute_url())
