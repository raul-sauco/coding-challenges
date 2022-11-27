# 2481. Minimum Cuts to Divide a Circle
# 🟢 Easy
#
# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/
#
# Tags: Math - Geometry

import timeit


# If n == 1, we do not need to cut, otherwise, if the number is uneven
# we need to make n radial cuts, but if n is uneven, we can make edge
# to edge cuts, diametral, and we only need n // 2 of them.
#
# Time complexity: O(1)
# Space complexity: O(1)
#
# Runtime: 59 ms, faster than 40.00%
# Memory Usage: 13.9 MB, less than 20.00%
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n % 2:
            return n if n != 1 else 0
        return n // 2


def test():
    executors = [Solution]
    tests = [
        [1, 0],
        [3, 3],
        [4, 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numberOfCuts(t[0])
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
