from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token  # Import Token
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField()

	class Meta:
		model = CustomUser
		fields = ('username', 'password', 'password2', 'email', 'bio', 'profile_picture')
	
	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError({"password": "Password fields didn't match."})
		return attrs

	def create(self, validated_data):
		user = CustomUser.objects.create(
			username=validated_data['username'],
			email=validated_data['email'],
			bio=validated_data.get('bio', ''),
		)
		user.set_password(validated_data['password'])
		user.save()

		# Create and return token after the user is created
		token = Token.objects.create(user=user)  # Token generation

		return user, token  # Return the token along with the user

# Serializer for handling user profile view and update
class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
		read_only_fields = ['username', 'email', 'followers']
