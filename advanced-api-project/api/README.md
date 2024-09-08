# Book API
The Book API supports the following endpoints:

- `/books/` (GET): List all books
- `/books/<int:pk>/` (GET): Retrieve a single book by ID
- `/books/create/` (POST): Create a new book (authenticated users only)
- `/books/<int:pk>/update/` (PUT/PATCH): Update a book (authenticated users only)
- `/books/<int:pk>/delete/` (DELETE): Delete a book (authenticated users only)
