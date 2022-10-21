from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
# Create your models here.

class Review(models.Model):

    user = models.ForeignKey(get_user_model(),  related_name="reviews", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie_name = models.CharField(max_length=80)
    grade = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="평점은 0~5 값을 입력해주세요.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):

    review = models.ForeignKey(Review, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name="comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
