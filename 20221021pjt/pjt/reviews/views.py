from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.contrib import messages

# Create your views here.

# 리뷰 전체조회
def index(request):

    reviews = Review.objects.all()
    context = {
        'reviews':reviews,
    }
    return render(request, 'reviews/index.html', context)


# 리뷰 생성
@login_required
def review_create(request):

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:index')
        
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form    
    }
    return render(request, 'reviews/create.html', context)

# 리뷰 목록 조회
def index(request):
    reviews = Review.objects.all()

    context = {
        'reviews':reviews,
    }
    return render(request, 'reviews/index.html', context)

# 리뷰 상세조회
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review':review,
    }

    return render(request, 'reviews/review_detail.html', context)

# 리뷰 수정(리뷰 작성자만 수정)
@login_required(login_url='accounts:login')
def review_update(request, review_pk):

    review = Review.objects.get(pk=review_pk)
    
    if request.user != review.user:
        messages.error(request,'권한이 없습니다.')
        return redirect('reviews:review_detail', review_pk)
    
    if request.method == 'POST':
        update_form = ReviewForm(request.POST, instance=review)
        if update_form.is_valid():
            update_form.save()
            return redirect('reviews:review_detail', review_pk)

    else:
         update_form = ReviewForm(instance=review)
    
    context = {
        'update_form':update_form,
    }

    return render(request, 'reviews/review_update.html', context)


# 리뷰 삭제(리뷰 작성자만 수정)
@login_required(login_url='accounts:login')
def review_delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
        
    if request.user != review.user:
        messages.error(request,'권한이 없습니다.')
        return redirect('reviews:review_detail', review_pk)
    
    review.delete()
    
    return redirect('reviews:index')

# 코멘트 추가
@login_required
def comment_add(request, review_pk):

    review = Review.objects.get(pk=review_pk)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user 
            comment.save() 
            return redirect('reviews:review_detail', review_pk)   

    else:
        comment_form = CommentForm()
    
    context = {
        'comment_form':comment_form,
    }

    return render(request, 'reviews/comment_add.html', context)

# 코멘트 삭제(코멘트 작성자만 수정)
@login_required(login_url='accounts:login')
def comment_delete(request, review_pk, comment_pk):
   
    comment = Comment.objects.get(pk=comment_pk)

    if request.user != comment.user:
        messages.error(request, '권한이 없습니다.')
        return redirect('reviews:review_detail', review_pk)

    comment.delete()
    return redirect('reviews:review_detail', review_pk)

# 코멘트 수정(코멘트 작성자만 수정)
@login_required(login_url='accounts:login')
def comment_update(request, review_pk, comment_pk):
   
    comment = Comment.objects.get(pk=comment_pk)

    if request.user != comment.user:
        messages.error(request, '권한이 없습니다.')
        return redirect('reviews:review_detail', review_pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('reviews:review_detail', review_pk)

    else:
        comment_form = CommentForm(instance=comment)

    context = {
        'comment_form':comment_form,
    }

    return render(request, 'reviews/comment_update.html', context)