from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
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
@login_required(login_url='accounts:login')
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
@login_required(login_url='accounts:login')
def user_update(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.user != user:
        messages.error(request, '권한이 없습니다.')
        
        return redirect('/')
    if request.method == 'POST':
        update_form = CustomUserChangeForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            
            return redirect('accounts:user_detail', user_pk)

    else: 
        update_form = CustomUserChangeForm(instance=request.user)

    context = {
        'update_form':update_form,
    }

    return render(request, 'accounts/user_update.html', context)
    
# 비밀번호 변경
@login_required(login_url='accounts:login')
def password_change(request, user_pk):

    user = User.objects.get(pk=user_pk)
    if request.user != user:
        messages.error(request, '권한이 없습니다.')
        
        return redirect('/')
    
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, request.user)

            return redirect('accounts:user_detail', user_pk)

    else:
        
        password_form = PasswordChangeForm(request.user)

    context = {
        'password_form':password_form,
    }
    return render(request, 'accounts/password_change.html', context)


@login_required(login_url='accounts:login')
def delete(request, user_pk):

    user = User.objects.get(pk=user_pk)
    if request.user != user:
        messages.error(request, '권한이 없습니다.')
        
        return redirect('/')
    
    user.delete()
    user_logout(request)
    
    return redirect('/')