#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/05/13 19:51
# @Author : AllisonOge

import unittest
from python.is_palindrome import is_palindrome

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(arr):
    """create a linked list from an array
    Args:
        arr (list): array of integers
    Return:
        head (Node): head of the linked list
    """
    head = None
    tail = None

    for data in arr:
        if head is None:
            head = Node(data)
            tail = head
        else:
            tail.next = Node(data)
            tail = tail.next

    return head

class TestIsPalindrome(unittest.TestCase):
    def test_empty(self):
        head = None
        self.assertTrue(is_palindrome(head))
    
    def test_single(self):
        head = Node(1)
        self.assertTrue(is_palindrome(head))

    def test_palindrome_even(self):
        head = create_linked_list([1, 17, 972, 50, 98, 98, 50, 972, 17, 1])
        self.assertTrue(is_palindrome(head))
    
    def test_not_palindrome_even(self):
        head = create_linked_list([1, 17, 972, 50, 98, 98, 50, 972, 17, 2])
        self.assertFalse(is_palindrome(head))
    
    def test_palindrome_odd(self):
        head = create_linked_list([1, 17, 972, 50, 98, 50, 972, 17, 1])
        self.assertTrue(is_palindrome(head))
    
    def test_not_palindrome_odd(self):
        head = create_linked_list([1, 17, 972, 50, 98, 50, 972, 17, 2])
        self.assertFalse(is_palindrome(head))

    def test_long_palindrome(self):
        head = create_linked_list(list(range(1, 1001)) + list(range(1000, 0, -1)))
        self.assertTrue(is_palindrome(head))
    
    def test_long_not_palindrome(self):
        head = create_linked_list(list(range(1, 1001)) + list(range(999, 0, -1)) + [34, 56])
        self.assertFalse(is_palindrome(head))
    
    def test_not_palindrome_equal_sum(self):
        head = create_linked_list([8, 50, 0, 72, 72, 0, 8, 50])
        self.assertFalse(is_palindrome(head))

if __name__ == '__main__':
    unittest.main()