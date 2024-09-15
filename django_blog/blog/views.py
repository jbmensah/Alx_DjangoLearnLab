from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

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
	