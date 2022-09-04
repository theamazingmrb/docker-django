"""
Sample Test
"""
from django.test import SimpleTestCase

from app import calc


class CalTest(SimpleTestCase):
    """ Test"""
    def test_add_numbers(self):
        res = calc.add(6, 6)
        self.assertEqual(res, 12)
