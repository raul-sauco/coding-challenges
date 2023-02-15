# Square Of Zeroes
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/square-of-zeroes
#
# Tags: Dynamic Programming

import timeit
from typing import List


# Compute the number of zeroes to the right and below each position in
# the matrix, then iterate over all positions in the matrix at O(n^2),
# for each position, check if it has a 0 and the number of zeroes to its
# right and below it and check if any of the squares that could be
# generated starting at this position is a square of zeroes.
#
# Time complexity: O(n^3) - O(n^2) to iterate over all the positions in
# the matrix, for each, in the worst case, we will check n different
# squares in O(1) each, to see if they form a valid square of zeroes.
# Space complexity: O(n^2) - The row and column count matrixes each has
# a n*n size.
class Solution:
    def squareOfZeroes(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        # Compute the number of zeroes below or to the right of this
        # cell if it contains a zero.
        row_sums, col_sums = [[[0] * n for _ in range(n)] for _ in range(2)]
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if matrix[i][j] == 0:
                    row_sums[i][j] = 1
                    # Not last row.
                    if j < n - 1:
                        row_sums[i][j] += row_sums[i][j + 1]
                    col_sums[i][j] = 1
                    # Not last col.
                    if i < n - 1:
                        col_sums[i][j] += col_sums[i + 1][j]
        # Generate all valid squares in the matrix and check if the
        # border is all zeroes.
        for i in range(n):
            for j in range(n):
                # The maximum size will be the minimum number of zeroes
                # below or to the right of the current square.
                for k in range(1, min(row_sums[i][j], col_sums[i][j]) + 1):
                    # We know we have k zeroes below and to the right
                    # of (i, j), check the other positions.
                    if (
                        i + k <= n - 1
                        and j + k <= n - 1
                        and row_sums[i + k][j] > k
                        and col_sums[i][j + k] > k
                    ):
                        return True
        return False


def test():
    executors = [Solution]
    tests = [
        [[[0, 0], [0, 0]], True],
        [[[0, 1], [0, 0]], False],
        [[[0, 0, 0], [1, 0, 0], [0, 0, 0]], True],
        [[[0, 0, 0], [0, 1, 0], [0, 1, 0]], False],
        [[[1, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1]], True],
        [[[0, 0, 0, 1], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 1]], True],
        [
            [
                [0, 0, 0, 1],
                [0, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 1],
            ],
            False,
        ],
        [
            [
                [1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 0, 1],
                [0, 0, 0, 1, 0, 1],
                [0, 1, 1, 1, 0, 1],
                [0, 0, 0, 0, 0, 1],
            ],
            True,
        ],
        [
            [
                [1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 0, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 1, 1, 1, 0, 1],
                [0, 0, 0, 0, 0, 1],
            ],
            False,
        ],
        [
            [
                [0, 1, 0, 1, 1, 1],
                [0, 1, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
            ],
            False,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.squareOfZeroes(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
