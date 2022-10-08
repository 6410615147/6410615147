from django.test import TestCase, Client
from django.urls import reverse


class UsersViewTestCase(TestCase):

    def test_index_view_status_code(self):
        c = Client()
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 302)

    def test_valid_login_page(self):
        c = Client()
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_valid_registered_page(self):
        c = Client()
        response = c.get(reverse('users:registered'))
        self.assertEqual(response.status_code, 200)