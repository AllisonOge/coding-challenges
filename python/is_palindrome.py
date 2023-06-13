# -*- coding: utf-8 -*-
# @Time : 2023/05/13 19:46
# @Author : AllisonOge from GeeksForGeeks
# @Descirbe: Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.

# Limits
# Time limit: 80 seconds per test case.
# Memory limit: 64 megabytes.
# 1 ≤ N ≤ 10^5
#
# Link to problem statement: https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

def is_palindrome(head):
    """check if the given linked list is palindrome or not
    Args:
        head (Node): head of the linked list
    Return:
        is_palindrome (bool): True if the linked list is palindrome, False otherwise
    """
    slow = head
    stack = []

    while slow:
        stack.append(slow.data)
        slow = slow.next
    
    while head:
        if head.data != stack.pop():
            return False
        head = head.next
    return True
