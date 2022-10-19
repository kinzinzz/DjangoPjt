from turtle import right
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
# Create your views here.

# 메인 화면 
def main(request):

    return render(request, 'articles/main.html')

# 생성

def create(request):

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('articles:index')
    else:
        review_form = ReviewForm()

    context = {
        'review_form': review_form
    }

    return render(request, 'articles/create.html', context)

# 목록 조회

def index(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews
    }

    return render(request, 'articles/index.html', context)

# 정보 조회

def detail(request, pk):

    review = Review.objects.get(pk=pk)

    context = {
        'review': review,
    }
    return render(request, 'articles/detail.html', context)

# 수정

def update(request, pk):

    review = Review.objects.get(pk=pk)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()

            return redirect('articles:index')

    else:
        review_form = ReviewForm(instance=review)

    context = {
        'review_form': review_form,
    }
    return render(request, 'articles/update.html', context)

# 삭세

def delete(request, pk):

    review = Review.objects.get(pk=pk)
    review.delete()

    return redirect('articles:index')