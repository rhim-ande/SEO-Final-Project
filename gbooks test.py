import unittest
from gbooks import get_books


# tests if get_books output is a list of 3 items
class TestBooks(unittest.TestCase):
    def test_get_books(self):
        self.assertEqual(type(get_books()), type([]))
        self.assertEqual(len(get_books()), 3)


if __name__ == '__main__':
    unittest.main()