#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.prime_game import is_winner


class TestPrimeGame(unittest.TestCase):
    def test_maria_wins(self):
        self.assertEqual(is_winner(3, [4, 5, 1]), 'Ben')

    def test_tie(self):
        self.assertIsNone(is_winner(2, [1, 2]))


if __name__ == '__main__':
    unittest.main()
