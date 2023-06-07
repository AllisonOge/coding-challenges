#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/05/07 07:54
# @Author : AllisonOge

import unittest
from ..two_sum import two_sum

class Test2Sum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(two_sum([], 9), [])

    def test_no_pair(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 3), [])
    
    def test_one_pair(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_multiple_pairs(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 17), [0, 3])

if __name__ == '__main__':
    unittest.main()