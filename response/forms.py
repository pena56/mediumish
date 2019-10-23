from django import forms

from .models import Response

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('response',)
