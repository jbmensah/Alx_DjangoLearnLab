## Import the Book class from the models module
from bookshelf.models import Book 

## Create a new Book instance with the specified title, author and publication year
q = Book(title = "1984", author = "George Orwell", publication_year = 1949)

## Save the Book Object to the database
q.save()

## Print the saved object to confirm the creation
print(q) # Expected Output: <Book: 1984>