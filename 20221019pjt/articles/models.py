from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# 게시글
class Articles(models.Model):

    user = models.ForeignKey(
        get_user_model(), related_name="articles", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=80)
    content = models.TextField()    

# 댓글
class Comments(models.Model):

    article = models.ForeignKey(
        Articles, related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(get_user_model(), related_name="comments", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=80)
