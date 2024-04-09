from django.urls import path
from . import views

appname = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]
