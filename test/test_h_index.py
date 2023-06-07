#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/05/07 08: 16
# @Author : AllisonOge

import unittest
from python.h_index import h_index


class TestHIndex(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(h_index([]), [])

    def test_one_paper(self):
        self.assertEqual(h_index([5]), [1])

    def test_multiple_papers(self):
        self.assertEqual(h_index([5, 1, 2]), [1, 1, 2])

    def test_multiple_papers_2(self):
        self.assertEqual(h_index([1, 3, 3, 2, 2, 15]), [1, 1, 2, 2, 2, 3])


if __name__ == '__main__':
    unittest.main()
