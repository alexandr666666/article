from django.shortcuts import render, redirect
from .models import *
from .forms import *

def show_main_page(request):
    article = Article.objects.all()
    return render(request, 'main-page.html', {'article': article})

def add_article(request):
    if request.method == 'POST':
        form = AddArticle(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Главная страница')
    else:
        form = AddArticle()
    return render(request, 'add-article.html', {'form': form})

def add_comment(request):
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Страница для добавления статей')
    else:
        form = AddComment()
    comment = Comment.objects.all()
    return render(request, 'add-comment.html', {'form': form, 'comment': comment})