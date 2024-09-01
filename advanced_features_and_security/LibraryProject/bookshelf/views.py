from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from .models import Book

# View for listing books - anyone logged in can view
@login_required
@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
	books = Book.objects.all()
	return render(request, 'books/book_list.html', {'books': books})

# View for adding a new book - only users with can_create permission
@login_required
@permission_required('app_name.can_create', raise_exception=True)
def book_create(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		author = request.POST.get('author')
		publication_year = request.POST.get('publication_year')
		Book.objects.create(title=title, author=author, publication_year=publication_year)
		return redirect('book_list')
	return render(request, 'books/book_form.html')

# View for editing an existing book - only users with can_edit permission
@login_required
@permission_required('app_name.can_edit', raise_exception=True)
def book_edit(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		book.title = request.POST.get('title')
		book.author = request.POST.get('author')
		book.publication_year = request.POST.get('publication_year')
		book.save()
		return redirect('book_list')
	return render(request, 'books/book_form.html', {'book': book})

# View for deleting a book - only users with can_delete permission
@login_required
@permission_required('app_name.can_delete', raise_exception=True)
def book_delete(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		book.delete()
		return redirect('book_list')
	return render(request, 'books/book_confirm_delete.html', {'book': book})
