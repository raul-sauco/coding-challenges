# 54. Spiral Matrix
# 🟠 Medium
#
# https://leetcode.com/problems/spiral-matrix/
#
# Tags: Array - Matrix - Simulation

import timeit
from typing import List

# 1e4 calls:
# » Boundaries          0.04174   seconds
# » ElementCount        0.06738   seconds

# Define a helper function that lets us visualize the remaining section on the matrix in the debugger.
#
# Paste `viewRemaining(matrix, top, right, bottom, left)` into the watch section of the debugger and it will
# display the current remaining rows and columns that the algorithm needs to explore.
#
# It is designed to work with the `Boundaries` solution
def viewRemaining(matrix: List[List[int]], top: int, right: int, bottom: int, left: int) -> List[List[int]]:
    res = [[0] * (right - left) for _ in range(bottom - top)]
    for i in range(bottom - top):
        for j in range(right - left):
            res[i - top][j - left] = matrix[i][j]
    return res


# Keep track of the boundaries of the matrix area that we haven't explored yet and keep updating them as we visit
# rows and columns adding their values to the result.
# This solution is easier to understand, we can visualize it as "eliminating" each row and column from the matrix
# once we visit them.
# The process can be visualized using the helper function viewRemaining()
#
# Time complexity: O(n) - We visit each element in the matrix.
# Space complexity: O(1) - If we don't take into account the output list.
#
# Runtime: 35 ms, faster than 85.28% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13.8 MB, less than 99.02% of Python3 online submissions for Spiral Matrix.
class Boundaries:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize the boundaries.
        top, right, bottom, left = 0, len(matrix[0]), len(matrix), 0
        result = []
        while top < bottom and left < right:
            # Go right along the top row.
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # Go down along the right column.
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            # Prevent trying to move back on single row, or single column, matrices.
            if top == bottom or left == right:
                break

            # Go left along the bottom row.
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            # Go up along the leftmost column.
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result


# Count the total elements in the matrix and iterate that number of times keeping track of the direction and
# the rows and cols we have already visited.
# This solution is overly complicated and hard to read without offering any advantages.
#
# Time complexity: O(n) - We visit each element in the matrix.
# Space complexity: O(1) - If we don't take into account the output list.
#
# Runtime: 63 ms, faster than 12.34% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13.9 MB, less than 32.78% of Python3 online submissions for Spiral Matrix.
class ElementCount:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, right, bottom, left, dir = 0, n - 1, m - 1, 0, 0
        i, j, remaining, result = 0, 0, m * n, []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while remaining > 0:
            result.append(matrix[i][j])
            if dir == 0 and j == right:
                dir = 1
                top += 1
            elif dir == 1 and i == bottom:
                dir = 2
                right -= 1
            elif dir == 2 and j == left:
                dir = 3
                bottom -= 1
            elif dir == 3 and i == top:
                dir = 0
                left += 1

            i += directions[dir][0]
            j += directions[dir][1]
            remaining -= 1

        return result


def test():
    executors = [Boundaries, ElementCount]
    tests = [
        [
            [
                [1],
                [2],
                [3],
            ],
            [1, 2, 3],
        ],
        [[[1]], [1]],
        [
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ],
        [
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
            ],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.spiralOrder(t[0])
                exp = t[1]
                # The exercise asks for in-place modification of the matrix
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
