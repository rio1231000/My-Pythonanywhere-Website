from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import lists
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/lists/')  
        self.assertEqual(found.func, lists)

{'''
    def test_home_page_returns_correct_html1(self):
        request = HttpRequest()
        response = lists(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)

    def test_home_page_returns_correct_html2(self):
        response = self.client.get('/lists/')

        html = response.content.decode('utf8')


        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

        self.assertTemplateUsed(response, 'wrong.html')
'''}

    def test_uses_home_template(self):
        response = self.client.get('/lists/')
        self.assertTemplateUsed(response, 'home.html')