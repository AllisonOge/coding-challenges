#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.utf8_validation import valid_utf8


class TestUtf8Validation(unittest.TestCase):
    def test_valid_data(self):
        self.assertTrue(valid_utf8([197, 130, 1]))

    def test_invalid_data(self):
        self.assertFalse(valid_utf8([235, 140, 4]))


if __name__ == '__main__':
    unittest.main()
