# -*- coding: utf-8 -*-
# @Time : 2023/05/07 07:54
# @Author : AllisonOge
# @Describe: create a function to find a pair of numbers from a set of numbers that add up to a target number

def two_sum(nums, target):
    """
    :param nums: a list of numbers
    :param target: a target number
    :return: a list of the index of the pair of numbers that add up to the target number
    
    :example:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    """
    # hash table to store the number and its index
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[num], i]

    num_indices[num] = i
    return []

# time and space complexity: O(n)
# this is because it take O(n) time to iterate through the list of numbers and O(n) space to store the hash table