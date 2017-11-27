from unittest import TestCase
from utils import parse_home_dir

class TestParse_home_dir(TestCase):
    def test_parse_home_dir(self):
        self.assertEqual(parse_home_dir('log', 'error.log'), r'C:\Users\Admin\log\error.log', "Not expected result")
