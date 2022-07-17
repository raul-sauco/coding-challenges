# https://leetcode.com/problems/rotate-image/


# Tags: Array - Math - Matrix


import timeit
from typing import List

import numpy as np


# Iterate over half the rows, and the columns in the row that have not been reordered yet, and move the elements
# in groups of the four symmetrical positions from the center of the matrix.
# In Matrixes with an uneven n, the central element does not need to move.
#
# Time complexity: O(n) - we visit each element once.
# Space complexity: O(1) - we keep 6 values in memory, independently of the size of the matrix.
#
# Runtime: 47 ms, faster than 68.66% of Python3 online submissions for Rotate Image.
# Memory Usage: 13.9 MB, less than 74.54% of Python3 online submissions for Rotate Image.
class Iterative:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Reordering half the rows recursively reorders half the matrix
        for row in range(len(matrix) // 2):
            # Go through all the positions in the row we haven't moved already
            for col in range(row, len(matrix) - (row + 1)):
                # For each origin, we need to move the four symmetrical positions
                val = matrix[row][col]
                for _ in range(4):
                    dest_row, dest_col = col, (len(matrix) - 1) - row
                    dest_val = matrix[dest_row][dest_col]
                    matrix[dest_row][dest_col] = val

                    # Prepare values for the next substitution
                    val, col, row = dest_val, dest_col, dest_row


# Similar idea but we assign the 4 values directly instead of using a for loop.
#
# Time complexity: O(n) - we visit each element once.
# Space complexity: O(1) - we keep 6 values in memory, independently of the size of the matrix.
#
# Runtime: 64 ms, faster than 27.95% of Python3 online submissions for Rotate Image.
# Memory Usage: 13.8 MB, less than 74.54% of Python3 online submissions for Rotate Image.
class IterDirectAssign:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i], matrix[n - 1 - i][n - j - 1], matrix[j][n - 1 - i], matrix[i][j] = (
                    matrix[n - 1 - i][n - j - 1],
                    matrix[j][n - 1 - i],
                    matrix[i][j],
                    tmp,
                )


# Official "elegant" solution using standard matrix operations.
#
# Time complexity: O(n) - we visit each element twice.
# Space complexity: O(1) - we only store the loop counters in memory.
#
# Runtime: 52 ms, faster than 56.56% of Python3 online submissions for Rotate Image.
# Memory Usage: 13.9 MB, less than 74.54% of Python3 online submissions for Rotate Image.
class TransposeReflect:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        # Reflect
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


class LibraryFn:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = np.array(matrix)
        m = m.transpose()
        matrix = np.fliplr(m).tolist()


def test():
    executors = [
        Iterative,
        # IterDirectAssign,
        # TransposeReflect,
        # LibraryFn,
    ]
    tests = [
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        ],
        [
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        ],
        [[[1]], [[1]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.rotate(t[0])
                exp = t[1]
                # The exercise asks for in-place modification of the matrix
                t[0] == exp, f"\033[93m» {t[0]} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
