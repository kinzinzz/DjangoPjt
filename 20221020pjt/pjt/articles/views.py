from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from .models import Article
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 목록 조회
def index(request):

    articles = Article.objects.all()
    context = {
        'articles':articles,
    }

    return render(request, 'articles/index.html', context)

# 글작성
@login_required
def create(request):

    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()

            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form':article_form,
    }
    return render(request, 'articles/create.html', context)

# 글수정
@login_required(login_url='common:login')
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.user != article.user :
        messages.error(request, '수정권한이 없습니다')
        return redirect('articles:detail', article_pk)

    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()

    else:
        article_form = ArticleForm(instance=article)

    context = {
        'article_form':article_form,
    }
    return render(request, 'articles/update.html', context)

# 글삭제
@login_required(login_url='common:login')
def delete_article(request, article_pk):
    article = Article.objects.get(pk=article_pk)  

    if request.user != article.user :
        messages.error(request, '삭제권한이 없습니다')
        return redirect('articles:detail', article_pk)

    article.delete()

    return redirect('articles:index')
   

# 글 조회

def article_detail(request, article_pk):

    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article,
    }
    return render(request,'articles/article_detail.html', context)

# 댓글 생성
@login_required
def add_comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()

            return redirect('articles:article_detail', article_pk)

    else:
        comment_form = CommentForm()
    
    context = {
        'comment_form':comment_form,
    }

    return render(request, 'articles/add_comment.html', context)

# 댓글 삭제
@login_required(login_url='common:login')
def delete_comment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article = Article.objects.get(pk=article_pk)

    if request.user != article.user :
        messages.error(request, '삭제권한이 없습니다')
        return redirect('articles:article_detail', article_pk)

    comment.delete()

    return redirect('articles:article_detail', article_pk)