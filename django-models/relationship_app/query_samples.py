from relationship_app.models import Author, Book, Library, Librarian
# Add Author to objects
author_name = Author.objects.create(name="George R.R Martin")
author_name1 = Author.objects.create(name="James Clear")
Author.objects.all()

# Add Book Objects
bk = Book.objects.create(title="A Game of Thrones", author=author_name)
bk1 = Book.objects.create(title="Atomic Habits", author=author_name1)
Book.objects.all()
bk2 = Book.objects.create(title="A Clash of Kings", author=author_name)
Book.objects.all()

# Get books by one author
print("Books by George R.R. Martin:")
author_name = Author.objects.get(name__startswith="George")
for books in author_name:
    print(books.title)
book_au = Book.objects.filter(author=author_name)
for books in book_au:
    print(books.title)

# List all books
print("\nAll books:")
all_bks = Book.objects.all()
for books in all_bks:
    print(books.title)

# Create a Library Instance
library_name = Library.objects.create(name="Accra Central Library")

# Add books to Library
library_name.book.add(bk, bk1, bk2)

# List all books in the Library using the desired structure
print("\nBooks in Accra Central Library:")
# library = Library.objects.get(name="Accra Central Library")
books_in_library = Library.objects.get(name=library_name).books.all()
for book in books_in_library:
    print(book.title)

# # Verify the books have been added
# lib_books = lib.book.all()
# for book in lib_books:
#     print(book.title)

# Add Librarian
librarian = Librarian.objects.create(name='Akua Sekyiwaa Afrifa', library=library_name)

# Retrieve a Librarian for a library
Librarian.objects.get(library=library_name)


import readline
for i in range(readline.get_current_history_length()):
    print(readline.get_history_item(i+1))