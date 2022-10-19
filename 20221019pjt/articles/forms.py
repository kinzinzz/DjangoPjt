from .models import Articles, Comments
from django import forms

class Articles_Form(forms.ModelForm):

    class Meta:
        model = Articles
        exclude = [
            'user'
        ]

class Comments_Form(forms.ModelForm):

    class Meta:
        model = Comments
        fields = [
            'content',
        ]