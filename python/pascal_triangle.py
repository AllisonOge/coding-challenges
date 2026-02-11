# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: build Pascal's triangle up to n rows.


def pascal_triangle(n):
    """Return Pascal's triangle with ``n`` rows.

    :param n: number of rows
    :return: list of rows

    Mental roadmap:
    1. Start with the first row ``[1]``.
    2. Build each next row from the previous one.
    3. New row always starts/ends with ``1``.
    4. Middle values are pairwise sums from previous row.

    Toy example:
    prev = [1, 3, 3, 1]
    next = [1, (1+3), (3+3), (3+1), 1] -> [1, 4, 6, 4, 1]
    Why effective:
    Each value in Pascal's triangle is defined by exactly those two
    neighbors, so this construction is direct and linear in row size.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev = triangle[-1]
        row = [1]
        for i in range(1, len(prev)):
            row.append(prev[i - 1] + prev[i])
        row.append(1)
        triangle.append(row)
    return triangle
