import unittest
from quickbite.menu import search

class MenuTests(unittest.TestCase):
    def test_search_finds_item(self):
        self.assertEqual(search("biryani")[0]["id"], 2)
    def test_search_no_match(self):
        self.assertEqual(search("sushi"), [])
