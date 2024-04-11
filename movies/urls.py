from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:movie_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<int:movie_pk>/', views.edit, name='edit'),
    path('update/', views.update, name='update'),
    path('delete/<int:movie_pk>', views.delete, name='delete')
]
