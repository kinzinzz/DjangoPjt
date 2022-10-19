import re
from django.shortcuts import render, redirect
from .forms import CustomUserCreationFrom, CustomUserChangeForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db.models import Q
# Create your views here.

# 메인화면

def index(request):
    
    return render(request, 'base.html')

# 회원가입
def signup(request):

    if request.method == 'POST':
        user_form = CustomUserCreationFrom(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/')

    else:
        user_form = CustomUserCreationFrom()

    context = {
        'user_form': user_form,
    }
    return render(request, 'accounts/signup.html', context)

# 전체 회원 조회
@login_required

def user_list(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request,'accounts/user_list.html',context)

@login_required
# 회원 상세 조회

def detail(request, pk):

    user = User.objects.get(pk=pk)
    context = {
        'user':user,
    }
    return render(request, 'accounts/detail.html', context)

# 로그인

def user_login(request):
    
    if request.method == 'POST':
        login_form = AuthenticationForm(request,data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())           
            return redirect('/')
    else:
        login_form = AuthenticationForm()

    context = {
        'login_form':login_form,
    }
    return render(request,'accounts/login.html',context)

# 로그아웃
def user_logout(request):
    
    logout(request)
    return redirect('/')

@login_required
# 회원정보 수정
def update(request, pk):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:detail', request.user.pk)
    
    else:
        user_form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'user_form':user_form,
    }
    return render(request,'accounts/update.html', context)

# 비밀번호 변경

@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            # 비밀번호 병경후 자동 로그인(세션 업데이트를 자동으로 해줌)
            # login(request, user)를 할 경우 비밀번호 변경전 세션으로 새로변경한 비밀번호의 세션과 충돌
            update_session_auth_hash(request, password_form.user)
            return redirect('accounts:detail', request.user.pk)
    else:
        password_form = PasswordChangeForm(request.user)

    context = {
        'password_form': password_form,
    }
    return render(request,'accounts/change_password.html', context)

#탈퇴
@login_required
def delete(request):
    # 탈퇴후 > 로그아웃 해야한다
    request.user.delete()
    logout(request)

    return redirect('/')

#회원검색
@login_required
def search(request):

    if 'kw' in request.GET:
        query = request.GET.get('kw')
        users = User.objects.all().filter(
            Q(username__icontains = query)
        )
    context = {
        'query': query,
        'users': users,
    }

    return render(request, 'accounts/search.html', context)
