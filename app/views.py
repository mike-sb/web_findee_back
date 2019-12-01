from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    UserSerializer, RegisterSerializer, 
    AuthSerializer, ProfileSerializer,
    ProfileCreateSerializer, ProfileUpdateSerializer
)
from .models import Profile
from .permissions import IsOwner


class UserDetail(generics.RetrieveAPIView):
    # Получение информации о юзере

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserRegister(generics.GenericAPIView):
    # Регистрация юзера

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token-access": str(refresh.access_token),
        })


class UserLogin(generics.GenericAPIView):
    # Вход юзера

    serializer_class = AuthSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token-access": str(refresh.access_token),
        })


class ProfileCreate(generics.CreateAPIView):
    # Создание профиля юзера

    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProfileDetail(generics.RetrieveAPIView):
    # Информация о профиле юзера

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]
    lookup_field = 'user__id'


class ProfileUpdate(generics.UpdateAPIView):
    # Обновление профиля юзера

    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    lookup_field = 'user__id'