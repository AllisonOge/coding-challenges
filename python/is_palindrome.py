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

def reverse(head):
    """reverse a linked list
    Args:
        head (Node): head of a linked list
    Return:
        None
    """
    prev = None
    current = head

    while current:
        head = current.next
        current.next = prev
        prev = current
        current = head
    
    head = prev
    return head

def compare_lists(head1, head2):
    """check if two linked list are equal
    Args:
        head1 (Node): pointer to head of first list
        head2 (Node): pointer to head of second list
    Return:
        equal (bool): True if the linked lists are equal, False
        otherwise
    """
    temp1 = head1
    temp2 = head2

    while temp1 and temp2:
        if temp1.data != temp2.data:
            return False
        temp1 = temp1.next
        temp2 = temp2.next
    
    if temp1 is None and temp1 is None:
        return True
    
    return False

def is_palindrome(head):
    """check if the given linked list is palindrome or not
    Args:
        head (Node): head of the linked list
    Return:
        is_palindrome (bool): True if the linked list is palindrome, False otherwise
    """
    # Method 1: brute-force approach
    # slow = head
    # stack = []

    # while slow:
    #     stack.append(slow.data)
    #     slow = slow.next
    
    # while head:
    #     if head.data != stack.pop():
    #         return False
    #     head = head.next

    # Method 2: two-pointer approach
    is_palindrome = True
    slow = head
    prev_slow = None
    midnode = None
    fast = head

    # an empty and single list is palindrome
    if head == None or head.next == None:
        return is_palindrome

    while fast != None and fast.next != None:
        fast = fast.next.next
        prev_slow = slow
        slow = slow.next
    
    if fast != None:
        midnode = slow
        # move to second half
        slow = slow.next
    second_half = slow
    # null terminate first half
    prev_slow.next = None
    second_half = reverse(second_half)

    is_palindrome = compare_lists(head, second_half)

    # construct the original linked list back
    second_half = reverse(second_half)
    if midnode != None:
        prev_slow.next = midnode
        midnode.next = second_half
    else:
        prev_slow.next = second_half

    return is_palindrome
