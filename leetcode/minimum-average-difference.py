# 2256. Minimum Average Difference
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-average-difference/
#
# Tags: Array - Prefix Sum

import timeit
from typing import List

# Compute the sum of all array elements in O(1), then iterate over them
# keeping the sum of the left and right side to compute the left and
# right side averages and their differences. Return the index of the
# smallest difference found.
#
# Time complexity: O(n) - We iterate twice over the array elements.
# Space complexity: O(1) - We use constant space.
#
# Runtime: 991 ms, faster than 97.47%
# Memory Usage: 24.9 MB, less than 56.92%
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        res, ls, rs, n = (float("inf"), 0), 0, sum(nums), len(nums)
        for i, num in enumerate(nums):
            # Add and remove the current value from the sums.
            ls += num
            rs -= num
            # Compute the averages.
            la = ls // (i + 1)
            ra = rs // (n - i - 1) if i < n - 1 else 0
            avg = abs(la - ra)
            # Check if we need to update the minimum.
            if avg < res[0]:
                res = (avg, i)
        # Return the index of the best average.
        return res[1]


def test():
    executors = [Solution]
    tests = [
        [[0], 0],
        [[2, 5, 3, 9, 5, 3], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimumAverageDifference(t[0])
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
