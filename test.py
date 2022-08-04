from main import app
from gbooks import get_books
from gnews import get_articles
import unittest
import sys

sys.path.append('../SEO-Final-Project')


class WebsiteTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_activities_page(self):
        response = self.app.get('/activities', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_history_page(self):
        response = self.app.get('/history', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_news_page(self):
        response = self.app.get('/news', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_resources_page(self):
        response = self.app.get('/resources', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class APITests(unittest.TestCase):

    # tests if get_books output is a list of 3 items
    def test_get_books(self):
        self.assertEqual(type(get_books()), type([]))
        self.assertEqual(len(get_books()), 3)

    # tests if get_articles output is a list of 3 items
    def test_get_articles(self):
        self.assertEqual(type(get_articles()), type([]))
        self.assertEqual(len(get_articles()), 3)


if __name__ == "__main__":
    unittest.main()
