#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_empty(self):
        self.assertIsNone(max_integer([]))
    def test_negative(self):
        self.assertEqual(max_integer([-5, -2, -9]), -2)
    def test_one(self):
        self.assertEqual(max_integer([7]), 7)
if __name__ == "__main__":
    unittest.main()
