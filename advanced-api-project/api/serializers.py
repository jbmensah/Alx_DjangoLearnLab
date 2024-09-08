from rest_framework import serializers
from .models import Book, Author

# Serializes the Book model, including custom validation for publication year
class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'

	# Custom validation for publication year
	def validate_publication_year(self, value):
		from datetime import datetime
		current_year = datetime.now().year
		if value > current_year:
			raise serializers.ValidationError("Publication year cannot be in the future.")
		return value


# Serializes the Author model, including a nested BookSerializer for related books
class AuthorSerializer(serializers.ModelSerializer):
	books = BookSerializer(many=True, read_only=True)

	class Meta:
		model = Author
		fields = ['name', 'books']