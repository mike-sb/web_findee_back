from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers
from .models import Profile, Image, Rating
from .permissions import IsOwner, IsOwnerOfImage


class UserDetail(generics.RetrieveAPIView):
    # Получение информации о юзере

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]


class UserRegister(generics.GenericAPIView):
    # Регистрация юзера

    serializer_class = serializers.RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "token-access": str(refresh.access_token),
        })


class UserLogin(generics.GenericAPIView):
    # Вход юзера

    serializer_class = serializers.AuthSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "token-access": str(refresh.access_token),
        })


class ProfileCreate(generics.CreateAPIView):
    # Создание профиля юзера

    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileCreateSerializer
    permission_classes = [IsAuthenticated]


class ProfileDetail(generics.RetrieveAPIView):
    # Информация о профиле юзера

    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__id'


class ProfileUpdate(generics.UpdateAPIView):
    # Обновление профиля юзера

    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'user__id'


class ImageCreate(generics.CreateAPIView):
    # Создание картинки в портфолио

    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageDetail(generics.RetrieveAPIView):
    # Информация о картинке в портфолио

    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageUpdate(generics.UpdateAPIView):
    # Обновление картинки в портфолио

    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfImage]


class ImageDelete(generics.DestroyAPIView):
    # Удаление картинки из портфолио

    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfImage]


class RatingAdd(generics.GenericAPIView):
    # Отправка оценки специалисту

    serializer_class = serializers.RatingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, user__id):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=Profile.objects.get(user__id=self.kwargs['user__id']))

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentAdd(generics.GenericAPIView):
    # Добавление отзыва о специалисте

    serializer_class = serializers.CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, user__id):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            from_profile=request.user.profile, 
            to_profile=Profile.objects.get(user__id=self.kwargs['user__id'])
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)