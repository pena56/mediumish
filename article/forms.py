from django import forms
from mediumeditor.widgets import MediumEditorTextarea

from .models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'topic', 'article_img', 'status', )
        widgets = {
            'title': MediumEditorTextarea(),
            'body': MediumEditorTextarea(),
        }


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'topic', 'article_img', 'status', )
        widgets = {
            'title': MediumEditorTextarea(),
            'body': MediumEditorTextarea(),
        }

