from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('marlon', email='marlonbaptista@hotmail.com')

    def test_get_user(self):
        """
        Simple test of add a user
        :return:
        """
        marlon = User.objects.get(username='marlon')
        self.assertEqual(marlon.username, 'marlon')
