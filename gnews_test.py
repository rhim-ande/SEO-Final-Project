import unittest
from gnews import get_articles


# tests if get_articles output is a list of 3 items
class TestNews(unittest.TestCase):
    def test_get_articles(self):
        self.assertEqual(type(get_articles()), type([]))
        self.assertEqual(len(get_articles()), 3)


if __name__ == '__main__':
    unittest.main()
