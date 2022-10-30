from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.


def index(request):

    return render(request, "articles/index.html")


def follow(request, pk):

    user = get_user_model().objects.get(pk=pk)
    if request.user == user:
        return redirect("articles:detail", pk)

    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    user.followers.add(request.user)  # pk의 팔로워가 증가
    return redirect("articles:detail", pk)
