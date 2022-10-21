from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreatrionForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.

# 회원가입
def signup(request):

    if request.method == 'POST':
        signup_form = CustomUserCreatrionForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # 회원가입하면 자동으로 로그인
            username = signup_form.cleaned_data.get("username")
            direct_password = signup_form.cleaned_data.get("password1")
            user = authenticate(username=username, password=direct_password)
            user_login(request, user)
            return redirect('/')
    
    else:
        signup_form = CustomUserCreatrionForm()

    context = {
        'signup_form':signup_form,
    }

    return render(request, 'accounts/signup.html', context)

# 로그인
def login(request):

    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user_login(request, login_form.get_user())
            return redirect('/')
    
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

    return redirect('/')

# 프로필
@login_required
def user_detail(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.user != user:
        messages.error(request, '권한이 없습니다.')
        
        return redirect('/')
  

    context = {
        'user':user,
    }
    return render(request, 'accounts/user_detail.html', context)


# 회원정보 수정
@login_required(login_url='common:login')
def user_update(request, user_pk):
    user = User.objects.get(pk=user_pk)

    if request.user != user:
        messages.error(request, '권한이 없습니다.')
       
        return redirect('accounts:user_detail', user_pk)

    if request.method == 'POST':
        update_form = CustomUserChangeForm(request.POST, data=request.user)
        if update_form.is_valid():
            update_form.save()
            
            return redirect('acconts:user_detail', user_pk)

    else: 
        update_form = CustomUserChangeForm(data=request.user)

    context = {
        'update_form':update_form,
    }

    return render(request, 'accounts/user_update.html', context)