#!/usr/bin/python3
"""Unittests for max_integer function.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_values(self):
        self.assertEqual(max_integer([-5, -2, -10]), -2)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_duplicates(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)


if __name__ == "__main__":
    unittest.main()
