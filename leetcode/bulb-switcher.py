# 319. Bulb Switcher
# 🟠 Medium
#
# https://leetcode.com/problems/bulb-switcher/
#
# Tags: Math - Brain Teaser

import timeit
from math import sqrt


# The perfect squares will remain on after n number of toggles, we can
# compute the number of perfect squares as the floor of the sqrt of n.
#
# Time complexity: O(log(n)) - I believe that sqrt in Python is log(n).
# Space complexity: O(1) - I believe that sqrt uses constant space.
#
# Runtime 54 ms Beats 8.42%
# Memory 16.3 MB Beats 34.9%
class Sqrt:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))


# Sqrt is pretty slow because it is trying to find an accurate solution,
# since we are only trying to find the floor of the solution, we can
# try to use binary search.
#
# Time complexity: O() -
# Space complexity: O() -
#
# Runtime 23 ms Beats 96.51%
# Memory 16.2 MB Beats 34.9%
class BinarySearch:
    def bulbSwitch(self, n: int) -> int:
        l, r = 0, min(n, 31622)
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > n:
                r = mid - 1
            else:
                l = mid + 1
        return r


def test():
    executors = [
        Sqrt,
        BinarySearch,
    ]
    tests = [
        [0, 0],
        [1, 1],
        [3, 1],
        [4, 2],
        [6, 2],
        [8, 2],
        [9, 3],
        [10, 3],
        [24, 4],
        [25, 5],
        [35, 5],
        [36, 6],
        [48, 6],
        [49, 7],
        [60, 7],
        [80, 8],
        [100, 10],
        [81_423, 285],
        [1_000_000_000, 31622],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.bulbSwitch(t[0])
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
