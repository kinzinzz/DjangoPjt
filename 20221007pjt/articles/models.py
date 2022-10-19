from venv import create
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie_title = models.CharField(max_length=50)
    grade = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], help_text="평점 0~5사이 값을 입력해주세요")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)