from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# 카테고리 테이블
class Category(models.Model):
    category = models.CharField(max_length=50)

#책 목록 테이블
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    cover = models.URLField(max_length=512, blank=True, null=True)
    publisher = models.CharField(max_length=255)
    pub_date = models.DateField()
    author = models.CharField(max_length=255)
    customer_review_rank = models.PositiveIntegerField(default=0)

# 독후감 테이블
class BookReview(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 독후감 댓글 테이블
class Comment(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE
            )
    review = models.ForeignKey(BookReview, on_delete=models.CASCADE)
    content = models.TextField()
    comment_level = models.BooleanField(default=False)
    parent_comment_id = models.ForeignKey(
            'self',
            on_delete=models.CASCADE,
            null=True,
            blank=True,
        )
    created_at = models.DateTimeField(auto_now_add=True)

# 독후감 좋아요 테이블
class Like(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE
            )
    review = models.ForeignKey(BookReview, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)