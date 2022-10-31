# 766. Toeplitz Matrix
# 🟢 Easy
#
# https://leetcode.com/problems/toeplitz-matrix/
#
# Tags: Array - Matrix

import timeit
from typing import List

# 10e4 calls.
# » TravelDiagonals     0.02273   seconds
# » OptimizedSpace      0.01241   seconds

# Find all the cells on the top row and leftmost column, use them as the
# start of all the matrixes diagonals and compare their value with all
# the values in the diagonal, if any of them is different, return false
# otherwise, once we have checked all diagonals, return true.
#
# Time complexity: O(m*n) - We visit each cell once and do O(1) work.
# Space complexity: O(m+n) - The start cells array will store all the
# cell indexes for the top row and first column.
#
# Runtime: 175 ms, faster than 60.11%
# Memory Usage: 13.8 MB, less than 78.65%
class TravelDiagonals:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        NUM_ROWS, NUM_COLS = len(matrix), len(matrix[0])
        # Find the start cells of all positive diagonals.
        start_cells = [(0, i) for i in range(NUM_COLS)] + [
            (i, 0) for i in range(1, NUM_ROWS)
        ]
        for i, j in start_cells:
            # The entire diagonal should match the value at the start.
            val = matrix[i][j]
            # Visit all the diagonal's cells.
            i, j = i + 1, j + 1
            while i < NUM_ROWS and j < NUM_COLS:
                # If any of the cells has another value, return false.
                if matrix[i][j] != val:
                    return False
                i, j = i + 1, j + 1
        return True


# Optimize the previous solution memory complexity iterating over each
# element of the matrix except the ones on the first row and column
# comparing their value with their diagonal neighbor up and left, if we
# ever find two values that don't match, the matrix is not Toeplitz.
#
# Time complexity: O(m*n) - We visit each element and do O(1) work.
# Space complexity: O(1) - We only use constant space.
#
# Runtime: 92 ms, faster than 91.65%
# Memory Usage: 13.8 MB, less than 78.65%
class OptimizedSpace:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        NUM_ROWS, NUM_COLS = len(matrix), len(matrix[0])
        for i in range(1, NUM_ROWS):
            for j in range(1, NUM_COLS):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


def test():
    executors = [
        TravelDiagonals,
        OptimizedSpace,
    ]
    tests = [
        [[[1, 2], [2, 2]], False],
        [[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isToeplitzMatrix(t[0])
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
