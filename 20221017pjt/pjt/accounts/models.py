from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# app_name 설정하면 'app_name/이미지파일명'으로 저장된다.
class Articles(models.Model):
    title = models.CharField(max_length=80)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 60},
    )
