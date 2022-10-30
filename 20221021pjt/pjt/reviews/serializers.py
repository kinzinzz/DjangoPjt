from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = (
            'id',
            'review',
            'user',
            'content',
        )


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    user = UserSerializer()
    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'title',
            'content',
            'movie_name',
            'grade',
            'comments',
            'created_at',
        )