from django.shortcuts import render, redirect
from .models import *

def show_main_page(request):
    article = Article.objects.all()
    return render(request, 'main-page.html', {'article': article})