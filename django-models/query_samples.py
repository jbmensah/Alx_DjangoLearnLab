from relationship_app.models import Author, Book, Library, Librarian

# Create Authors
jk_rowling = Author.objects.create(name="J.K. Rowling")
george_rr_martin = Author.objects.create(name="George R.R. Martin")
james_clear = Author.objects.create(name="James Clear")

# Create Books by J.K. Rowling
book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=jk_rowling)
book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=jk_rowling)

# Create Books by George R.R. Martin
book3 = Book.objects.create(title="A Game of Thrones", author=george_rr_martin)
book4 = Book.objects.create(title="A Clash of Kings", author=george_rr_martin)

# Create Books by James Clear
book5 = Book.objects.create(title="Atomic Habits", author=james_clear)

# Create a Library
accra_library = Library.objects.create(name="Accra Central Library")

# Add books to the library
accra_library.book.add(book1, book2, book3, book4, book5)

# Create a Librarian for the Library
librarian = Librarian.objects.create(name="John Doe", library=accra_library)

# Query books by J.K. Rowling
print("Books by J.K. Rowling:")
author = Author.objects.get(name="J.K. Rowling")
books = Book.objects.filter(author=author)
for book in books:
	print(book.title)

# List all books in Accra Central Library
print("\nBooks in Accra Central Library:")
library = Library.objects.get(name="Accra Central Library")
books = library.book.all()  # Use `.all()` to retrieve all books
for book in books:
	print(book.title)
	
# Retrieve the librarian for Accra Central Library
print("\nLibrarian for Accra Central Library:")
library = Library.objects.get(name="Accra Central Library")
librarian = Librarian.objects.get(library=library)
print(librarian.name)
