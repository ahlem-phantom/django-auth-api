from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'api_key']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},  # Ensure password is required and write-only
            'first_name': {'required': True},  # Ensure first_name is required
            'last_name': {'required': True},   # Ensure last_name is required
        }

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
