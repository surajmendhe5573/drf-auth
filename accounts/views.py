from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, LoginSerializer

# Register View
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

# Login View
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
