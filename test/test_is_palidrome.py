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

def count_allocations(func, *args, **kwargs):
    """count the number of memory allocations
    Args:
        func (function): function to count the number of memory allocations
        *args: arguments to pass to the function
        **kwargs: keyword arguments to pass to the function
    Return:
        count (int): number of memory allocations
    """
    count = 0
    def count_allocations_wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        return func(*args, **kwargs)
    return count_allocations_wrapper

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
        head = create_linked_list(list(range(1, 1001)) + list(range(999, 0, -1)))
        self.assertFalse(is_palindrome(head))
    
    def test_not_palindrome_equal_sum(self):
        head = create_linked_list([8, 50, 0, 72, 72, 0, 50, 8])
        self.assertFalse(is_palindrome(head))

    def test_memory_allocations(self):
        head = create_linked_list([1, 17, 972, 50, 98, 98, 50, 972, 17, 1])
        is_palindrome_count_allocations = count_allocations(is_palindrome)
        is_palindrome_count_allocations(head)
        self.assertEqual(is_palindrome_count_allocations.count, 1)
    
if __name__ == '__main__':
    unittest.main()