# 1431. Kids With the Greatest Number of Candies
# 🟢 Easy
#
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
#
# Tags: Array

import timeit
from typing import List


# Find the boundary for a kid's candies to be the maximum after we give
# them the extra candies as the maximum of the array minus the extra
# candies, then iterate checking if the value at each position plus the
# extra candies would be greater than the original greatest.
#
# Time complexity: O(n) - Two passes of the input array.
# Space complexity: O(1) - Or, O(n) if we take into account the output
# array.
#
# Runtime 41 ms Beats 54.32%
# Memory 13.8 MB Beats 50.96%
class Solution:
    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        boundary = max(candies) - extraCandies
        return [c >= boundary for c in candies]


def test():
    executors = [Solution]
    tests = [
        [[2, 3, 5, 1, 3], 3, [True, True, True, False, True]],
        [[4, 2, 1, 1, 2], 1, [True, False, False, False, False]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.kidsWithCandies(t[0], t[1])
                exp = t[2]
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
