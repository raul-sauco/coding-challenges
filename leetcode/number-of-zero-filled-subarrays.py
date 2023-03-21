# 2348. Number of Zero-Filled Subarrays
# 🟠 Medium
#
# https://leetcode.com/problems/number-of-zero-filled-subarrays/
#
# Tags: Array - Sliding Window - Math

import timeit
from typing import List


# Use a for loop to iterate over the values, for each value, if we
# are in sequence, add the sequence length to the result.
#
# Time complexity: O(n) -  We visit each element once and do O(1) work.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 1090 ms Beats 76.32%
# Memory 24.5 MB Beats 78.9%
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l, res = 0, 0
        for r, num in enumerate(nums):
            if num:
                l = r + 1
            else:
                res += 1 + r - l
        return res


def test():
    executors = [Solution]
    tests = [
        [[2, 10, 2019], 0],
        [[0, 0, 0, 2, 0, 0], 9],
        [[1, 3, 0, 0, 2, 0, 0, 4], 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.zeroFilledSubarray(t[0])
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
