# diaries/serializers.py
from rest_framework import serializers
from .models import Diary

# 일기 리스트 serializer
class DiaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'

# 일기 단건건 serializer
class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'