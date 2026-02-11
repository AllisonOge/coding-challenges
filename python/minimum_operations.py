# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: compute minimum copy/paste operations to reach n H characters.


def min_operations(n):
    """Return fewest operations needed to reach ``n`` characters.

    Mental roadmap:
    1. Only useful operations are Copy-All + repeated Paste.
    2. Any optimal sequence breaks ``n`` into multiplicative steps.
    3. Those steps correspond to prime factors of ``n``.
    4. Sum those factors to get minimum operations.

    Toy example:
    n = 9 = 3 * 3
    Build 1 -> 3 in 3 ops, then 3 -> 9 in 3 ops, total = 6.
    Why effective:
    Factoring captures exactly the cheapest chunk sizes for copy/paste growth.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
