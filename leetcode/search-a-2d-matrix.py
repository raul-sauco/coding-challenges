# 74. Search a 2D Matrix
# 🟠 Medium
#
# https://leetcode.com/problems/search-a-2d-matrix/
#
# Tags: Array - Binary Search - Matrix

import timeit
from typing import List


# We can first use binary search on the first element of each row to
# find which row could possibly hold the target. Then use binary search
# on the row.
#
# Time complexity: O(log(n)) - Each iteration we eliminate half the
# search space.
# Space complexity: O(1) complexity, we only store pointers.
#
# Runtime: 66 ms, faster than 58.12%
# Memory Usage: 14.5 MB, less than 42.95%
class TwoPhaseBinSearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We can quickly discard values outside the range in the matrix.
        if (
            target < matrix[0][0]
            or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]
        ):
            return False
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            # Get the row between top and bottom.
            row = (bottom + top) // 2
            # If the first value of the row is bigger than the target,
            # the target needs to be in a row above this one
            if matrix[row][0] > target:
                bottom = row - 1
            # If the target is larger than the last value of this row,
            # it needs to be in a row below this one.
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                # The target is in this row.
                break

        # Binary search the value in the row.
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            # Get the value at the middle of the current range.
            mid = (right + left) // 2
            val = matrix[row][mid]
            # Update the pointers.
            if target > val:
                left = mid + 1
            elif target < val:
                right = mid - 1
            else:
                return True

        # The search failed, the target value does not exist in the
        # matrix.
        return False


# If we took each row of the matrix and appended it to the end of the
# previous row, we would have a sorted array, if we look at the problem
# that way, we can just use regular binary search. To find out which
# row and column the pointers point to, we can use div and mod.
#
# Time complexity: O(log(n)) - Each iteration we eliminate half the
# search space.
# Space complexity: O(1) complexity, we only store pointers.
#
# Runtime: 68 ms, faster than 54.31%
# Memory Usage: 14.5 MB, less than 42.97%
class BinarySearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We can quickly discard values outside the range in the matrix.
        # This conditional speeds up the results in LeetCode by 40%.
        if (
            target < matrix[0][0]
            or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]
        ):
            return False
        # Look at the matrix as one single array, the right pointer will
        # point at the last element.
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            # Get the value at the middle of the current range.
            mid = (right + left) // 2
            row, col = divmod(mid, len(matrix[0]))
            val = matrix[row][col]
            # Update the pointers.
            if target > val:
                left = mid + 1
            elif target < val:
                right = mid - 1
            else:
                return True
        # The value is not in the matrix.
        return False


def test():
    executors = [
        TwoPhaseBinSearch,
        BinarySearch,
    ]
    tests = [
        [[[1]], 1, True],
        [[[1]], 3, False],
        [[[1], [2], [3]], 3, True],
        [[[-1, 3, 10, 20]], 10, True],
        [[[-1, 3, 10, 20]], 20, True],
        [[[-1, 3, 10, 20]], 15, False],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], -63, False],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 63, False],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 7, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 10, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 20, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 23, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 30, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60, True],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 8, False],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 21, False],
        [
            [
                [1, 3, 5, 7, 9],
                [10, 11, 16, 20, 21],
                [23, 30, 34, 60, 62],
                [70, 80, 90, 100, 120],
                [170, 280, 390, 400, 620],
            ],
            20,
            True,
        ],
        [
            [
                [1, 3, 5, 7, 9],
                [10, 11, 16, 20, 21],
                [23, 30, 34, 60, 62],
                [70, 80, 90, 100, 120],
                [170, 280, 390, 400, 620],
            ],
            65,
            False,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.searchMatrix(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
