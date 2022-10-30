from django import forms
from . import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = (
            "title",
            "content",
            "movie_name",
            "grade",
            "image",
        )


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "댓글을 입력하세요",
            }
        ),
    )

    class Meta:
        model = models.Comment
        fields = ("content",)
