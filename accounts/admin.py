from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# accounts/admin.py
# Admin site 출력을 위해 생성한 user model 등록
admin.site.register(User, UserAdmin)