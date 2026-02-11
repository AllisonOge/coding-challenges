# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: solve the N-Queens puzzle and return all solutions.


def solve_n_queens(n):
    """Return all solutions as [[col, row], ...] for each board.

    Mental roadmap:
    1. Place one queen per row.
    2. For each row, try every column.
    3. Reject positions that clash on column/diagonals.
    4. Recurse to next row; backtrack on dead ends.

    Toy example (n=4):
    row0->col1, row1->col3, row2->col0, row3->col2 is valid.
    Any choice that blocks a future row is undone immediately.
    Why effective:
    Pruning invalid partial boards avoids exploring most impossible states.
    """
    if n < 4:
        return []

    solutions = []
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    placement = [-1] * n

    def backtrack(row):
        if row == n:
            solutions.append([[r, placement[r]] for r in range(n)])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            placement[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return solutions
