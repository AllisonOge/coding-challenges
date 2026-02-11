#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.making_change import make_change


class TestMakingChange(unittest.TestCase):
    def test_exact_change(self):
        self.assertEqual(make_change([1, 2, 25], 37), 7)

    def test_impossible_change(self):
        self.assertEqual(make_change([2, 4], 7), -1)


if __name__ == '__main__':
    unittest.main()
