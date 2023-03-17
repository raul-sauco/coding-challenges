# 303. Range Sum Query - Immutable
# 🟢 Easy
#
# https://leetcode.com/problems/range-sum-query-immutable/
#
# Tags: Array - Design - Prefix Sum

import timeit
from itertools import accumulate
from typing import List


# Create an array of sums. When a range sum is requested, fetch it
# from Sum(right - left).
#
# Time complexity: O(n) - To create the prefix sum array, O(1) to
# calculate the range sums on sumRange() calls.
# Space complexity: O(n) for the prefix sum array.
#
# Runtime 76 ms Beats 90.39%
# Memory 17.7 MB Beats 59.83%
class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (self.sums[left - 1] if left > 0 else 0)


# Similar idea but use a zero padded sums array instead of checking if
# the value is positive when computing the sum.
#
# Runtime 72 ms Beats 96.72%
# Memory Usage 17.7 MB Beats 25.94%
class ZeroPadded:
    def __init__(self, nums: List[int]):
        self.sums = list(accumulate([0] + nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]


def test():
    executors = [
        NumArray,
        ZeroPadded,
    ]
    tests = [
        [
            [2],
            {
                2: [0, 0],
            },
        ],
        [
            [-2, 0, 3, -5, 2, -1],
            {
                1: [0, 2],
                -1: [2, 5],
                -3: [0, 5],
                -1: [5, 5],
            },
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor(t[0])
                for sum in t[1]:
                    result = sol.sumRange(*t[1][sum])
                    exp = sum
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
