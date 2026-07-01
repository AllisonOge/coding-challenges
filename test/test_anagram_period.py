#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.anagram_period import anagram_period


class TestAnagramPeriod(unittest.TestCase):
    def test_sample_string(self):
        self.assertEqual(anagram_period("abcbcacba"), 3)

    def test_single_character_period(self):
        self.assertEqual(anagram_period("aaaaaa"), 1)

    def test_exact_repeated_anagram_period(self):
        self.assertEqual(anagram_period("abab"), 2)

    def test_period_with_repeated_characters(self):
        self.assertEqual(anagram_period("aabbbbaa"), 4)

    def test_no_smaller_period(self):
        self.assertEqual(anagram_period("abcde"), 5)

    def test_empty_string(self):
        self.assertEqual(anagram_period(""), 0)


if __name__ == '__main__':
    unittest.main()
