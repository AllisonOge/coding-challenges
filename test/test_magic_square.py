#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/05/07 08: 26
# @Author : AllisonOge

import unittest
from ..magic_square import forming_magic_square

class TestMagicSquare(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(forming_magic_square([]), float("inf"))

    def test_costly_matrix(self):
        self.assertEqual(forming_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 20)
    
    def test_cheap_matrix(self):
        self.assertEqual(forming_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 5]]), 1)

if __name__ == "__main__":
    unittest.main()