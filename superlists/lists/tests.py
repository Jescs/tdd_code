from django.urls import resolve
from django.test import TestCase
# from list.views import home_page
from lists.views import home_page  # git bash 下运行manage.py 没有superlists文件夹，所以只能直接import lists


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
