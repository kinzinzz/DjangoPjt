from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Comment
        fields = (
            "id",
            "content",            
        )

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = models.Article
        fields = (
            "id",
            "title",
            "content",
            "comments",
        )


