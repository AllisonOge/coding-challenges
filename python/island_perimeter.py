# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: calculate the perimeter of an island in a grid.


def island_perimeter(grid):
    """Return the total perimeter of land cells in ``grid``.

    Mental roadmap:
    1. Each land cell contributes 4 edges initially.
    2. Shared sides between adjacent land cells are internal, not perimeter.
    3. While scanning, only check top and left neighbors.
    4. For each shared side found, subtract 2 once.

    Toy example:
    grid = [[1, 1]]
    two cells contribute 8 total edges.
    one shared side removes 2 -> perimeter 6.
    Why effective:
    It avoids double-counting corrections and runs in one grid pass.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:
                continue

            perimeter += 4
            if r > 0 and grid[r - 1][c] == 1:
                perimeter -= 2
            if c > 0 and grid[r][c - 1] == 1:
                perimeter -= 2

    return perimeter
