from django.db import models
from django.utils import timezone
from datetime import timedelta

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField('', max_length=50, default='')
    title = models.CharField('', max_length=100, default='')
    text = models.TextField('')
    pub_date = models.DateField(default=timezone.now)

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('', max_length=40, default='')
    text = models.CharField('', max_length=200, default='')
    pub_date = models.DateField(default=timezone.now)

    def __repr__(self):
        return self.article
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'