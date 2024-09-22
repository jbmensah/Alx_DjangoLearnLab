from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField()

	class Meta:
		model = User  # Use the custom user model here
		fields = ('username', 'password', 'password2', 'email', 'bio', 'profile_picture')

	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError({"password": "Password fields didn't match."})
		return attrs

	def create(self, validated_data):
		# Use get_user_model().objects.create_user() to create the user
		user = User.objects.create_user(
			username=validated_data['username'],
			email=validated_data['email'],
			password=validated_data['password'],  # password is automatically hashed by create_user()
			bio=validated_data.get('bio', ''),
			profile_picture=validated_data.get('profile_picture', None)
		)

		# Create and return the token after the user is created
		token = Token.objects.create(user=user)

		return user, token  # Return both the user and the token

# Serializer for handling user profile view and update
class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User  # Use the custom user model here
		fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
		read_only_fields = ['username', 'email', 'followers']
