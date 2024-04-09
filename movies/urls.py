from django.urls import path
from . import views

appname = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:movie>/', views.detail, name='detail'),
    path('create/', views.create),
]
