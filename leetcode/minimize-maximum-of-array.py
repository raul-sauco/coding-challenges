# 2439. Minimize Maximum of Array
# 🟠 Medium
#
# https://leetcode.com/problems/minimize-maximum-of-array/
#
# Tags: Array - Binary Search - Dynamic Programming - Greedy - Prefix Sum

import timeit
from itertools import accumulate
from math import ceil
from typing import List


# Iterate over the array from left to right keeping the sum of
# values 0..i, at that point, at any point we can move values to the
# left, but never to the right, for any given i, the maximum value of
# the subarray at that point will be the ceiling of the average of the
# values on 0..i, the result will be the maximum of all the subarray
# maximums.
#
# Time complexity: O(n) - We iterate over all elements and do O(1) work
# for each.
# Space complexity: O(1) - We store three integers.
#
# Runtime 756 ms Beats 91.3%
# Memory 26.1 MB Beats 84.30%
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        subarray_sum, res = 0, 0
        for i in range(len(nums)):
            subarray_sum += nums[i]
            # Using max is slower on leetcode tests.
            # res = max(res, ceil(subarray_sum / (i + 1)))
            subarray_max = ceil(subarray_sum / (i + 1))
            if subarray_max > res:
                res = subarray_max
        return res


# Same logic as the previous solution but an interesting way of
# implementing that logic, credits to @Lee215
# https://leetcode.com/problems/minimize-maximum-of-array/solutions/2706521/
#
# Time complexity: O(n) - We iterate over all elements and do O(1) work
# for each.
# Space complexity: O(1) - We store three integers.
#
# Runtime 759 ms Beats 90.13%
# Memory 26.8 MB Beats 39.46%
class UseAccumulate:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max((x + i) // (i + 1) for i, x in enumerate(accumulate(nums)))


def test():
    executors = [
        Solution,
        UseAccumulate,
    ]
    tests = [
        [[10, 1], 10],
        [[3, 7, 1, 6], 5],
        [[6, 9, 3, 8, 14], 8],
        [[13, 13, 20, 0, 8, 9, 9], 16],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimizeArrayValue(t[0])
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
