from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import User
# Create your views here.
def index(request):

    return render(request, 'index.html')


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

def accounts(request):

    users = User.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'accounts/accounts.html', context)

def detail(request, pk):

    user = User.objects.get(pk=pk)

    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)