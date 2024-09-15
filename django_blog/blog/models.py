from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager



class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	published_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = TaggableManager()

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.pk})  # Adjust 'post-detail' to match your URL pattern name


	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'Comment by {self.author.username} on {self.post.title}'

	# def approve(self):
	# 	self.approved_comment = True
	# 	self.save()

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.post.pk})