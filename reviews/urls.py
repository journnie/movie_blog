from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:review_pk>/', views.detail, name='detail'),
    path('delete/<int:review_pk>', views.delete, name='delete')
]