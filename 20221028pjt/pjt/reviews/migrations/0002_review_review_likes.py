# Generated by Django 3.2.13 on 2022-10-28 07:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_likes',
            field=models.ManyToManyField(blank=True, related_name='review_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
