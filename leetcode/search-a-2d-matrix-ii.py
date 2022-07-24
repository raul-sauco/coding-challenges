# 240. Search a 2D Matrix II
# 🟠 Medium
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/
#
# Tags: Array - Binary Search - Divide and Conquer - Matrix

import timeit
from typing import List, Tuple

# 1e3 calls:
# » BinarySearch2D      0.01545   seconds
# » LinearSearch        0.00551   seconds
# » MixedSearch         0.01432   seconds

# We can use binary search updating two pointers, row and col.
#
# Time complexity; O(log(n)) - Each iteration we discard three quarters of the input.
# Space complexity; O(1) - If we don't consider the input matrix.
#
# Runtime: 199 ms, faster than 78.11% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.6 MB, less than 8.29% of Python3 online submissions for Search a 2D Matrix II.
class BinarySearch2D:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Recursive call with the section of the matrix that could contain the target.
        def searchRange(top_left: Tuple[int], bottom_right: Tuple[int]) -> bool:

            # Once we have a small enough matrix 3x3, check all the values.
            if top_left[0] - bottom_right[0] < 3 and top_left[1] - bottom_right[1] < 3:
                for row_idx in range(top_left[0], bottom_right[0] + 1):
                    for col_idx in range(top_left[1], bottom_right[1] + 1):
                        if matrix[row_idx][col_idx] == target:
                            return True
                return False

            # If we have a bigger than 3x3 matrix, divide it into smaller sections.
            # Get the middle value and use it to determine which side of the matrix we need to explore.
            mid_row = top_left[0] + ((bottom_right[0] - top_left[0]) // 2)
            mid_col = top_left[1] + ((bottom_right[1] - top_left[1]) // 2)
            val = matrix[mid_row][mid_col]

            if target < val:
                # We want to search from the current top-left to the current (mid_row, mid_col).
                return searchRange(top_left, (mid_row, mid_col))
            elif target == val:
                return True
            else:
                # We want to search two ranges, to the right and below the current row taking care not to go out of bounds.
                if mid_row < len(matrix) - 1 and mid_col < len(matrix[0]) - 1:
                    return searchRange((top_left[0], mid_col), (mid_row, bottom_right[1])) or searchRange(
                        (mid_row + 1, top_left[1]), bottom_right
                    )
                elif mid_row < len(matrix) - 1:
                    return searchRange((top_left[0], mid_col), (mid_row, bottom_right[1]))
                elif mid_col < len(matrix[0]) - 1:
                    return searchRange((mid_row + 1, top_left[1]), bottom_right)

                return False

        # Initial call, search the entire matrix.
        return searchRange((0, 0), (len(matrix) - 1, len(matrix[0]) - 1))


# We can improve on the O(log(n)) solution and search in linear n+m time starting at the bottom and moving:
#
# - One column to the right, if the value is smaller than the target.
# - One row up, if the value is greater than the target.
#
# Time complexity: O(n+m) - n: number of rows, m: number of columns, we visit each row and column a maximum of 1 time.
# Space complexity: O(1) - We only store two pointers in memory.
#
# Runtime: 176 ms, faster than 94.26% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.4 MB, less than 84.45% of Python3 online submissions for Search a 2D Matrix II.
class LinearSearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            val = matrix[row][col]
            if val == target:
                return True
            # If it does not match, move in function of the current value
            if val < target:
                # If the current value is less than the target, we want to check the values to the right.
                col += 1
            else:
                # If the current value is greater than the target, we want to check values above.
                row -= 1

        # If the search went out of bounds, the value is not in the matrix.
        return False


# We can also mix the two previous solutions. Use binary search when the size of the input matrix is big, then move
# to linear search once we have a smaller matrix.
#
# Intuitively this should perform better than either of the two previous solutions but it isn't the case.
#
# Runtime: 317 ms, faster than 24.54% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.7 MB, less than 8.29% of Python3 online submissions for Search a 2D Matrix II.
class MixedSearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Recursive call with the section of the matrix that could contain the target.
        def searchRange(top_left: Tuple[int], bottom_right: Tuple[int]) -> bool:

            limit = 20
            # Once we have a small enough matrix limit x limit, use linear search.
            if top_left[0] - bottom_right[0] < limit and top_left[1] - bottom_right[1] < limit:
                # Start at the bottom-left corner
                row, col = len(matrix) - 1, 0
                while row >= top_left[0] and col < bottom_right[1] + 1:
                    val = matrix[row][col]
                    if val == target:
                        return True
                    # If it does not match, move in function of the current value
                    if val < target:
                        # If the current value is less than the target, we want to check the values to the right.
                        col += 1
                    else:
                        # If the current value is greater than the target, we want to check values above.
                        row -= 1

                # If the search went out of bounds, the value is not in the matrix.
                return False

            # If we have a bigger than 3x3 matrix, divide it into smaller sections.
            # Get the middle value and use it to determine which side of the matrix we need to explore.
            mid_row = top_left[0] + ((bottom_right[0] - top_left[0]) // 2)
            mid_col = top_left[1] + ((bottom_right[1] - top_left[1]) // 2)
            val = matrix[mid_row][mid_col]

            if target < val:
                # We want to search from the current top-left to the current (mid_row, mid_col).
                return searchRange(top_left, (mid_row, mid_col))
            elif target == val:
                return True
            else:
                # We want to search two ranges, to the right and below the current row taking care not to go out of bounds.
                if mid_row < len(matrix) - 1 and mid_col < len(matrix[0]) - 1:
                    return searchRange((top_left[0], mid_col), (mid_row, bottom_right[1])) or searchRange(
                        (mid_row + 1, top_left[1]), bottom_right
                    )
                elif mid_row < len(matrix) - 1:
                    return searchRange((top_left[0], mid_col), (mid_row, bottom_right[1]))
                elif mid_col < len(matrix[0]) - 1:
                    return searchRange((mid_row + 1, top_left[1]), bottom_right)

                return False

        # Initial call, search the entire matrix.
        return searchRange((0, 0), (len(matrix) - 1, len(matrix[0]) - 1))


def test():
    executors = [BinarySearch2D, LinearSearch, MixedSearch]
    tests = [
        [[[1, 1]], 0, False],
        [[[1, 1]], 1, True],
        [[[1]], 1, True],
        [[[2]], 1, False],
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
            True,
        ],
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            2,
            True,
        ],
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            1,
            True,
        ],
        [
            [
                [1, 4, 7, 11],
                [2, 5, 8, 12],
                [3, 6, 9, 16],
                [10, 13, 14, 17],
                [18, 21, 23, 26],
            ],
            17,
            True,
        ],
        [
            [
                [1, 4, 7, 11],
                [2, 5, 8, 12],
                [3, 6, 9, 16],
                [10, 13, 14, 17],
                [18, 21, 23, 26],
            ],
            14,
            True,
        ],
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
            False,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.searchMatrix(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
