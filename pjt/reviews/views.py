from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, ReviewForm
from .models import Review, Comment
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

# 게시글 생성


@login_required
def create(request):

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.UserID = request.user
            review.save()
            return redirect("reviews:index")

    else:
        review_form = ReviewForm()

    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/create.html", context)


# 게시글 전체 조회


def index(request):

    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


# 게시글 상세 조회


def detail(request, review_pk):

    review = Review.objects.get(pk=review_pk)
    context = {
        "review": review,
    }

    return render(request, "reviews/detail.html", context)


# 게시글 수정


@login_required
def update(request, review_pk):

    review = Review.objects.get(pk=review_pk)

    if request.method == "POST":
        update_form = ReviewForm(request.POST, instance=review)
        if update_form.is_valid():
            update_form.save()

            return redirect("reviews:index")

    else:
        update_form = ReviewForm(instance=review)

    context = {
        "update_form": update_form,
    }

    return render(request, "reviews/update.html", context)


# 글 삭제


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()

    return redirect("reviews:index")


# 검색


def search(request):

    if "검색어" in request.GET:
        query = request.GET.get("검색어")

        reviews = Review.objects.all().filter(Q(title__icontains=query))

        context = {
            "query": query,
            "reviews": reviews,
        }

        return render(request, "reviews/search.html", context)


# 댓글 쓰기


@login_required
def add_comment(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()

            return redirect("reviews:detail", review.pk)
    else:
        comment_form = CommentForm()

    context = {
        "comment_form": comment_form,
    }
    return render(request, "reviews/add_comment.html", context)


# 댓글 수정


@login_required
def comment_modify(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()

            return redirect("reviews:detail", comment.review.pk)

    else:
        comment_form = CommentForm(instance=comment)

    context = {
        "comment_form": comment_form,
    }

    return render(request, "reviews/add_comment.html", context)


# 댓글 삭제


@login_required
def comment_remove(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect("articles:detail", comment.articles.pk)
