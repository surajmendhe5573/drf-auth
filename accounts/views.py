from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Register View
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

# Login View
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer