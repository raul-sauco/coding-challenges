# 498. Diagonal Traverse
# 🟠 Medium
#
# https://leetcode.com/problems/diagonal-traverse/
#
# Tags: Array - Matrix - Simulation

import timeit
from collections import defaultdict
from typing import List


# Use the fact that row_idx + col_idx results in the same value for all
# elements in the same negative diagonals, which are the ones that the
# problem is asking us to find, to place all cell values into lists
# indexed by their row_idx + col_idx value. Then iterate over the
# entries in the dictionary, since Python 3.6 the dictionary guarantees
# that it will return the keys in the same order they were inserted on,
# which is guaranteed to be the same order we want because we visit
# lower row/column values first. The only extra step we need to take is
# to reverse all even diagonals to simulate the up/down travel.
#
# Time complexity: O(n) - We visit each cell once to add its value to
# the dictionary and once to copy the value to the result.
# Space complexity: O(n) - The dictionary will grow to the same size
# as the input.
#
# Runtime: 194 ms, faster than 95.96%
# Memory Usage: 17.9 MB, less than 27.87%
class DiagonalDictionary:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                diagonals[i + j].append(mat[i][j])
        return [
            val
            for key in diagonals.keys()
            for val in (
                diagonals[key] if key % 2 else reversed(diagonals[key])
            )
        ]


def test():
    executors = [
        DiagonalDictionary,
    ]
    tests = [
        [[[2, 3]], [2, 3]],
        [[[1, 2], [3, 4]], [1, 2, 3, 4]],
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findDiagonalOrder(t[0])
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
