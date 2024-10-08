from rest_framework import viewsets, permissions, status, generics
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('-created_at')
	serializer_class = PostSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['title', 'content']

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all().order_by('-created_at')
	serializer_class = CommentSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
	# Use get_object_or_404 to handle fetching the post or raising a 404
	post = generics.get_object_or_404(Post, pk=pk)
	like, created = Like.objects.get_or_create(user=request.user, post=post)

	if created:
		# Create a notification for the post owner
		Notification.objects.create(
			recipient=post.author,
			actor=request.user,
			verb='liked',
			target=post
		)
		return Response(status=status.HTTP_201_CREATED)
	else:
		return Response({'detail': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
	# Use get_object_or_404 to handle fetching the post or raising a 404
	post = generics.get_object_or_404(Post, pk=pk)
	like = Like.objects.filter(user=request.user, post=post).first()

	if like:
		like.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	else:
		return Response({'detail': 'You haven\'t liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)
