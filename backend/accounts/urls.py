from django.urls import path
from .views import(
    RegisterView,
    CurrentUserView,
    UpdateProfileView,
    ChangePasswordView
)
from rest_framework_simplejwt.views import(
    TokenRefreshView,
    TokenObtainPairView
)

urlpatterns = [
    path("register/",RegisterView.as_view()),
    path("login/",TokenObtainPairView.as_view()),
    path("refresh/",TokenRefreshView.as_view()),
    path("me/",CurrentUserView.as_view()),
    path("profile/update/",UpdateProfileView),
    path("change-password/",ChangePasswordView()),
    
]

