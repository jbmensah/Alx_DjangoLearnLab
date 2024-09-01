from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
	path("api/", include(router.urls)),
	path('api/token/', obtain_auth_token, name='api_token_auth'),
]