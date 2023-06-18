# 2328. Number of Increasing Paths in a Grid
# 🔴 Hard
#
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
#
# Tags: Array - Dynamic Programming - Depth-First Search - Breadth-First Search
# - Graph - Topological Sort - Memoization - Matrix

import timeit
from typing import List


# From each cell in the grid, compute the number of paths that start
# there, store already computed cells to avoid computing them multiple
# times.
#
# Time complexity: O(m*n) - We visit each cell in the grid, for each, we
# call the recursive function, the function only runs once per cell, if
# the number of paths from that cell has already been computed, it will
# return that value in O(1).
# Space complexity: O(m*n) - The size of the dp matrix.
#
# Runtime 1690 ms Beats 100%
# Memory 32.3 MB Beats 96.12%
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if dp[i][j] == -1:
                dp[i][j] = 1
                if i > 0 and grid[i][j] < grid[i - 1][j]:
                    dp[i][j] += dfs(i - 1, j)
                if j > 0 and grid[i][j] < grid[i][j - 1]:
                    dp[i][j] += dfs(i, j - 1)
                if i < m - 1 and grid[i][j] < grid[i + 1][j]:
                    dp[i][j] += dfs(i + 1, j)
                if j < n - 1 and grid[i][j] < grid[i][j + 1]:
                    dp[i][j] += dfs(i, j + 1)
                dp[i][j] %= 1_000_000_007
            return dp[i][j]

        return (
            sum(sum(dfs(i, j) for j in range(n)) for i in range(m))
            % 1_000_000_007
        )
        # The nested loops are slightly slower but have better memory
        # complexity than the list comprehension.
        res = 0
        for i in range(m):
            for j in range(n):
                res += dfs(i, j)
        return res % 1_000_000_007


def test():
    executors = [Solution]
    tests = [
        [[[1], [2]], 3],
        [[[1, 1], [3, 4]], 8],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countPaths(t[0])
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
