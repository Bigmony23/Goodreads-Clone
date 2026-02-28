from django.test import TestCase
from django.urls import reverse

from books.models import Book, Book_Review
from users.models import CustomUser


class HomePageTest(TestCase):
    def test_paginated_list(self):
        book=Book.objects.create(title='Book 1', description='Book 1',isbn='1241414')
        user = CustomUser.objects.create_user(
            username='jakhongir',
            first_name='Jakhongir',
            last_name="Rakhmonov",
            email='test@gmail.com'

        )
        user.set_password("somepass")
        user.save()
        self.client.login(username='jakhongir', password='somepass')
        review1=Book_Review.objects.create(book=book,user=user,stars_given=3,comment='Very good book')
        review2=Book_Review.objects.create(book=book,user=user,stars_given=4,comment='Good book')
        review3=Book_Review.objects.create(book=book,user=user,stars_given=5,comment='Nice book')
        response=self.client.get(reverse("home_page")+"?page_size=2")
        self.assertContains(response,review3.comment)
        self.assertContains(response,review2.comment)








