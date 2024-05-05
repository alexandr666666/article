from django.forms import ModelForm
from .models import *
from django import forms

class AddArticle(ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'title', 'text', 'pub_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название статьи'})
        }

class AddComment(ModelForm):
    class Meta:
        model = Comment
        fields = ["article", 'author', 'text', 'pub_date']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Автор комметария'}),
            'text': forms.TextInput(attrs={'placeholder': 'Текст комментария'})
        }