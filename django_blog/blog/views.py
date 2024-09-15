from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def posts(request):
	# Your logic here
	return render(request, 'posts.html')

def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('login')
	else:
		form = CustomUserCreationForm()
	return render(request, 'registration/register.html', {'form': form})

def user_login(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('home')
	else:
		form = AuthenticationForm()
	return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
	logout(request)
	return redirect('home')

@login_required
def profile(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(data = request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = CustomUserCreationForm(instance=request.user)
	return render(request, 'registration/profile.html', {'form': form})



class PostListView(ListView):
	model = Post
	template_name = 'blog/posts_list.html'
	context_object_name = 'posts'


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'blog/post_form.html'
	form_class = PostForm
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	template_name = 'blog/post_form.html'
	form_class = PostForm

	def get_queryset(self):
		return Post.objects.filter(author=self.request.user)
	
	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author  # Ensures only the author can edit

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/post_confirm_delete.html'
	success_url = reverse_lazy('post_list')

	def get_queryset(self):
		return Post.objects.filter(author=self.request.user)

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author  # Ensures only the author can delete

class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'blog/add_comment.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.post = get_object_or_404(Post, id=self.kwargs['pk'])
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.post.get_absolute_url()

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Comment
	form_class = CommentForm
	template_name = 'blog/edit_comment.html'

	def test_func(self):
		comment = self.get_object()
		return self.request.user == comment.author

	def get_success_url(self):
		return self.object.post.get_absolute_url()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	template_name = 'blog/delete_comment.html'

	def test_func(self):
		comment = self.get_object()
		return self.request.user == comment.author

	def get_success_url(self):
		return self.object.post.get_absolute_url()