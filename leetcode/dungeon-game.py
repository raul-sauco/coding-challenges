# 174. Dungeon Game
# 🔴 Hard
#
# https://leetcode.com/problems/dungeon-game/
#
# Tags: Array - Dynamic Programming - Matrix

import timeit
from typing import List


# Start at the "princess" and traverse the matrix backwards computing the
# minimum health we need to start with from that cell to be able to reach
# the princess.
#
# Time complexity: O(m*n) - Nested loops with m and n elements each,
# inside the inner loop we do O(1) work.
# Space complexity: O(n) - Two lists of size n each.
#
# Runtime 70 ms Beats 74.67%
# Memory 17.32 MB Beats 78.51%
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [float("inf")] * (n + 1)
        dp[n - 1] = 1
        prev = [x for x in dp]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[j] = min(prev[j], dp[j + 1]) - dungeon[i][j]
                if dp[j] < 1:
                    dp[j] = 1
            prev = dp
            dp[n] = float("inf")
        return prev[0]


def test():
    executors = [Solution]
    tests = [
        [[[0]], 1],
        [[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.calculateMinimumHP(t[0])
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
