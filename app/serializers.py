from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers 

from .models import Profile, Image
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


class ImageSerializer(serializers.ModelSerializer):
    # Картинки в портфолио

    class Meta:
        model = Image
        fields = ['id', 'image', 'text']

    def create(self, validated_data):
        image = Image.objects.create(profile=self.context['request'].user.profile, **validated_data)
        return image


class ProfileSerializer(serializers.ModelSerializer):
    # Профиль юзера

    user = UserSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Profile
        fields = [
            'user', 'name', 'surname', 
            'patronymic', 'birth_date', 'photo', 
            'kind', 'regions', 'phone', 
            'company', 'categories', 'about',
            'images', 'verify', 'premium'
        ]


class ProfileCreateSerializer(serializers.ModelSerializer):
    # Создание профиля юзера
    
    class Meta:
        model = Profile
        fields = [
            'name', 'surname', 'patronymic', 
            'birth_date', 'kind', 'regions', 
            'phone', 'company', 'categories'
        ]

    def create(self, validated_data):
        profile = Profile.objects.create(user=self.context['request'].user, **validated_data)
        return profile


class ProfileUpdateSerializer(serializers.ModelSerializer):
    # Изменение профиля юзера

    user = UserSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Profile
        fields = [
            'user', 'name', 'surname', 
            'patronymic', 'birth_date', 'photo',
            'kind', 'regions', 'phone', 
            'company', 'categories', 'about',
            'images','verify', 'premium'
        ]

    def validate(self, data):
        ban = ['name', 'surname', 'patronymic', 'birth_date', 'premium']
        
        if self.context['request'].user.profile.verify:
            for field in ban:
                if field in data:
                    raise serializers.ValidationError("Вы не можете изменить ФИО или дату рождения")

        return data