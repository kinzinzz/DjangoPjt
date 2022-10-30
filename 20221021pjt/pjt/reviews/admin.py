from django.contrib import admin
from .models import Review, Comment
from django.contrib.auth import get_user_model
# Register your models here.
User = get_user_model()

admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(User)