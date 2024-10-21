from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response
from .serializers import UserSerializerSocial
from django.shortcuts import render


@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)



User = get_user_model()

class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializerSocial  # Deberás crear este serializador

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

