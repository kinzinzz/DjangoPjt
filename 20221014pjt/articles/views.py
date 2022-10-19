from ast import Pass
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Articles
# Create your views here.

def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # method 가 POST 방식이면 DB 저장
    if request.method == 'POST':
        article = ArticlesForm(request.POST)
        # 유효성 검증    
        if article.is_valid():
            article.save()
            return redirect('articles:index')
    # GET 방식이라면 
    else:
        article_form = ArticlesForm()
    
    context = {
        'article_form':article_form,
    }
            
    return render(request, 'articles/create.html', context)

def detail(request, pk):

    article = Articles.objects.get(id=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)

def update(request, pk):
    
    article = Articles.objects.get(id=pk)
    
    if request.method == 'POST':
        article_form = ArticlesForm(request.POST, instance=article)

        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.id)

    else: 
        article_form = ArticlesForm(instance=article)
    context = {
        'article_form':article_form,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):

    article = Articles.objects.get(id = pk)
    article.delete()

    return redirect('articles:index')
