from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publication_year')	# Displays the listed fields
	search_fields = ('title', 'author')	# Search Parameters
	list_filter = ('publication_year')	# Filter for publication year

# Register the Book model with the Django admin
admin.site.register(Book, BookAdmin)
