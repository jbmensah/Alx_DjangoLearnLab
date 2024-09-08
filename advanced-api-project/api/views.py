from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# ListView to retrieve all books
class BookListView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['title', 'author__name', 'publication_year']
	search_fields = ['title', 'author__name']
	ordering_fields = ['title', 'publication_year']
	ordering = ['title']

# DetailView to retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

# CreateView to add a new book
class BookCreateView(generics.CreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	# Add permission to allow only authenticated users to create books
	permission_classes = (IsAuthenticatedOrReadOnly,)

# UpdateView to modify an existing book
class BookUpdateView(generics.UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	# Add permission to allow only authenticated users to update books
	permission_classes = (IsAuthenticatedOrReadOnly,)

# DeleteView to remove a book
class BookDeleteView(generics.DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	# Add permission to allow only authenticated users to delete books
	permission_classes = (IsAuthenticatedOrReadOnly,)
