#!/usr/bin/python3
"""This module defines test_cases for objects of class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Test cases for checking proper instantiation of
    rectangle objects"""

    def test_width_and_height_args(self):
        r1 = Rectangle(2, 10)
        r2 = Rectangle(5, 6)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_with_all_args(self):
        r1 = Rectangle(2, 10, 4, 20, 23)
        self.assertEqual(r1.id, 23)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 20)
