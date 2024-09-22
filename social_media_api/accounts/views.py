from rest_framework.response import Response
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import CustomUser
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import Post
from .serializers import PostSerializer



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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
	try:
		user_to_follow = CustomUser.objects.get(id=user_id)
		request.user.following.add(user_to_follow)
		return Response(status=status.HTTP_204_NO_CONTENT)
	except CustomUser.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
	try:
		user_to_unfollow = CustomUser.objects.get(id=user_id)
		request.user.following.remove(user_to_unfollow)
		return Response(status=status.HTTP_204_NO_CONTENT)
	except CustomUser.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

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
	

class UserFeedView(generics.ListAPIView):
	serializer_class = PostSerializer

	def get_queryset(self):
		# Get the list of users the current user follows
		following_users = self.request.user.following.all()
		return Post.objects.filter(author__in=following_users).order_by('-created_at')
