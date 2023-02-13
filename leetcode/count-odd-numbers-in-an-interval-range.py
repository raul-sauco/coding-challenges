# 1523. Count Odd Numbers in an Interval Range
# 🟢 Easy
#
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
#
# Tags: Math

import timeit


# Count the number of elements between the low and the high, for even
# length series, the number of odd values will be half the length, for
# odd length series, we need to check if they start in an odd or even
# value, if they start in an odd value, it will be the result of the
# integer division by the length plus one.
#
# Time complexity: O(1) - We perform an addition, division and modulus
# operations.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 31 ms Beats 71.9%
# Memory 13.8 ms Beats 95.7%
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        size = high - low + 1
        if size % 2 == 0 or low % 2 == 0:
            return size // 2
        return size // 2 + 1


def test():
    executors = [Solution]
    tests = [
        [3, 7, 3],
        [2, 5, 2],
        [2, 4, 1],
        [1, 3, 2],
        [8, 10, 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countOdds(t[0], t[1])
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
