#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test for max_integer function"""

    def test_positive_integers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with a list of mixed positive and negative integers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_single_element(self):
        """Test with a list of a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_identical_elements(self):
        """Test with a list of identical elements"""
        self.assertEqual(max_integer([5, 5, 5]), 5)
