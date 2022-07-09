#!/usr/bin/python3
"""
Unittesting module for function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittest for function max_integer"""

    def test_max_integer(self):
        #Test case using list of integers
        test_list = [1, 2, 3, 4]
        self.assertAlmostEqual(max_integer(test_list), 4)

    def test_empty_list(self):
        #Test correct output for an empty list
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floats(self):
        #Test a list of float
        floats = [1.33, -2.45, 9.78, 0.0001]
        self.assertEqual(max_integer(floats), 9.78)

    def test_string(self):
        #Test a list of characters
        chars = "gregory"
        self.assertEqual(max_integer(chars), 'y')
