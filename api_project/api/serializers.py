from rest_framework import serializers
from api.models import Book

class BookSerializer(serializers.ModelSerializer):
	# Meta class is used to specify additional options or configuration
	class Meta:
		# Specifies that the serializer should be based on the Book model
		model = Book
		# Specifies that all fields from the Book model should be included in the serialized output
		fields = '__all__'