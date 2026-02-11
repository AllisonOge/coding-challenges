#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.pascal_triangle import pascal_triangle


class TestPascalTriangle(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(pascal_triangle(0), [])

    def test_five_rows(self):
        self.assertEqual(
            pascal_triangle(5),
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        )


if __name__ == '__main__':
    unittest.main()
