from django.db import models
from django.conf import settings
from books.models import Book
# 추천도서 테이블블
class Recommendation(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)