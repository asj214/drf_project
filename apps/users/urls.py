from django.urls import path
from .views import (
    LoginView,
    AuthMeView,
    RegisterUserView,
)


urlpatterns = [
    path(r'auth/register', RegisterUserView.as_view()),
    path(r'auth/login', LoginView.as_view()),
    path(r'auth/me', AuthMeView.as_view()),
]
