from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from website.views import home_page


class HomePageTests(TestCase):
    def test_home_page_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Barend ICT</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
