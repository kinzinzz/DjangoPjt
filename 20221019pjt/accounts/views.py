from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from articles.models import Articles,Comments
# Create your views here.

# 로그인
def user_login(request):

    if request.method == 'POST':
        login_form = AuthenticationForm(request,data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())

            return redirect('articles:index')

    else:
        login_form = AuthenticationForm()

    context = {
        'login_form':login_form,
    }
    
    return render(request, 'accounts/login.html', context)


# 로그아웃
@login_required
def user_logout(request):

    logout(request)

    return redirect('articles:index')

# 프로필
@login_required
def detail(request, pk):
    user = User.objects.get(pk=pk)
   
    context = {
        'user':user,
    }

    return render(request, 'accounts/detail.html', context)

