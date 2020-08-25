from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import lists

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/lists/')  
        self.assertEqual(found.func, lists)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = lists(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>To-Do lists</title>', html)  
        self.assertTrue(html.endswith('</html>'))