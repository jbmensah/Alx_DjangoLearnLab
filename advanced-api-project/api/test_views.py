from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User

class BookTests(APITestCase):
	
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpass')
		self.author = Author.objects.create(name='J.K. Rowling')
		self.book = Book.objects.create(
			title='Harry Potter and the Philosopher\'s Stone',
			publication_year=1997,
			author=self.author
		)
		self.client.login(username='testuser', password='testpass')

	def test_create_book(self):
		url = reverse('book-list')  # Adjust if necessary
		data = {
			'title': 'New Book Title',
			'publication_year': 2024,
			'author': self.author.id
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Book.objects.count(), 2)
		self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book Title')

	def test_get_book(self):
		url = reverse('book-detail', args=[self.book.id])  # Adjust if necessary
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['title'], self.book.title)

	def test_update_book(self):
		url = reverse('book-detail', args=[self.book.id])  # Adjust if necessary
		data = {
			'title': 'Updated Title'
		}
		response = self.client.put(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.book.refresh_from_db()
		self.assertEqual(self.book.title, 'Updated Title')

	def test_delete_book(self):
		url = reverse('book-detail', args=[self.book.id])  # Adjust if necessary
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(Book.objects.count(), 0)

	def test_filter_books(self):
		url = reverse('book-list')  # Adjust if necessary
		response = self.client.get(url, {'title': 'Harry Potter'})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertGreater(len(response.data), 0)  # Ensure we get at least one book

	def test_search_books(self):
		url = reverse('book-list')  # Adjust if necessary
		response = self.client.get(url, {'search': 'Harry'})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertGreater(len(response.data), 0)

	def test_order_books(self):
		url = reverse('book-list')  # Adjust if necessary
		response = self.client.get(url, {'ordering': 'publication_year'})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		# Check if books are ordered correctly
		sorted_books = sorted(response.data, key=lambda x: x['publication_year'])
		self.assertEqual(response.data, sorted_books)

	def test_permissions(self):
		# Test with an unauthenticated user or a user with limited permissions
		self.client.logout()
		url = reverse('book-list')  # Adjust if necessary
		response = self.client.post(url, {'title': 'Unauthorized Book'}, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
