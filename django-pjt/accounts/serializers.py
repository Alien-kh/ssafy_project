# accounts/serializers.py

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import Follow

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['age'] = self.validated_data.get('age', '')
        return data
    
    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get('age', '')
        user.save()
        return user
    

# 팔로우 serializer
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'