from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 데이터 목록 조회
def index(request):
    page = request.GET.get("page", "1")  # 처음 화면은 1페이지
    reviews = Review.objects.all().order_by("-created_at")
    paginator = Paginator(reviews, 10)  # 페이지당 10개씩
    page_obj = paginator.get_page(page)  # 모든 데이터를 가져오는것이 아니라 페이지의 데이터만 조회
    return render(request, "reviews/index.html", {"reviews": page_obj})


# 데이터 작성
@login_required(login_url="accounts:user_login")
def create(request):

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect("/")

    else:
        form = ReviewForm()

    return render(request, "reviews/create.html", {"form": form})


# 게시물 조회 + 댓글폼
def detail(request, review_pk):

    review = get_object_or_404(Review, pk=review_pk)

    form = CommentForm()
    return render(request, "reviews/detail.html", {"review": review, "form": form})


# 게시물 수정
@login_required(login_url="accounts:user_login")
def update(request, review_pk):

    review = get_object_or_404(Review, pk=review_pk)

    if request.user != review.author:
        messages.error(request, "권한이 없습니다.")
        return redirect("reviews:review_detail", review_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect("reviews:detail", review_pk)

    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/update.html", {"form": form})


# 게시물 삭제
@login_required(login_url="accounts:user_login")
def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.user != review.author:
        messages.error(request, "권한이 없습니다.")
        return redirect("reviews:review_detail", review_pk)

    else:
        review.delete()
        return redirect("reviews:index")


# 게시물 좋아요
@login_required(login_url="accounts:user_login")
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.user in review.review_likes.all(): 
        review.review_likes.remove(request.user)
        existed_user = False
    
    else:
        review.review_likes.add(request.user)
        existed_user = True
    likeCount = review.review_likes.count()
    context = {
        "existed_user": existed_user,
        "likeCount": likeCount,
    }
    
    return JsonResponse(context)


# 댓글 작성
@login_required(login_url="accounts:user_login")
def comments_create(request, review_pk):

    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.review = review
            comment.save()
            context = {
                "commentAuthorUsername": comment.author.username,
                "commentContent": comment.content,
                "commentId": comment.id,
                "commentReviewId": comment.review.id,
            }

            return JsonResponse(context)

    else:
        form = CommentForm()

        return (request, "reviews/detail.html", {"form": form})


# 댓글 삭제
@login_required(login_url="accounts:user_login")
def comments_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user != comment.author:
        messages.error(request, "권한이 없습니다.")
        return redirect("reviews:review_detail", review_pk)

    comment.delete()
    return redirect("reviews:detail", review_pk)
