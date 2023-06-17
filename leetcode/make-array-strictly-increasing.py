# 1187. Make Array Strictly Increasing
# 🔴 Hard
#
# https://leetcode.com/problems/make-array-strictly-increasing/
#
# Tags: Array - Binary Search - Dynamic Programming - Sorting

import timeit
from bisect import bisect_right
from collections import defaultdict
from typing import List


# If we sort the second array, then we can iterate over the first array
# and, for each value that breaks the increasing sequence, we can check
# what is the smallest value in arr2 that we can change it to in log(n)
# if we use binary search.
#
# Time complexity: O(m*n*log(n)) - We iterate over all the values in
# arr1, for each, we iterate each value in dp, which could have a max
# length of n, for each inner loop iteration, we binary search the
# smallest value that we can use in arr2.
# Space complexity: O(n) - Both the dp and next_dp dictionary can hold
# n entries.
#
# Runtime 576 ms Beats 86.15%
# Memory 16.7 MB Beats 74.62%
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        vals = list(set(arr2))
        vals.sort()
        dp = {-1: 0}
        m, n = len(arr1), len(vals)
        for i in range(m):
            next_dp = defaultdict(lambda: 1_000_000_001)
            for prev in dp:
                if arr1[i] > prev:
                    next_dp[arr1[i]] = min(next_dp[arr1[i]], dp[prev])
                idx = bisect_right(vals, prev)
                if idx < n:
                    next_dp[vals[idx]] = min(next_dp[vals[idx]], 1 + dp[prev])
            dp = next_dp
        return min(dp.values()) if dp else -1


def test():
    executors = [Solution]
    tests = [
        [[1, 5, 3, 6, 7], [4, 3, 1], 2],
        [[1, 5, 3, 6, 7], [1, 3, 2, 4], 1],
        [[1, 5, 3, 6, 7], [1, 6, 3, 3], -1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.makeArrayIncreasing(t[0], t[1])
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
