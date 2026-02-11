#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.lockboxes import can_unlock_all


class TestLockboxes(unittest.TestCase):
    def test_can_unlock(self):
        boxes = [[1], [2], [3], []]
        self.assertTrue(can_unlock_all(boxes))

    def test_cannot_unlock(self):
        boxes = [[1, 3], [3, 0, 1], [2], [0]]
        self.assertFalse(can_unlock_all(boxes))


if __name__ == '__main__':
    unittest.main()
