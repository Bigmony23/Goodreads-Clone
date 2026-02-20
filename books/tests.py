from django.contrib.auth import get_user
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from books.models import Book


class BooksTestCase(TestCase):
    def test_no_books(self):
        response=self.client.get(reverse('book-list'))

        self.assertContains(response, 'No books found.')

    def test_books_list(self):
        book1=Book.objects.create(title='Book1', description='Description1', isbn='1234' )
        book2=Book.objects.create(title='Book2', description='Description2', isbn='12345' )
        book3=Book.objects.create(title='Book3', description='Description3', isbn='123456' )

        response=self.client.get(reverse('book-list'))


        for book in [book1, book2]:
            self.assertContains(response, book.title)

        response=self.client.get(reverse('book-list')+'?page=2')
        self.assertContains(response, book3.title)

    def test_books_detail(self):
        book=Book.objects.create(title='Book1', description='Description1', isbn='1234' )

        response=self.client.get(reverse('book-detail', kwargs={'id':book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

# Create your tests here.
