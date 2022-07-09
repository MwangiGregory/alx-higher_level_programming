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

    def test_max_at_beginning(self):
        #Test when max value is at the beginning of the list
        start = [9, 8, 7, 6]
        self.assertEqual(max_integer(start), 9)

    def test_max_in_the_middle(self):
        #Test when max value is in the middle of the list
        middle = [1, 2, 7, 4, 5]
        self.assertEqual(max_integer(middle), 7)

    def test_with_neg_number(self):
        #Test when the list argument has negative values
        neg = [1, 2, -33, 4]
        self.assertEqual(max_integer(neg), 4)

    def test_only_neg_numbers(self):
        #Test when the list only has negative numbers
        neg = [-9, -8, -7, -1]
        self.assertEqual(max_integer(neg), -1)

    def test_one_element(self):
        #Test with only one element in the list
        one = [8]
        self.assertEqual(max_integer(one), 8)

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
