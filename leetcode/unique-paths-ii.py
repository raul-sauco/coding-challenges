# 63. Unique Paths II
# 🟠 Medium
#
# https://leetcode.com/problems/unique-paths-ii/
#
# Tags: Array - Dynamic Programming - Matrix

import timeit
from typing import List


# Similar to unique paths, since we can only move right or down, the
# number of ways to reach any cell equals the sum of the number of ways
# to reach the cell above it and the number of ways to reach the cell to
# its left. When we find an obstacle, the number of ways to reach that
# cell is 0 since we cannot visit it.
#
# Time complexity: O(m*n) - We will visit each cell once.
# Space complexity: O(n) - We use an array of size n to store
# intermediate results.
#
# Runtime 45 ms Beats 86.33%
# Memory 13.8 MB Beats 97.57%
class DP:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        # Prefill a row before the initial row in the grid.
        dp = [0, 1] + [0] * (n - 1)
        # Iterate over the matrix rows.
        for row in obstacleGrid:
            for i in range(1, len(dp)):
                if row[i - 1] == 1:
                    dp[i] = 0
                else:
                    dp[i] += dp[i - 1]
        return dp[-1]


def test():
    executors = [DP]
    tests = [
        [[[0, 1], [0, 0]], 1],
        [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], 6],
        [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.uniquePathsWithObstacles(t[0])
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
