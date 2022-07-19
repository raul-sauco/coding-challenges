# https://leetcode.com/problems/range-sum-query-2d-immutable/

# Tags: Array - Design - Matrix - Prefix Sum

import timeit
from typing import List


# The naive approach would be to assign the matrix and calculate the result
# on each call to the sumRegion.
#
# Time complexity: O(n^2)
# Space complexity: O1
#
# Time limit exceeded on LeetCode.
class Naive:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                sum += self.matrix[row][col]
        return sum


# Create a matrix of prefix sums when the class is instantiated.
# Then use the prefix sums to calculate the sum of any submatrix in O(1)
#
# Time complexity of __init__: O(n) - we visit each element of the matrix to create the prefix sum.
# Time complexity of sumRegion: O(1) - using the prefix sum we can access in constant time a maximum of 4 matrix
# elements to create the sum of all elements in the submatrix.
# Space complexity: O(n) - We keep a matrix of size n in memory
#
# Runtime: 1808 ms, faster than 82.98% of Python3 online submissions for Range Sum Query 2D - Immutable.
# Memory Usage: 24.6 MB, less than 88.71% of Python3 online submissions for Range Sum Query 2D - Immutable.
class PrefixSum:
    def __init__(self, matrix: List[List[int]]):
        # Exit if no matrix passed in as input
        if matrix == None or not matrix or matrix[0] == None or not matrix[0]:
            return
        self.sums = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row_idx, row in enumerate(matrix):
            row_sum = 0
            for col_idx, col in enumerate(row):
                row_sum += col
                self.sums[row_idx][col_idx] = row_sum if row_idx == 0 else row_sum + self.sums[row_idx - 1][col_idx]

        print(self.sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Start with the total at the bottom-right edge of the selected area
        result = self.sums[row2][col2]
        # If the start row is not the first one, subtract the sum at (row1-1,col2)
        if row1 > 0:
            result -= self.sums[row1 - 1][col2]
        # If the start col is not the first one, subtract the sum at (row2, col1-1)
        if col1 > 0:
            result -= self.sums[row2][col1 - 1]
        # If both the start column and the start row are not the first one, we
        # have subtracted that area twice, we have to re-add its value
        if row1 > 0 and col1 > 0:
            result += self.sums[row1 - 1][col1 - 1]
        return result


def test():
    executors = [Naive, PrefixSum]
    tests = [
        [
            [
                [3, 0, 1, 4, 2],
                [5, 6, 3, 2, 1],
                [1, 2, 0, 1, 5],
                [4, 1, 0, 1, 7],
                [1, 0, 3, 0, 5],
            ],
            {  # Sum: submatrix vertices
                8: [2, 1, 4, 3],
                11: [1, 1, 2, 2],
                12: [1, 2, 2, 4],
            },
        ]
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor(t[0])
                for sum in t[1]:
                    result = sol.sumRegion(*t[1][sum])
                    exp = sum
                    assert (
                        result == exp
                    ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
