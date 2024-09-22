from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import RegisterSerializer, UserProfileSerializer
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
	queryset = CustomUser.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = RegisterSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Override get_object to return the currently authenticated user
        return self.request.user