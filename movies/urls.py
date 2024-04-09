from django.urls import path
from . import views

appname = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:movie>/', views.movie_detail, name='movie_detail'),
    path('create_movie/', views.create_movie),
]
