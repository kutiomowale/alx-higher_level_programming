#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer function"""

    def test_results(self):
        """Test the results for certain input"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 1, 2]), 3)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([1, 3, -2]), 3)
        self.assertEqual(max_integer([-1, -3, -2]), -1)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([]), None)
