#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.minimum_operations import min_operations


class TestMinimumOperations(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual(min_operations(1), 0)
        self.assertEqual(min_operations(4), 4)

    def test_prime_value(self):
        self.assertEqual(min_operations(13), 13)


if __name__ == '__main__':
    unittest.main()
