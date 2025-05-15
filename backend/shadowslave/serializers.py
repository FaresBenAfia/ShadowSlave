# characters/serializers.py
from rest_framework import serializers
from .models import Character
# app/serializers.py
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'true_name', 'age', 'vital_status', 'rank', 'class_name', 'aspect', 'flaw', 'image']