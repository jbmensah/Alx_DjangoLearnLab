from django.urls import path
from .views import RegisterView, UserProfileView, follow_user, unfollow_user
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
	path('profile/', UserProfileView.as_view(), name='profile'),
	path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]