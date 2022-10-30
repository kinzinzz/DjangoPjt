from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse


# 회원가입
def signup(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")

    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


# 로그인
def user_login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")

    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


# 로그아웃
@login_required(login_url="accounts:user_login")
def user_logout(request):

    logout(request)

    return redirect("/")


# 회원정보 조회
@login_required(login_url="accounts:user_login")
def user_detail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    return render(request, "accounts/user_detail.html", {"user": user})


# 회원정보 변경
@login_required(login_url="accounts:user_login")
def profile_change(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    if request.user != user:
        messages.error(request, "권한이 없습니다.")
        return redirect("reviews:review_detail", user_pk)

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("accounts:user_detail", user_pk)
    else:
        form = form = CustomUserChangeForm(instance=user)

    return render(request, "accounts/profile_change.html", {"form": form})


# 비밀번호 변경
@login_required(login_url="accounts:user_login")
def password_change(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    if request.user != user:
        messages.error(request, "권한이 없습니다.")
        return redirect("reviews:review_detail", user_pk)

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)

            return redirect("accounts:user_detail", user_pk)

    else:
        form = PasswordChangeForm(request.user)

    return render(request, "accounts/password_change.html", {"form": form})


# 회원 탈퇴
@login_required(login_url="accounts:user_login")
def user_delete(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    if request.user != user:
        messages.error(request, "권한이 없습니다.")
        return redirect("reviews:review_detail", user_pk)

    user.delete()
    user_logout(request)

    return redirect("reviews:index")


# 팔로우
@login_required(login_url="accounts:user_login")
def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    if request.user == user:
        userFollowings = user.followings.count()
        userFollowers = user.follower.count()
        
        self_follow = True
        context = {
            'self_follow':self_follow,
            'userFollowings':userFollowings,
            'userFollowers':userFollowers,
        }
     
        return JsonResponse(context)

    else:
        if request.user in user.followings.all():
            user.followings.remove(request.user)
            exited_user = False

        else:
            user.followings.add(request.user)
            exited_user = True
            
        userFollowings = user.followings.count()
        userFollowers = user.follower.count()
        context = {
            'exited_user':exited_user,
            'userFollowings':userFollowings,
            'userFollowers':userFollowers,
        }
        print(user.followings.all())
        print(user.follower.all())
        return JsonResponse(context)

