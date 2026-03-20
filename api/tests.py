from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Book, Book_Review
from users.models import CustomUser


class BookReviewTestCase(APITestCase):
    def setUp(self):
        #DRY
        self.user = CustomUser.objects.create(username="jakhongir", first_name="Jakhongir")
        self.user.set_password("somepassword")
        self.user.save()
        self.client.login(username='jakhongir', password='somepassword')

    def test_book_review_detail(self):
        book = Book.objects.create(title='Sport', description='Description1', isbn='1234')
        br=Book_Review.objects.create(book=book, user=self.user,stars_given=5,comment='interesting')
        response=self.client.get(reverse('api:reviews-detail', kwargs={'id':br.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['comment'], "interesting")
        self.assertEqual(response.data['book']['id'], br.book.id)
        self.assertEqual(response.data['book']['description'], "Description1")
        self.assertEqual(response.data['book']['isbn'], "1234")
        self.assertEqual(response.data['book']['title'], "Sport")
        self.assertEqual(response.data['user']['id'], self.user.id)
        self.assertEqual(response.data['user']['username'], 'jakhongir')
        self.assertEqual(response.data['user']['first_name'], "Jakhongir")

    def test_delete_review(self):
        book = Book.objects.create(title='Sport', description='Description1', isbn='1234')
        br = Book_Review.objects.create(book=book, user=self.user, stars_given=5, comment='interesting')
        response=self.client.delete(reverse('api:reviews-detail', kwargs={'id':br.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book_Review.objects.filter(id=br.id).exists())
    def test_patch_review(self):
        book = Book.objects.create(title='Sport', description='Description1', isbn='1234')
        br = Book_Review.objects.create(book=book, user=self.user, stars_given=5, comment='interesting')
        response = self.client.patch(reverse('api:reviews-detail', kwargs={'id': br.id}) ,data={'stars_given':4})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['stars_given'], 4)
    def test_put_review(self):
        book = Book.objects.create(title='Sport', description='Description1', isbn='1234')
        br = Book_Review.objects.create(book=book, user=self.user, stars_given=5, comment='interesting')
        response=self.client.put(reverse('api:reviews-detail', kwargs={'id':br.id}) ,data={'stars_given':5,'comment':'interesting','user_id':self.user.id,'book_id':book.id})
        br.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['comment'], "interesting")
    def test_create_review(self):
        book = Book.objects.create(title='Sport', description='Description1', isbn='1234')
        data={
            'stars_given':3,
            'comment':'interesting',
            'user_id':self.user.id,
            'book_id':book.id
        }
        response=self.client.post(reverse('api:reviews-list'), data=data)
        br=Book_Review.objects.get(book=book)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['stars_given'], 3)
        self.assertEqual(response.data['comment'], "interesting")







    def test_book_review_list(self):
        user2= CustomUser.objects.create(username="someuser", first_name="SomeBody")
        book = Book.objects.create(title='Sport', description='Description1', isbn='1234')
        br1 = Book_Review.objects.create(book=book, user=self.user, stars_given=5, comment='interesting')
        br2 = Book_Review.objects.create(book=book, user=user2, stars_given=3, comment='bad book')

        response=self.client.get(reverse('api:reviews-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results=response.data['results']

        self.assertEqual(response.data['count'], 2)
        self.assertIn('next',response.data)
        self.assertIn('previous', response.data)
        # Don't assume position — look up by actual ID
        br1_data = next(r for r in results if r['id'] == br1.id)
        br2_data = next(r for r in results if r['id'] == br2.id)
        self.assertEqual(br2_data['stars_given'], 3)
        self.assertEqual(br1_data['stars_given'], 5)
        self.assertEqual(br2_data['comment'], br2.comment)
        self.assertEqual(br1_data['comment'], br1.comment)







# Create your tests here.
