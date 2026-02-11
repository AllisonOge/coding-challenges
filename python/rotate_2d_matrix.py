# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: rotate an n x n matrix in place by 90 degrees clockwise.


def rotate_2d_matrix(matrix):
    """Rotate ``matrix`` in place by 90 degrees clockwise.

    Mental roadmap:
    1. Process matrix ring-by-ring from outer to inner layer.
    2. For each position on top edge, rotate 4 cells in a cycle.
    3. Use one temp variable for safe in-place swapping.

    Toy example (2x2):
    [ [1,2],      [ [3,1],
      [3,4] ]  ->   [4,2] ]
    Why effective:
    Every element is moved exactly once to its rotated coordinate, with O(1)
    extra memory.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
