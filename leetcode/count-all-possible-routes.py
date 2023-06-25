# 1575. Count All Possible Routes
# 🔴 Hard
#
# https://leetcode.com/problems/count-all-possible-routes/
#
# Tags: Array - Dynamic Programming - Memoization

import timeit
from functools import cache
from typing import List


# We can use memoization, starting at each city, we can decide to visit
# any other city, including ones that we have visited previously, any
# time we reach the destination, we could stop there, and that would be
# one of the possible routes, but we can also keep going. If we run out
# of fuel, we return 0 to represent that the branch did not lead to a
# route, even though it could have included some possible routes if it
# went through the finish location at some middle point.
#
# Time complexity: O(m*n) - Where m is the number of locations and n is
# the number of different values that the remaining fuel could take, and
# could be equal to the initial fuel. Once we have computed m*n calls to
# dfs, any possible result will be stored in the cache and calls would
# be solved in O(1)
# Space complexity: O(m*n) - The size of the cache.
#
# Runtime 2055 ms Beats 63.16%
# Memory 33.9 MB Beats 31.58%
class Solution:
    def countRoutes(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        @cache
        def dfs(l: int, fuel: int) -> int:
            if fuel < 0:
                return 0
            return (
                sum(
                    dfs(i, fuel - abs(locations[i] - locations[l]))
                    for i in range(len(locations))
                    if i != l
                )
                + (1 if l == finish else 0)
            ) % 1_000_000_007

        return dfs(start, fuel)


def test():
    executors = [Solution]
    tests = [
        [[4, 3, 1], 1, 0, 6, 5],
        [[5, 2, 1], 0, 2, 3, 0],
        [[2, 3, 6, 8, 4], 1, 3, 5, 4],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countRoutes(t[0], t[1], t[2], t[3])
                exp = t[4]
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
