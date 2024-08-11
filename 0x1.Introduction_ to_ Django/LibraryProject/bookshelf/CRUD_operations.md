# CRUD Operations in Django
This document details the Create, Retrieve, Update, and Delete operations performed on the Book model using the Django interactive shell.

## 1. Create
### Command:
<
## Import the Book class from the models module
from bookshelf.models import Book 

## Create a new Book instance with the specified title, author, and publication year
q = Book(title="1984", author="George Orwell", publication_year=1949)

## Save the Book object to the database
q.save()

## Print the saved object to confirm the creation
print(q)  # Expected Output: <Book: 1984>
>

### Expected Output:
<Book: 1984>

## 2. Retrieve
### Command:
<
## Import the Book class from the models module
from bookshelf.models import Book

## Retrieve all Book instances from the database
books = Book.objects.all()

## Iterate through the QuerySet and display the attributes of each Book instance
for book in books:
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
>

### Expected Output:
<Title: 1984, Author: George Orwell, Year: 1949>

## 3. Update
### Command:
<
## Import the Book class from the models module
from bookshelf.models import Book

## Try to handle exceptions when trying to retrieve the specific Book instance with the title "1984"
try:
    book = Book.objects.get(title="1984")

    ## Update the title of the Book instance
    book.title = "Nineteen Eighty-Four"

    ## Save the changes to the database
    book.save()

    ## Print the updated object to confirm the title change
    print(book)  # Expected Output: <Book: Nineteen Eighty-Four>

except Book.DoesNotExist:
    ## Handle the case where no book with the specified title exists
    print("Error: No book found with the title '1984'.")

except Book.MultipleObjectsReturned:
    ## Handle the case where multiple books with the specified title are found
    print("Error: Multiple books found with the title '1984'.")
>

### Expected Output:
<Book: Nineteen Eighty-Four>

## 4. Delete
### Command:
<
## Import the Book class from the models module
from bookshelf.models import Book 

## Filter and delete the specific book title
book_to_delete = Book.objects.filter(title__startswith="Nineteen")

## Check if any books were found and delete them
if book_to_delete.exists():
    book_to_delete.delete()
    print("Book(s) with title starting with 'Nineteen' deleted successfully.")
else:
    print("No books found with the title starting with 'Nineteen'.")

## Retrieve and display remaining Book instances
books = Book.objects.all()

## Display the remaining books, if any
if books.exists():
    for book in books:
        print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
else:
    print("No books found. All books have been deleted.")
>

### Expected Output:
<Book(s) with title starting with 'Nineteen' deleted successfully.
No books found. All books have been deleted.
>