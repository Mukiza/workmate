from django.test import TestCase
from django.test.client import Client


class HomeViewTest(TestCase):

    def test_gets_home_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(200, response.status_code)
        templates = [template.name for template in response.templates]
        self.assertIn('home/index.html', templates)
