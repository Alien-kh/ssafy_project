from django.db import models
from django.conf import settings

# 일기 테이블
class Diary(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    diary_date = models.DateField()
    content = models.TextField()
    weather = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)