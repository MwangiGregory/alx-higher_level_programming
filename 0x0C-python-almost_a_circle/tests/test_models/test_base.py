"""This module contains the test cases for class Base"""
import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Unit test for checking proper instatiation of objects
    of type Base"""

    def test_no_arguments(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_arguments(self):
        b1 = Base(21)
        self.assertEqual(b1.id, 21)
        b2 = Base(42)
        self.assertEqual(b2.id, 42)

    def test_id_is_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
        
