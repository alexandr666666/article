from django.urls import path
from . import views

urlpatterns = [
    path('main-page/', views.show_main_page, name='Главная страница'),
    path('add-article/', views.add_article, name='Страница для добавления статей'),
    path('add-comment/', views.add_comment, name='Страница для добавления комментариев')
]
