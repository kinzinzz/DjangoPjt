from django.shortcuts import render,redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.

# 메인페이지
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'articles/index.html', context)

# 생성
def create(request):

    if request.method == 'POST':

        movie_form = MovieForm(request.POST)

        if movie_form.is_valid():
            movie_form.save()
            return redirect('articles:index')
    else:
        movie_form = MovieForm()

    context = {
        'movie_form': movie_form,
    }

    return render(request, 'articles/create.html', context)

# 상세

def detail(request, pk):

    movie = Movie.objects.get(pk=pk)

    context = {
        'movie': movie,
    }
    return render(request, 'articles/detail.html', context)

# 수정

def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('articles:detail', movie.pk)

    else:
        movie_form = MovieForm(instance=movie)

    context = {
        'movie_form': movie_form,
    }
    return render(request, 'articles/update.html', context)

# 삭제

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()

    return redirect('articles:index')
    