#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.nqueens import solve_n_queens


class TestNQueens(unittest.TestCase):
    def test_n4_solution_count(self):
        self.assertEqual(len(solve_n_queens(4)), 2)

    def test_too_small(self):
        self.assertEqual(solve_n_queens(3), [])


if __name__ == '__main__':
    unittest.main()
