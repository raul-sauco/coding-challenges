# https://leetcode.com/problems/set-matrix-zeroes/

# Tags: Array - Hash Table - Matrix

import timeit
from typing import List


# The obvious solution is to find rows and columns that contain 0s and store them in two sets,
# then iterate over the rows, and columns, in the sets, and update all their values to 0.
#
# Time complexity: O(n) - We iterate once over all the positions in the matrix, then once more over all the positions
# that need to be updated.
# Space complexity: O(a+b) the number of rows and columns that need to be updated, a max of len(matrix) + len(matrix[0])
# if all the values in the matrix need to be updated.
#
# Runtime: 134 ms, faster than 92.22% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 14.7 MB, less than 90.07% of Python3 online submissions for Set Matrix Zeroes.
class Sets:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()

        # Store all rows and column numbers that contain 0s
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over all marked rows and columns and update them to 0
        for row in rows:
            for col in range(len(matrix[row])):
                matrix[row][col] = 0

        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0


# Follow-up question, do the same with constant space.
#
# Time complexity: O(n) - we iterate over the matrix elements a constant number of times
# Space complexity: O(1) - we keep a fixed number of variables in memory
#
# Runtime: 233 ms, faster than 28.76% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 14.9 MB, less than 15.43% of Python3 online submissions for Set Matrix Zeroes.
class Sets:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        FLAG = "#"
        row0 = False
        # Find zero values
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    # Use a separate flag for row[0] to differentiate from column[0]
                    if i == 0:
                        row0 = True
                    else:
                        matrix[i][0] = FLAG

                    matrix[0][j] = FLAG

        for i in range(1, len(matrix)):
            if matrix[i][0] == FLAG:
                # Update the row to 0
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0

        for j in range(len(matrix[0]) - 1, -1, -1):
            if matrix[0][j] == FLAG:
                # Update the column to 0
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        if row0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0


def test():
    executors = [Sets]
    tests = [
        [
            [[0, 2, 3, 4], [5, -20, 7, 8], [-4, 10, 11, 12], [13, 14, 15, -30]],
            [[0, 0, 0, 0], [0, -20, 7, 8], [0, 10, 11, 12], [0, 14, 15, -30]],
        ],
        [
            [[-4, -2147483648, 6, -7, 0], [-8, 6, -8, -6, 0], [2147483647, 2, -9, -6, -10]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [2147483647, 2, -9, -6, 0]],
        ],
        [
            [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]],
            [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        ],
        [[[-1], [2], [3]], [[-1], [2], [3]]],
        [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]],
        [[[0]], [[0]]],
        [[[4]], [[4]]],
        [[[4], [5], [11], [0]], [[0], [0], [0], [0]]],
        [[[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]],
        [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                sol.setZeroes(t[0])
                exp = t[1]
                # The problem asks for in-place modification of the matrix
                assert t[0] == exp, f"\033[93m» {t[0]} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
