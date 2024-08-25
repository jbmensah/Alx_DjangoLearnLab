from django.urls import path
from .views import list_books, LibraryDetailView
from .views import CustomLoginView, CustomLogoutView, register
from . import views
from .views import admin_view, librarian_view, member_view
from .views import add_book_view, edit_book_view, delete_book_view

urlpatterns = [
	path('books/', list_books, name='list_books'),
	path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
	path('login/', CustomLoginView.as_view(template_name='login.html/'), name='login'),
	path('logout/', CustomLogoutView.as_view(template_name='logout.html/'), name='logout'),
	path('register/', views.register, name='register'),
	path('admin/', admin_view, name='admin_view'),
	path('librarian_view/', librarian_view, name='librarian_view'),
	path('member_view/', member_view, name='member_view'),
	path('books/add/', add_book_view, name='add_book'),
	path('books/<int:pk>/edit/', edit_book_view, name='edit_book'),
	path('books/<int:pk>/delete/', delete_book_view, name='delete_book'),
]