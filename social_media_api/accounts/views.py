from rest_framework.response import Response
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import CustomUser
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
	serializer_class = RegisterSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user, token = serializer.save()

		return Response({
			"user": {
				"username": user.username,
				"email": user.email,
				"bio": user.bio,
			},
			"token": token.key  # Return the token in the response
		})


class LoginView(ObtainAuthToken):
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({
			'token': token.key,
			'user_id': user.pk,
			'username': user.username
		})

class UserProfileView(generics.RetrieveUpdateAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return self.request.user  # Return the authenticated user's profile
