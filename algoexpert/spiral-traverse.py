# Spiral Traverse
# 🟠 Medium
#
# https://www.algoexpert.io/questions/spiral-traverse
#
# Tags: Array - Matrix

import timeit
from typing import List


# Use four pointers to mark the boundaries of the section of the matrix
# that we have not explored yet. Use four nested loops to explore top
# row, right column, bottom row then left column, adding the values to
# the result.
#
# Time complexity: O(n) - We visit each cell once.
# Space complexity: O(1) - Constant extra space is used.
class Solution:
    def spiralTraverse(self, array: List[int]) -> bool:
        # Define some boundaries.
        top, right, bottom, left, res = 0, len(array[0]), len(array), 0, []
        # While we still have cells to visit.
        while top < bottom and left < right:
            # Top row rightwards.
            for j in range(left, right):
                res.append(array[top][j])
            top += 1
            # Right column down.
            for i in range(top, bottom):
                res.append(array[i][right - 1])
            right -= 1
            # Prevent trying to move back on uneven number of rows/cols.
            if top == bottom or left == right:
                break
            # Bottom row reverse.
            for j in reversed(range(left, right)):
                res.append(array[bottom - 1][j])
            bottom -= 1
            # Left column up.
            for i in reversed(range(top, bottom)):
                res.append(array[i][left])
            left += 1
        return res


def test():
    executors = [Solution]
    tests = [
        [
            [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        ],
        [
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.spiralTraverse(t[0])
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
