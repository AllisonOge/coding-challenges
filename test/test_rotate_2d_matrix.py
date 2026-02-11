#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.rotate_2d_matrix import rotate_2d_matrix


class TestRotate2DMatrix(unittest.TestCase):
    def test_rotate_3x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate_2d_matrix(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])


if __name__ == '__main__':
    unittest.main()
