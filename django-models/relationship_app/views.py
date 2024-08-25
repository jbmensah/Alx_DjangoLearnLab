from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def list_books(request):
	books = Book.objects.all()
	return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
	model = Library
	template_name = 'relationship_app/library_detail.html'
	context_object_name = 'library'

class CustomLoginView(LoginView):
	template_name = 'login.html'

class CustomLogoutView(LogoutView):
	template_name = 'logout.html'

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'relationship_app/register.html', {'form': form})