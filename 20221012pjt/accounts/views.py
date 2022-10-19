from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# 홈페이지
def index(request):

    return render(request, 'base.html')

# 회원가입
def signup(request):

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            
            return redirect('/')
    else:   
        user_form = CustomUserCreationForm()

    context = {
        'user_form': user_form 
    }
    return render(request,'accounts/signup.html', context)

# 회원목록
@login_required
def accounts(request):

    users = User.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'accounts/accounts.html', context)

# 프로필
def profile(request, pk):

    user = User.objects.get(pk=pk)

    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)

# 로그인
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
def logout(request):

    auth_logout(request)
    return redirect('/')

# 프로필 수정
def profile_update(request, pk):

    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:accounts')
    else: 
        user_form = CustomUserCreationForm(instance=user)
    context = {
        'user_form':user_form,
    }

    return render(request, 'accounts/profile_update.html', context)
    


