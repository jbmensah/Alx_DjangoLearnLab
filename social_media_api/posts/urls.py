from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, CommentViewSet, UserFeedView  # Import the UserFeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
	path('feed/', UserFeedView.as_view(), name='user_feed'),  # Add the feed route here
] + router.urls  # Combine with the router URLs
