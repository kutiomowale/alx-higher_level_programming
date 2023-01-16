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
        self.assertEqual(max_integer([0, -2, -5]), 0)
        self.assertEqual(max_integer([0, '5', -5]), 0)
