from django.urls import path
from .views import GoogleLogin, login_view, RegisterView

urlpatterns = [
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]