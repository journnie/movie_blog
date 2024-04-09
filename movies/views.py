from django.shortcuts import render

# Create your views here.
def index(request):
    req_data = request.GET
    context = {
        'movie': req_data.get('movie')
    }
    return render(request, 'movies/index.html', context)

def create_movie(request):
    return render(request, 'movies/create_movie.html')

def movie_detail(request, movie):
    print(request)
    print(movie)
    return render(request, 'movies/movie_detail.html')
