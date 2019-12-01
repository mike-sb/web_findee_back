from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('register/', csrf_exempt(views.UserRegister.as_view())),
    path('login/', csrf_exempt(views.UserLogin.as_view())),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('profile/<int:user__id>/', views.ProfileDetail.as_view()),
    path('profile/create/', csrf_exempt(views.ProfileCreate.as_view())),
    path('profile/<int:user__id>/update/', csrf_exempt(views.ProfileUpdate.as_view())),
]
