from django.db import models
from django.utils import timezone

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('', max_length=100)
    text = models.TextField('')
    pub_date = models.DateField(default=timezone.now)