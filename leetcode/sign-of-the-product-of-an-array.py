# 1822. Sign of the Product of an Array
# 🟢 Easy
#
# https:#leetcode.com/problems/sign-of-the-product-of-an-array/
#
# Tags: Array - Math

import timeit
from typing import List


# Iterate over the input values, if we see a 0, return 0, otherwise xor
# the sign with the boolean result of checking if the current number is
# negative.
#
# Time complexity: O(n) - We visit all values and do O(1) work for each.
# Space complexity: O(1) - We use one boolean of extra memory.
#
# Runtime 80 ms Beats 5.64%
# Memory 16.4 MB Beats 7.53%
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = False
        for num in nums:
            if not num:
                return 0
            neg ^= num < 0
        return -1 if neg else 1


def test():
    executors = [Solution]
    tests = [
        [[1, 5, 0, 2, -3], 0],
        [[-1, 1, -1, 1, -1], -1],
        [[-1, -2, -3, -4, 3, 2, 1], 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.arraySign(t[0])
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
