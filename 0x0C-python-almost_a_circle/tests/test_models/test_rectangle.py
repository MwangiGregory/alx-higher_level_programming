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


class TestRectangle_width(unittest.TestCase):
    """Test validation of width setters of Rectangle objects"""
    def test_str_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("2", 3)

    def test_list_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle([2, 3, 4], 3)

    def test_float_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(3.435, 6)

    def test_zero_width(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 5)

    def test_negative_width(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-12, 7)


class TestRectangle_height(unittest.TestCase):
    """Tests if validation of height setters for Rectangle objects works"""
    def test_str_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, "hello")

    def test_tuple_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, (9, 8, 7))

    def test_zero_height(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(2, 0)

    def test_negative_height(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(2, 0)


class TestRectangle_x(unittest.TestCase):
    """Tests if validation of x setters for Rectangle objects works"""
    def test_str_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(2, 3, x="5")

    def test_tuple_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(2, 3, x=(8, 7))

    def test_negative_x(self):
        with self.assertRaises(ValueError, msg="x must be > 0"):
            Rectangle(2, 0, x=-9)

    def test_zero_x(self):
        r1 = Rectangle(2, 3, x=0)
        self.assertEqual(r1.x, 0)


class TestRectangle_y(unittest.TestCase):
    """Tests if validation of y setters for Rectangle objects works"""
    def test_str_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(2, 3, y="hello")

    def test_tuple_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(2, 6, y=(9, 8, 7))

    def test_negative_y(self):
        with self.assertRaises(ValueError, msg="y must be > 0"):
            Rectangle(2, 0, y=-28)

    def test_zero_y(self):
        r1 = Rectangle(2, 3, y=0)
        self.assertEqual(r1.y, 0)
