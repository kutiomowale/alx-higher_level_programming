#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(10)
        b5 = Base()
        b6 = Base(-20)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 10)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, -20)
