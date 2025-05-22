# postcardes/serializers.py
from rest_framework import serializers
from .models import PostCard,PostCardImage

# 엽서 이미지 리스트 serializer
class PostCardImagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCardImage
        fields = '__all__'

# 엽서 이미지 단건 serializer
class PostCardImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCardImage
        fields = '__all__'

# 엽서 리스트 serializer
class PostCardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCard
        fields = '__all__'


# 엽서 단건 serializer
class PostCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCard
        fields = '__all__'