from django.contrib.auth import get_user
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from books.models import Book
from users.models import CustomUser


class BooksTestCase(TestCase):
    def test_no_books(self):
        response=self.client.get(reverse('book-list'))

        self.assertContains(response, 'No books found.')

    def test_books_list(self):
        book1=Book.objects.create(title='Book1', description='Description1', isbn='1234' )
        book2=Book.objects.create(title='Book2', description='Description2', isbn='12345' )
        book3=Book.objects.create(title='Book3', description='Description3', isbn='123456' )

        response=self.client.get(reverse('book-list')+'?page_size=2')


        for book in [book1, book2]:
            self.assertContains(response, book.title)
        self.assertNotContains(response, book3.title)

        response=self.client.get(reverse('book-list')+'?page=2&page_size=2')
        self.assertContains(response, book3.title)

    def test_books_detail(self):
        book=Book.objects.create(title='Book1', description='Description1', isbn='1234' )

        response=self.client.get(reverse('book-detail', kwargs={'id':book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

    def test_search_books(self):
        book1 = Book.objects.create(title='Sport', description='Description1', isbn='1234')
        book2 = Book.objects.create(title='Guide', description='Description2', isbn='12345')
        book3 = Book.objects.create(title='Shu Doe', description='Description3', isbn='123456')

        response=self.client.get(reverse('book-list')+'?q=sport')
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse('book-list') + '?q=guide')
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse('book-list') + '?q=shu')
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        # response=self.client.get(reverse('book-list')+'?q=guide')
        # self.assertContains(response, book2.title)
        # response=self.client.get(reverse('book-list')+'?q=shu')
        # self.assertContains(response, book3.title)

class BookReviewTestCase(TestCase):
    def test_no_books(self):
        book = Book.objects.create(title='Sport', description='Description1', isbn='1234')
        user = CustomUser.objects.create_user(
            username='jakhongir',
            first_name='Jakhongir',
            last_name="Rakhmonov",
            email='test@gmail.com'

        )
        user.set_password("somepass")
        user.save()
        self.client.login(username='jakhongir', password='somepass')

        self.client.post(reverse('addreviews', kwargs={'id':book.id}),data={
            'stars_given':3,
            "comment":"Nice book very useful information",
        })
        book_reviews=book.book_review_set.all()

        self.assertEqual(book_reviews.count(),1)
        self.assertEqual(book_reviews.first().stars_given,3)
        self.assertEqual(book_reviews.first().comment,"Nice book very useful information")
        self.assertEqual(book_reviews[0].user,user)
        self.assertEqual(book_reviews[0].book,book)


# Create your tests here.
