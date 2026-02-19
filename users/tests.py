from django.contrib.auth import get_user
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser


class RegistrationTestCase(TestCase):
    # def setUp(self):
    #     User.objects.create_user(
    #         username='jakhongir',
    #         first_name='Jakhongir',
    #         last_name="Rakhmonov",
    #         email='test@gmail.com',
    #         password="somepassword",
    #     )
    def test_user_account_is_created(self):
        self.client.post(reverse("register"), data={"username":"jakhongir",
                                                  "first_name":"Jakhongir",
                                                  "last_name":"Rakhmonov",
                                                  "email":"test@gmail.com",
                                                  "password":"somepassword",})
        user=CustomUser.objects.get(username="jakhongir")
        self.assertEqual(user.username,"jakhongir")
        self.assertEqual(user.first_name,"Jakhongir")
        self.assertEqual(user.last_name,"Rakhmonov")
        self.assertEqual(user.email,"test@gmail.com")
        self.assertNotEqual(user.password,"somepassword")
        self.assertTrue(user.check_password("somepassword"))

    def test_required_fields(self):
        response=self.client.post(reverse("register"), data={"first_name":"Jakhongir",
                                                    "email":"test@gmail.com",})
        user_count=CustomUser.objects.count()
        self.assertEqual(user_count, 0)
        form=response.context["create_form"]
        self.assertFormError(form,"username","This field is required.")
        self.assertFormError(form,"password","This field is required.")
    def test_invalid_email(self):
        response=self.client.post(reverse("register"), data={"username": "jakhongir",
                                                    "first_name": "Jakhongir",
                                                    "last_name": "Rakhmonov",
                                                    "email": "invalid-email",
                                                    "password": "somepassword", })
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)
        form=response.context["create_form"]
        self.assertFormError(form,"email","Enter a valid email address.")

    def test_unique_username(self):
        response = self.client.post(reverse("register"), data={"username": "jakhongir",
                                                               "first_name": "Jakhongir",
                                                               "last_name": "Rakhmonov",
                                                               "email": "test@gmail.com",
                                                               "password": "somepassword", })
        response2 = self.client.post(reverse("register"), data={"username": "jakhongir",
                                                               "first_name": "Jakhongir",
                                                               "last_name": "Rakhmonov",
                                                               "email": "test@gmail.com",
                                                               "password": "somepassword", })
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)
        form = response2.context["create_form"]
        self.assertFormError(form,"username","A user with that username already exists.")


class LoginTestCase(TestCase):
    def setUp(self):
        #DRY
        self.db_user = CustomUser.objects.create(username="jakhongir", first_name="Jakhongir")
        self.db_user.set_password("somepassword")
        self.db_user.save()

    def test_user_succesfull_login(self):


        self.client.post(reverse("login"), data={"username":"jakhongir",'password':'somepassword'})
        user=get_user(self.client)
        self.assertTrue(user.is_authenticated)
    def test_wrong_username_login(self):


        self.client.post(reverse("login"), data={"username": "wrong_username", 'password': 'somepassword'})
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
    def test_wrong_password(self):

        self.client.post(reverse("login"), data={"username": "wrong_username", 'password': 'somepass'})
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
    def testlogout(self):


        self.client.login(username= "jakhongir", password='somepassword')
        self.client.get(reverse("logout"))
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)



class ProfileTestCase(TestCase):
    def test_logged_in_user(self):
        response=self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,f"{reverse('login')}?next={reverse('profile')}")

    def test_profile_details(self):
        user=CustomUser.objects.create_user(
            username='jakhongir',
            first_name='Jakhongir',
            last_name="Rakhmonov",
            email='test@gmail.com'

        )
        user.set_password("somepass")
        user.save()
        # self.client.post(
        #     reverse("login"),
        #     data={"username": "jakhongir",
        #           'password': 'somepass'})

        self.client.login(username='jakhongir', password='somepass')

        response=self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response,user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_update_profile(self):
        user = CustomUser.objects.create_user(
            username='jakhongir',
            first_name='Jakhongir',
            last_name="Rakhmonov",
            email='test@gmail.com'

        )
        user.set_password("somepass")
        user.save()
        self.client.login(username='jakhongir', password='somepass')
        response=self.client.post(
            reverse("profile_edit"),
            data={
                'username':'jakhongir',
                'first_name':'Jakhongir',
                'last_name':'Doe',
                'email':'test1@gmail.com'
            }

        )
        user.refresh_from_db()
        # user=User.objects.get(pk=user.pk)
        self.assertEqual(user.last_name,"Doe")
        self.assertEqual(user.email,"test1@gmail.com")
        self.assertEqual(response.url, reverse("profile"))







# Create your tests here.
