from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter

from .views import UserRegister, UserLogin

urlpatterns = [
    path('register/', csrf_exempt(UserRegister.as_view())),
    path('login/', csrf_exempt(UserLogin.as_view())),
]
