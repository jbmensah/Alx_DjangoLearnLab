from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)

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
		return user
	
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['username', 'email', 'followers']
		