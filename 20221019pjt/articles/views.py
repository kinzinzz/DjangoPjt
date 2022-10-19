from django.shortcuts import render, redirect
from .models import Articles, Comments
from .forms import Articles_Form, Comments_Form
from django.contrib.auth.decorators import login_required
# Create your views here.

# 메인 화면

def index(request):
    articles = Articles.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

# 글 생성
@login_required
def create(request):

    if request.method == 'POST':
        articles_form = Articles_Form(request.POST)
        if articles_form.is_valid():
            article = articles_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index') 

    else:
        article_form = Articles_Form()

    context = {
        'article_form':article_form,
    }

    return render(request, 'articles/create.html', context)

# 글 상세 조회
@login_required
def detail(request, article_pk):

    article = Articles.objects.get(pk=article_pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

# 댓글 생성
@login_required
def add_comment(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    if request.method == 'POST':
        comment_form = Comments_Form(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect('articles:detail', article_pk)
    else:
        comment_form = Comments_Form()
    
    context = {
        'comment_form':comment_form,
    } 
    
    return render(request,'articles/add_comment.html', context)

# 댓글 삭제
@login_required
def delete_comment(request, article_pk, comment_pk):
    comment = Comments.objects.get(pk=comment_pk)
    comment.delete()
    
    return redirect('articles:detail', article_pk)
