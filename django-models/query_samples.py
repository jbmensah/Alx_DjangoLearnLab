from relationship_app.models import Author, Book, Library, Librarian

# Add Author objects
george_rr_martin = Author.objects.create(name="George R.R. Martin")
george_rr_martin.save()
james_clear = Author.objects.create(name="James Clear")
james_clear.save()

# Add Book objects
game_of_thrones = Book.objects.create(title="A Game of Thrones", author=george_rr_martin)
clash_of_kings = Book.objects.create(title="A Clash of Kings", author=george_rr_martin)
atomic_habits = Book.objects.create(title="Atomic Habits", author=james_clear)

game_of_thrones.save()
clash_of_kings.save()
atomic_habits.save()

# Get books by one author
print("Books by George R.R. Martin:")
george_rr_martin = Author.objects.get(name="George R.R. Martin")
books_by_george = Book.objects.filter(author=george_rr_martin)
for books in books_by_george:
	print(books.title)

# List all books
print("\nAll books:")
all_books = Book.objects.all()
for books in all_books:
	print(books.title)

# Create Library Instance
accra_library = Library.objects.create(name='Accra Central Library')
accra_library.save()

# Add books to Library
accra_library.books.add(game_of_thrones, clash_of_kings, atomic_habits)

# List all books in Library
print("\nBooks in Accra Central Library:")
accra_library.books.all()
Library.objects.get(name='Accra Central Library'), books.all()

# for book in books_in_library:
#     print(book.title)

# Add Librarian
librarian = Librarian.objects.create(name='Akua Sekyiwaa', library=accra_library)
librarian.save()

# Retrieve a Librarian for a library
print("\nLibrarian for Accra Central Library:")
librarian = Librarian.objects.get(library=accra_library)
print(librarian.name)
