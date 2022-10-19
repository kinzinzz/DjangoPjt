from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):

    if request.method == 'POST':
        article_form = ArticleForm(request.POST)

        if article_form.is_valid():
            article_form.save()

            return redirect('articles:index')

    else:
        article_form = ArticleForm()

    context = {
        'article_form':article_form,
    }

    return render(request, 'articles/create.html', context)

def detail(request, pk):

    article = Article.objects.get(pk=pk)

    return render(request, 'articles/detail.html', context ={ 'article':article,} )

def update(request, pk):

    article = Article.objects.get(pk=pk)

    if request.method == 'POST':

        article_form = ArticleForm(request.POST, instance=article)

        if article_form.is_valid():
            article_form.save()

            return redirect('articles:detail', article.pk)

    else:

        article_form = ArticleForm(instance=article)

    return render(request, 'articles/update.html', context = { 'article_form':article_form,})

def delete(request, pk):

    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')
