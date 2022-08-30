# 1329. Sort the Matrix Diagonally
# 🟠 Medium
#
# https://leetcode.com/problems/sort-the-matrix-diagonally/
#
# Tags: Array - Sorting - Matrix

import timeit
from collections import defaultdict
from typing import List


# Iterate over all matrix positions starting at the top-left and add
# each value to a list formed by all the values of the given diagonal.
# We can easily determine which positive diagonal a position belongs to
# subtracting its column index from its row index. Once we have all the
# diagonals expressed as lists, sort them, then create a result matrix
# of the same size as the input matrix and iterate over its positions
# assigning the correct value obtained from the dictionary.
#
# Time complexity: O(m*n*log(min(m,n))) - We iterate over all the matrix
# positions, for each diagonal, of max length min(m,n), we sort it.
# Space complexity: O(m*n) - The diagonals dictionary has the same size
# as the matrices.
#
# Runtime: 91 ms, faster than 88.85%
# Memory Usage: 14.6 MB, less than 10.92%
class DiagonalsHashTable:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Store the number of rows and columns
        num_rows, num_cols = len(mat), len(mat[0])
        # Using a default dictionary we don't need to check if the
        # diagonals have been added to the dictionary already.
        diagonals = defaultdict(list)
        # Iterate over the rows and columns adding each cell to its
        # diagonal in the dictionary. O(m*m)
        for i in range(num_rows):
            for j in range(num_cols):
                diagonals[i - j].append(mat[i][j])
        # Sort all the diagonals O((m*n)*log(min(m,n))).
        for k in diagonals:
            diagonals[k].sort(reverse=1)
        # Initialize a matrix of the same size as the input.
        result = [[0] * num_cols for _ in range(num_rows)]
        # Fill the result matrix with the sorted diagonal values.
        for i in range(num_rows):
            for j in range(num_cols):
                result[i][j] = diagonals[i - j].pop()
        return result


# We can also iterate over the diagonals one by one, collecting their
# values sorting and assigning them to the result matrix.
#
# Time complexity: O(m*n*log(min(m,n))) - Same as the previous solution.
# Space complexity: O(min(m,n)) - We only store diagonals in memory.
#
# Runtime: 99 ms, faster than 81.81%
# Memory Usage: 14.4 MB, less than 51.64%
class SingleDiagonalSort:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Store the number of rows and columns
        m, n = len(mat), len(mat[0])
        # Create a matrix to store results. We could modify in place
        # the input instead if the description asked for that.
        result = [[0] * n for _ in range(m)]
        # Define a function that sorts a diagonal given its top-left.
        def sort(i, j):
            vals = []
            # Iterate over the diagonal cells collecting their values.
            while i < m and j < n:
                vals.append(mat[i][j])
                i += 1
                j += 1
            # Sort the collected values at O(log(len(vals))).
            vals.sort()
            # Assign the sorted values
            while i and j:
                j -= 1
                i -= 1
                result[i][j] = vals.pop()

        # Sort all diagonals that start at col 0.
        for i in range(m):
            sort(i, 0)
        # Sort all diagonals that start at row 0.
        for j in range(n):
            sort(0, j)
        return result


# Similar to the previous version but use some built in functions to
# improve performance using C code.
#
# Time complexity: O(m*n*log(min(m,n))) - Same as the previous solution.
# Space complexity: O(min(m,n)) - We only store diagonals in memory.
#
# Runtime: 158 ms, faster than 31.57%
# Memory Usage: 14.2 MB, less than 76.29%
class BuiltInFn:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Get the num of rows and columns.
        m, n = len(mat), len(mat[0])
        # Define a function that sorts diagonals in place.
        def sort(i, j):
            ij = list(zip(mat[i:], range(j, n)))
            vals = iter(sorted(r[j] for r, j in ij))
            for r, j in ij:
                r[j] = next(vals)

        # Sort diagonals that start in col 0.
        for i in range(m):
            sort(i, 0)
        # Sort diagonals that start in row 0.
        for j in range(n):
            sort(0, j)
        return mat


def test():
    executors = [
        DiagonalsHashTable,
        SingleDiagonalSort,
        BuiltInFn,
    ]
    tests = [
        [
            [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]],
            [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]],
        ],
        [
            [
                [11, 25, 66, 1, 69, 7],
                [23, 55, 17, 45, 15, 52],
                [75, 31, 36, 44, 58, 8],
                [22, 27, 33, 25, 68, 4],
                [84, 28, 14, 11, 5, 50],
            ],
            [
                [5, 17, 4, 1, 52, 7],
                [11, 11, 25, 45, 8, 69],
                [14, 23, 25, 44, 58, 15],
                [22, 27, 31, 36, 50, 66],
                [84, 28, 75, 33, 55, 68],
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.diagonalSort(t[0])
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
