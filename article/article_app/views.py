from django.shortcuts import render, redirect
from .models import *
from .forms import *

def show_main_page(request):
    article = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'main-page.html', {'article': article})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Главная страница')
    else:
        form = ArticleForm()
    return render(request, 'add-article.html', {'form': form})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Страница для добавления статей')
    else:
        form = CommentForm()
    comment = Comment.objects.all()
    return render(request, 'add-comment.html', {'form': form, 'comment': comment})