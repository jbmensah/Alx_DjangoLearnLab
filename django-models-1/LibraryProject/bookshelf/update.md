## Import the Book class from the models module
from bookshelf.models import Book

## Try to handle exceptions when trying to retrieve the specific Book instance with the title "1984"
try:
	book = Book.objects.get(title = "1984")

## Update the title of the Book instance
	book.title = "Nineteen Eighty-Four"

## Save the changes to the database
	book.save()

## Print the updated object to confirm the title change
	print(book) # Expected Output: Nineteen Eighty-Four

except Book.DoesNotExist:
## Handle the case where book with specified title does not exist
	print("Error: No book found with title '" + book.title)

except Book.MultipleObjectsReturned:
## Handle the case where multiple books with specified title found
	print("Error: Multiple books found with title '" + book.title)