# 2389. Longest Subsequence With Limited Sum
# 🟢 Easy
#
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/
#
# Tags: Array - Binary Search - Greedy - Sorting - Prefix Sum

import timeit
from bisect import bisect_right
from itertools import accumulate
from typing import List


# Create an array of prefix sums of the sorted input nums, result[i]
# will be the index at which we would need to insert that value on the
# prefix sum array to maintain the sorted order. What the algorithm does
# is to greedily pick the highest number of values that gives the lowest
# possible subsequence sum, then use binary search to determine how
# many values we can take while remaining below the given sum value.
#
# Time complexity: O(n*log(n) + k*log(n)) - Where n is the number of
# elements in the nums array and k is the number of queries, we need to
# sort the array nums in n*log(n) time, and compute the prefix sums in
# O(n), then, for each query k, we use binary search in O(log(n)) time
# to find the minimum number of values we can sum while still remaining
# below the query value.
# Space complexity: O(n) - The prefix sum array has the same size as the
# nums array.
#
# Runtime 99 ms Beats 98.35%
# Memory 14.1 MB Beats 79.61%
class Pythonic:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix_sums = [ps for ps in accumulate(sorted(nums))]
        return [bisect_right(prefix_sums, query) for query in queries]


# Same logic as the previous solution but avoiding the use of any
# libraries.
#
# Time complexity: O(n*log(n) + k*log(n)).
# Space complexity: O(n).
#
# Runtime 118 ms Beats 90.49%
# Memory 14.1 MB Beats 79.61%
class Custom:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix_sums, n, m = sorted(nums), len(nums), len(queries)
        for i in range(1, n):
            prefix_sums[i] += prefix_sums[i - 1]
        res = [None] * m
        for i in range(m):
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if prefix_sums[mid] <= queries[i]:
                    l = mid + 1
                else:
                    r = mid
            res[i] = l
        return res


def test():
    executors = [
        Pythonic,
        Custom,
    ]
    tests = [
        [[2, 3, 4, 5], [1], [0]],
        [[4, 5, 2, 1], [3, 10, 21], [2, 3, 4]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.answerQueries(t[0], t[1])
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
