#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""Unit test for Rectangle class"""


class TestRectangle(unittest.TestCase):
    """Unittest for Rectangle class"""

    def test_attributes(self):
        """Attribute tests"""
        b1 = Rectangle(5, 5)
        b2 = Rectangle(5, 5, 3)
        b3 = Rectangle(5, 5, 3, 4)
        b4 = Rectangle(5, 5, 3, 4, 10)
        b5 = Rectangle(5, 5)
        b6 = Rectangle(5, 5, 3, 4, -20)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 10)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, -20)

        self.assertEqual(b1.width, 5)
        self.assertEqual(b1.height, 5)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)
        self.assertEqual(b2.x, 3)
        self.assertEqual(b2.y, 0)

        with self.assertRaises(AttributeError):
            b1.area
