## Import the Book class from the models module
from bookshelf.models import Book 

## Filter books with a title starting with "Nineteen"
books_to_delete = Book.objects.filter(title__startswith="Nineteen")

## Check if any books were found and delete them
if books_to_delete.exists():
	for book in books_to_delete:
		book.delete()
		print(f"Deleted: Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
	print("All books with title starting with 'Nineteen' deleted successfully.")
else:
	print("No books were found with the title starting with 'Nineteen'.")

## Retrieve and display remaining Book instances
remaining_books = Book.objects.all()

if remaining_books.exists():
	for book in remaining_books:
		print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
else:
	print("No books found. All books deleted.")
