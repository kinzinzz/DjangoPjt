from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# 메인 페이지
def index(request):

    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html',context)


#게시글 생성

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

    return render(request, 'articles/review_create.html', context)

# 상세조회

def detail(request, pk):
    
    article = Article.objects.get(pk=pk)

    context = {
        'article':article,
    }

    return render(request, 'articles/detail.html', context)

# 댓글 생성

def add_comment(request, article_pk):

    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()

            return redirect('articles:detail', article_pk)

    else: 
        comment_form = CommentForm()

    context = {
        'comment_form':comment_form,
    }

    return render(request, 'articles/add_comment.html', context)

# 댓글 삭제

def delete_comment(request, article_pk, comment_pk):
    
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)