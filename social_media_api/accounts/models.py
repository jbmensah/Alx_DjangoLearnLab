from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	bio = models.TextField(blank=True, null=True)
	profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
	
	# Rename related_name for followers to avoid clashes
	followers = models.ManyToManyField(
		'self', 
		blank=True, 
		related_name='following_users',  # Changed this
		symmetrical=False
	)
	
	following = models.ManyToManyField(
		'self', 
		blank=True, 
		related_name='follower_users',  # Changed this
		symmetrical=False
	)

	def __str__(self):
		return self.username