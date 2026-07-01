# -*- coding: utf-8 -*-
# @Time : 2026/07/01 01:12
# @Author : AllisonOge from an Python AI interview
# @Descirbe: Given a string of characters, find the smallest anagram that can be used to produce the string.

# Ex. give abcbcacba the anagram substring abc can be represented in abc, bca and cba to form the string.

# helper function
def char_freq(substr):
    d = {c: 0 for c in set(substr)}
    for c in substr:
        d[c] += 1
    return d


def anagram_period(s):
    """Find the length of the shortest anagram period in a string.

    A period is valid when the input can be split into equal-sized blocks and
    every block is an anagram of the first block.

    Args:
        s (str): String to inspect.

    Return:
        int: Length of the smallest valid anagram period. Return 0 for an empty
            string. If no shorter period exists, return len(s).

    Examples:
        anagram_period("abcbcacba") -> 3
        anagram_period("abab") -> 2
        anagram_period("aaaaaa") -> 1
        anagram_period("abcde") -> 5
    """
    if len(s) == 0:
        return 0
    n = len(s)
    for k in range(2, n):
        ss = s[:k]
        target = char_freq(ss)
        valid = True
        for i in range(len(ss), n, len(ss)):
            pred = char_freq(s[i:i+k])
            if target != pred:
                valid = False

        if valid:
            return len(ss)
    # handle single char anagram
    return len(s)


if __name__ == "__main__":
    print(anagram_period("abcbcacba"))
