from django.urls import path
from . import views

urlpatterns = [
    path('main-page/', views.show_main_page, name='Главная страница')
]
