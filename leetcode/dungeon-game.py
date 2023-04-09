# 174. Dungeon Game
# 🔴 Hard
#
# https://leetcode.com/problems/dungeon-game/
#
# Tags: Array - Dynamic Programming - Matrix

import timeit
from typing import List


# This is a template that can be used as the starting point of a
# solution with minimal changes.
#
# Time complexity: O() -
# Space complexity: O() -
#
# Runtime  ms Beats %
# Memory  MB Beats %
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        pass


def test():
    executors = [Solution]
    tests = [
        [[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 1],
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
