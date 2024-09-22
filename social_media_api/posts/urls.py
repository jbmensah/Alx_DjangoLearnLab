from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, CommentViewSet, UserFeedView, like_post, unlike_post  # Import the UserFeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
	path('feed/', UserFeedView.as_view(), name='user_feed'),  # Add the feed route here
	path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),
	
] + router.urls  # Combine with the router URLs
