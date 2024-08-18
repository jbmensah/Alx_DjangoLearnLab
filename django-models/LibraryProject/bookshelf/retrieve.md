## Import the Book class from the models module
from bookshelf.models import Book

## Retrieve all Book instances from the database
books = Book.objects.get(title="1984")

## Iterate through the QuerySet and display the attributes of each Book instance
for book in books:
	print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

## Expected Output:
## Title: 1984, Author: George Orwell, Year: 1949
