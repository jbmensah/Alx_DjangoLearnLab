from django.db import models

# Author model represents the book's author with a name field
class Author(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

# Book model represents a book, related to an author
class Book(models.Model):
	title = models.CharField(max_length=200)
	publication_year = models.IntegerField()
	author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

	def __str__(self):
		return self.title
