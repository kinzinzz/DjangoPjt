from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm
from django.urls import reverse
from .models import Article, Comment
from . import serializers

# Create your views here.

def index(request):
    if request.method == "GET":
        comment_form = CommentForm()
        articles = Article.objects.all()
        serializer = serializers.ArticleSerializer(articles, many=True)
        return render(request, 'index.html', {'articles':serializer.data, 'comment_form':comment_form})


def create(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form':form})

    elif request.method == 'POST':

        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:

        return reverse('/')
        

def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()  
            new_comment = serializers.CommentSerializer(comment)
   
    return JsonResponse(new_comment.data)
            


