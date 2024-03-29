from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    # req_data = request.GET
    # context = {
    #     'movie': req_data.get('movie')
    # }
    return render(request, 'movies/index.html', context)


def create(request):
    # saving
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form
            movie.save()
            return redirect('movies:index')

    # create
    form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)

# def create(request):
#     if request.method == 'POST':
#         data = request.POST
#         movie = Movie()
#         movie.title = data.get('title')
#         movie.content = data.get('content')
#         movie.save()
#         return redirect('movies:detail', movie_pk=movie.pk)
#
#     return render(request, 'movies/create.html')


def edit(request, movie_pk):
    # print(request.method)
    # movie = Movie.objects.get(pk=movie_pk)
    # print(movie.title)
    # context = {
    #     'movie': movie
    # }
    movie = Movie.objects.get(pk=movie_pk)
    form = MovieForm(request.POST, instance=movie)
    context = {
        'form': form,
        'movie': movie
    }
    print(movie)
    return render(request, 'movies/edit.html', context)


def delete(request, movie_pk):
    Movie.objects.get(pk=movie_pk).delete()
    return redirect('movies:index')


def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }
    # data = request.POST
    # print(data)
    # movie = Movie()
    # movie.title = data.get('title')
    # movie.content = data.get('content')
    # movie.save()
    return render(request, 'movies/detail.html', context)


# 두개 합쳐서 쓸모 없어짐
def old_create(request):
    return render(request, 'movies/create.html')


def update(request):
    print('update')
    data = request.POST
    movie = Movie()
    movie.title = data.get('title')
    movie.content = data.get('content')
    movie.save()
    print('updated')
    return redirect('movies:detail', movie_pk=movie.pk)
