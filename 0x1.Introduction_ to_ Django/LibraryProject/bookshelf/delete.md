## Import the Book class from the models module
from bookshelf.models import Book 

## Filter and delete specific book title
book_to_delete = Book.objects.filter(book.title__startswith="Nineteen")

## Check if any books were found and delete them
if book_to_delete.exists():
	book_to_delete.delete()
	print("Book(s) with title starting with 'Nineteen' deleted successfully.")
else:
	print("No books were found with title 'Nineteen'.")

## Display remaining book Instances
if books.exists():
	for book in books:
		print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
else:
	print("No books found. All books deleted.")
