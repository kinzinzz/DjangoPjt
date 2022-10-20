from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
# Create your views here.

# 회원가입
def signup(request):

    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()

            return redirect('accounts:login')
    else:
        signup_form = CustomUserCreationForm()
    context = {
        'signup_form':signup_form,
    }
    return render(request,'accounts/signup.html', context)
    
# 로그인
def login(request):

    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user_login(request, login_form.get_user())
            return redirect('articles:index')

    else:
        login_form = AuthenticationForm()
    context = {
        'login_form':login_form,
    }
    return render(request, 'accounts/login.html', context)
    
# 로그아웃
@login_required
def logout(request):
    user_logout(request)
    return redirect('articles:index')

# 사용자 상세조회
@login_required
def user_detail(request, user_pk):
    user = User.objects.get(pk=user_pk)
    context = {
        'user':user,
    }
    return render(request, 'accounts/user_detail.html', context)

# 회원정보 조회
@login_required
def user_detail(request, user_pk):
    user = User.objects.get(pk=user_pk)

    if request.user != user :
        messages.error(request, '권한이 없습니다')
        return redirect('articles:index')

    context = {
        'user':user,
    }
    return render(request, 'accounts/user_detail.html', context)