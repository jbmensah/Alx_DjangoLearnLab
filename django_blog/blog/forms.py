from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from taggit.forms import TagWidget


class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")


	def save(self, commit=True):
		user = super().save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'tags']
		widgets = {
			'tags': TagWidget(attrs={'placeholder': 'Enter tags...'}),
		}
		labels = {
			'title': 'Title',
			'content': 'Content',
		}


from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']
		widgets = {
			'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment...'}),
		}
		labels = {
			'content': 'Comment',
		}