from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
	try:
		author = Author.objects.get(name=author_name)
		books = Book.objects.filter(author=author)
		for book in books:
			print(f"Title: {book.title}, Author: {book.author.name}")
	except Author.DoesNotExist:
		print(f"Error: No author found with the name '{author_name}'.")

# List all books in a library
def list_books_in_library(library_name):
	try:
		library = Library.objects.get(name=library_name)
		books = library.book.all()
		for book in books:
			print(f"Title: {book.title}, Author: {book.author.name}")
	except Library.DoesNotExist:
		print(f"Error: No library found with the name '{library_name}'.")

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
	try:
		library = Library.objects.get(name=library_name)
		librarian = Librarian.objects.get(library=library)
		print(f"Librarian: {librarian.name}")
	except Library.DoesNotExist:
		print(f"Error: No library found with the name '{library_name}'.")
	except Librarian.DoesNotExist:
		print(f"Error: No librarian found for the library '{library_name}'.")