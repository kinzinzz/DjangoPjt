from django.shortcuts import render

# Create your views here.
from .models import Articles
from django.shortcuts import render, redirect
from .forms import ArticleForm

# Create your views here.


def index(request):

    form = ArticleForm()
    accounts = Articles.objects.all()

    return render(request, "accounts/index.html", {"form": form, "accounts": accounts})


def create(request):

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect("accounts:index")

    else:
        form = ArticleForm()
    return render(request, "accounts/index.html", {"form": form})
