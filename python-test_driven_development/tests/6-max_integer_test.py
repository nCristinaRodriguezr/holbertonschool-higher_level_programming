#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list_with_integers(self):
        result = max_integer([10, 8, 1])
        self.assertEqual(result, 10)

    def test_empty_list(self):
        result = max_integer([])
        self.assertEqual(result, None)
    
    def test_None_list(self):
        result = max_integer([None])
        self.assertEqual(result, None)

    def test_negative_numbers(self):
        result = max_integer([-2, -50, -1])
        self.assertEqual(result, -1)

    def test_float_numbers(self):
        result = max_integer([10.5, 8.6, 15.11, 4.1])
        self.assertEqual(result, 15.11)
