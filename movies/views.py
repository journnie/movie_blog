from django.shortcuts import render

# Create your views here.
def index(request):
    req_data = request.GET
    context = {
        'movie': req_data.get('movie')
    }
    return render(request, 'movies/index.html', context)

def create(request):
    return render(request, 'movies/create.html')

def detail(request, movie):
    return render(request, 'movies/detail.html')
