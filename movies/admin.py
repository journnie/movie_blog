from django.contrib import admin
from .models import Movie
# Register your models here.

admin.site.register(Movie) # 관리자 사이트에 Movie 모델 추가하겠음
# admin.site.register(Article) # 관리자 사이트에 Movie 모델 추가하겠음