from operator import mod
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Article(models.Model):

    user = models.ForeignKey(get_user_model(), related_name="articles", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()

class Comment(models.Model):

    user = models.ForeignKey(get_user_model(), related_name="comments", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=80)