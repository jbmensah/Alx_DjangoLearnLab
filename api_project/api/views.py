from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # Import the IsAuthenticated permission class
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]  # Apply the IsAuthenticated permission class
