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


class ProfileSerializer(serializers.ModelSerializer):
    # Профиль юзера

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = [
            'user', 'name', 'surname', 
            'patronymic', 'birth_date', 'photo', 
            'kind', 'regions', 'phone', 
            'company', 'categories', 'verify'
        ]


class ProfileCreateSerializer(serializers.ModelSerializer):
    # Создание профиля юзера
    
    class Meta:
        model = Profile
        fields = [
            'name', 'surname', 'patronymic', 
            'birth_date', 'kind', 'regions', 
            'phone', 'company', 'categories', 
            'verify'
        ]

    def create(self, validated_data):
        profile = Profile.objects.create(user=self.context['request'].user, **validated_data)
        return profile


class ProfileUpdateSerializer(serializers.ModelSerializer):
    # Изменение профиля юзера

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = [
            'user', 'name', 'surname', 
            'patronymic', 'birth_date', 'photo',
            'kind', 'regions', 'phone', 
            'company', 'categories', 'verify'
        ]

    def validate(self, data):
        if self.context['request'].user.profile.verify:
            if 'name' in data or 'surname' in data or 'patronymic' in data or 'birth_date' in data:
                raise serializers.ValidationError("Вы не можете изменить ФИО или дату рождения")
        else:
            if 'verify' in data:
                raise serializers.ValidationError("Ошибка")

        return data