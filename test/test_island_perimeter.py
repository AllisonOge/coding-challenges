#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.island_perimeter import island_perimeter


class TestIslandPerimeter(unittest.TestCase):
    def test_single_island(self):
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
        ]
        self.assertEqual(island_perimeter(grid), 16)


if __name__ == '__main__':
    unittest.main()
