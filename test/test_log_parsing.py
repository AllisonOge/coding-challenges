#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.log_parsing import parse_log_lines


class TestLogParsing(unittest.TestCase):
    def test_parse_valid_and_invalid_lines(self):
        lines = [
            '10.0.0.1 - [2026-02-11] "GET /projects/260 HTTP/1.1" 200 12',
            '10.0.0.1 - [2026-02-11] "GET /projects/260 HTTP/1.1" 404 88',
            'invalid line',
        ]
        total, counts = parse_log_lines(lines)
        self.assertEqual(total, 100)
        self.assertEqual(counts[200], 1)
        self.assertEqual(counts[404], 1)


if __name__ == '__main__':
    unittest.main()
