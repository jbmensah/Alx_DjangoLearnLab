from django.db import models

# Showcase complex relationships between entities using ForeignKey, ManyToMany, and OneToOne fields.

class Author(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
	
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Library(models.Model):
	name = models.CharField(max_length=200)
	book = models.ManyToManyField(Book)

	def __str__(self):
		return self.name

class Librarian(models.Model):
	name = models.CharField(max_length=200)
	library = models.OneToOneField(Library, on_delete=models.CASCADE)

	def __str__(self):
		return self.name