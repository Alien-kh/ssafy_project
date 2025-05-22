# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 유저 테이블
class User(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    
# 팔로워 테이블
class Follow(models.Model):
    follower = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follower'
        )
    following = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following'
        )
    created_at = models.DateTimeField(auto_now_add=True)