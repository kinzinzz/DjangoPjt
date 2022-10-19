from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

# 홈페이지


def main(request):

    return render(request, "base.html")


# 회원가입


def signup(request):

    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get("username")
            direct_password = user_form.cleaned_data.get("password1")
            user = authenticate(username=username, password=direct_password)
            user_login(request, user)
            return redirect("/")

    else:
        user_form = CustomUserCreationForm()

    context = {
        "user_form": user_form,
    }
    return render(request, "accounts/signup.html", context)


# 로그인


def login(request):

    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user_login(request, login_form.get_user())
            return redirect("/")

    else:
        login_form = AuthenticationForm()

    context = {
        "login_form": login_form,
    }
    return render(request, "accounts/login.html", context)


# 로그아웃


@login_required
def logout(request):

    user_logout(request)

    return redirect("/")


# 회원 목록 조회


@login_required
def index(request):

    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


# 회원 프로필 조회


@login_required
def detail(request, pk):

    user = User.objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


# 회원정보 수정


@login_required
def update(request):

    if request.method == "POST":
        update_form = CustomUserChangeForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()

            return redirect("accounts:detail", request.user.pk)

    else:
        update_form = CustomUserChangeForm(instance=request.user)

    context = {
        "update_form": update_form,
    }

    return render(request, "accounts/update.html", context)


# 비밀번호 변경


@login_required
def password_change(request):

    if request.method == "POST":
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, request.user)

            return redirect("accounts:detail", request.user.pk)

    else:
        password_form = PasswordChangeForm(request.user)

    context = {
        "password_form": password_form,
    }

    return render(request, "accounts/password_change.html", context)


# 회원 탈퇴


@login_required
def delete(request):

    request.user.delete()
    user_logout(request)

    return redirect("/")


# 검색


@login_required
def search(request):

    if "검색어" in request.GET:
        query = request.GET.get("검색어")

        users = User.objects.all().filter(Q(username__icontains=query))

        context = {
            "query": query,
            "users": users,
        }

        return render(request, "accounts/search.html", context)
