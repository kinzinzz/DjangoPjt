from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

User = get_user_model()


class Review(models.Model):

    author = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie_name = models.CharField(max_length=80)
    grade = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="평점은 0~5 값을 입력해주세요.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(300, 400)],
        format="JPEG",
        options={"quality": 60},
    )
    review_likes = models.ManyToManyField(User, blank=True, related_name="review_likes")


class Comment(models.Model):

    review = models.ForeignKey(
        Review, related_name="comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
