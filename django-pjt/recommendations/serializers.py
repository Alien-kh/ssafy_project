# recommendeations/serializers.py

from rest_framework import serializers
from .models import Recommendation

# 추천도서 serializer
class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'