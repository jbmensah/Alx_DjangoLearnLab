from .views import BookList
from django.urls import path

urlpatterns = [
	path("api/books/", BookList.as_view(), name="book_list"),
]