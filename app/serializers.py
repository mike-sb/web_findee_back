from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers 

from .models import Profile
from . import views


class UserSerializer(serializers.ModelSerializer):
    # Сериализатор Юзера

    class Meta:
        model = User
        fields = ['id', 'username']


class RegisterSerializer(serializers.ModelSerializer):
    # Регистрация юзера

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user (
            validated_data['username'], 
            validated_data['username'],
            validated_data['password']
        )

        return user


class AuthSerializer(serializers.Serializer):
    # Авторизация юзера

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError("Неверные данные")


class ProfileCreateSerializer(serializers.ModelSerializer):
    # Создание профиля юзера
    
    class Meta:
        model = Profile
        fields = [
            'name', 'surname', 'patronymic', 
            'kind', 'regions', 'phone', 
            'company', 'categories', 'verify'
        ]

    def create(self, validated_data):
        profile = Profile.objects.create(user=self.context['request'].user, **validated_data)
        return profile


class ProfileSerializer(serializers.ModelSerializer):
    # Профиль юзера

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = [
            'user', 'name', 'surname', 
            'patronymic', 'kind', 'regions', 
            'phone', 'company', 'categories', 
            'verify'
        ]