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
        test_list = [-1, 23, -54, 8]
        self.assertAlmostEqual(max_integer(test_list), 23)
        
    def test_value(self):
        """Test if function max_integer raises a TypeError
        when necessary"""

        test_list = [1, 2, 3, 4]
        self.assertRaises(TypeError, max_integer, "string")
