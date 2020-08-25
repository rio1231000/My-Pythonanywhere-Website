from django.urls import resolve
from django.test import TestCase
from lists.views import lists  

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/lists/')  
        self.assertEqual(found.func, lists)