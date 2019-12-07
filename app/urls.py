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

    path('profile/<int:user__id>/rating/add/', csrf_exempt(views.RatingAdd.as_view())),
    path('profile/<int:user__id>/comment/add/', csrf_exempt(views.CommentAdd.as_view())),

    path('image/<int:pk>/', views.ImageDetail.as_view(), name="image-detail"),
    path('image/create/', views.ImageCreate.as_view(), name="image-create"),
    path('image/<int:pk>/update/', views.ImageUpdate.as_view(), name="image-update"),
    path('image/<int:pk>/delete/', views.ImageDelete.as_view(), name="image-delete")
]
