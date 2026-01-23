#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer function"""

    def test_ordered_list(self):
        """Test a list with ordered integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list with unordered integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test list where max is the first element"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_max_at_end(self):
        """Test list where max is the last element"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """Test a list with mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 0, 1, 2]), 2)

    def test_duplicates(self):
        """Test a list with duplicate max values"""
        self.assertEqual(max_integer([1, 2, 2, 2, 1]), 2)

    def test_floats(self):
        """Test a list with floats (should work if integers)"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    if __name__ == '__main__':
        unittest.main()
