from django.db import models
from django.conf import settings
from books.models import BookReview

# 엽서 이미지 테이블
class PostCardImage(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    review = models.ForeignKey(BookReview, on_delete=models.CASCADE)
    prompt = models.TextField()
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    delete_tf = models.BooleanField(default=False)

# 엽서 보관함 테이블
class PostCard(models.Model):
    sender = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='senders'
        )
    receiver = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receivers'
        )
    image = models.ForeignKey(PostCardImage, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)