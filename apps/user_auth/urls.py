from django.urls import path
from .views import GoogleLogin, login_view, RegisterView, GoogleLoginCallback

urlpatterns = [
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('auth/google/callback/',GoogleLoginCallback.as_view(), name="google_login_callback")
]