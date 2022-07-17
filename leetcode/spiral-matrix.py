# https://leetcode.com/problems/spiral-matrix/

# Tags: Array - Matrix - Simulation

import timeit
from typing import List


# Runtime: 63 ms, faster than 12.34% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13.9 MB, less than 32.78% of Python3 online submissions for Spiral Matrix.
class Solution:
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
    executors = [Solution]
    tests = [
        [[[1], [2], [3]], [1, 2, 3]],
        [[[1]], [1]],
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]],
        [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.spiralOrder(t[0])
                exp = t[1]
                # The exercise asks for in-place modification of the matrix
                result == exp, f"\033[93m» {t[0]} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
