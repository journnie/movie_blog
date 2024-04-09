from django.db import models

# Create your models here.
class Movie(models.Model): # 클래스 명은 테이블 이름
    # 각 변수 명은 필드 명
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_open = models.BooleanField(default=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
