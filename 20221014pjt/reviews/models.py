from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie_name = models.CharField(max_length=50)
    grade = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="평점은 0~5 값입니다.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    UserID = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Comment(models.Model):
    review = models.ForeignKey(
        Review, related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(null=True, blank=True)
    approve_comment = models.BooleanField(default=True)

    def __str__(self):
        return self.text
