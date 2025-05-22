from rest_framework import serializers
from .models import Book,BookReview,Like,Comment

# 책 리스트 serializer
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
# 독후감 리스트 serializer
class BookReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = '__all__'

# 독후감 단건 serializer
class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = '__all__'

# 댓글 serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# 좋아요 serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'



# # articles/serializers.py
# class ArticleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ('id', 'title', 'content')


# # articles/serializers.py
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = ('user',)
