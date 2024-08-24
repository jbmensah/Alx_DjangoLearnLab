from relationship_app.models import Author, Book, Library, Librarian

# Add Author objects
au = Author.objects.create(name="George R.R. Martin")
au.save()
au1 = Author.objects.create(name="James Clear")
au1.save()

# Add Book objects
bk = Book.objects.create(title="A Game of Thrones", author=george_rr_martin)
bk1 = Book.objects.create(title="A Clash of Kings", author=george_rr_martin)
bk2 = Book.objects.create(title="Atomic Habits", author=james_clear)

# Get books by one author
print("Books by George R.R. Martin:")
au_martin = Author.objects.get(name="George R.R. Martin")
bk_martin = Book.objects.filter(author=george_rr_martin)
for books in bk_martin:
	print(books.title)

# List all books
print("\nAll books:")
all_books = Book.objects.all()
for books in all_books:
	print(books.title)

# Create Library Instance
lib = Library.objects.create(name='Accra Central Library')
lib.save()

# Add books to Library
lib.books.add(game_of_thrones, clash_of_kings, atomic_habits)

# List all books in Library
print("\nBooks in Accra Central Library:")
lib.books.all()
Library.objects.get(name='Accra Central Library'), books.all()

# for book in books_in_library:
#     print(book.title)

# Add Librarian
libr = Librarian.objects.create(name='Akua Sekyiwaa', library=accra_library)
libr.save()

# Retrieve a Librarian for a library
print("\nLibrarian for Accra Central Library:")
libr = Librarian.objects.get(library=accra_library)
print(librarian.name)
