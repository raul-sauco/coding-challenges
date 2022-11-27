# 446. Arithmetic Slices II - Subsequence
# 🔴 Hard
#
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
#
# Tags: Array - Dynamic Programming

import timeit
from collections import defaultdict
from functools import cache
from typing import List, Optional


# Recursively build all the subsequences of the array as long as they
# are arithmetic.
#
# Time complexity: O(2^n) - The recursive tree can branch into two at
# each level.
# Space complexity: O(n) - The call stack will reach n levels.
#
# This solution fails with Time Limit Exceeded.
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # A helper function that takes in the next index on the input
        # array that we need to explore, the last value in the sequence
        # that we are building and the difference in the arithmetic
        # sequence that we need to maintain.
        @cache
        def dfs(
            i: int, l: int, last: Optional[int], diff: Optional[int]
        ) -> int:
            # Base case, we built a sequence.
            if i == len(nums):
                return 1 if l > 2 else 0
            # Base case, the sequence does not have any elements yet.
            if last is None:
                # Skip and use.
                return dfs(i + 1, l, None, None) + dfs(
                    i + 1, l + 1, nums[i], None
                )
            # Base case, the sequence only has one element.
            if diff is None:
                # Skip and use.
                return dfs(i + 1, l, last, None) + dfs(
                    i + 1, l + 1, nums[i], nums[i] - last
                )
            # We have at least two elements, check if this element
            # would follow the arithmetic sequence.
            if nums[i] - last == diff:
                # Skip and use.
                return dfs(i + 1, l, last, diff) + dfs(
                    i + 1, l + 1, nums[i], diff
                )
            # If adding this number would break the sequence, skip it.
            return dfs(i + 1, l, last, diff)

        return dfs(0, 0, None, None)


# We iterate over all pairs of numbers in the input computing their
# difference, for each array element, we have a dictionary of
# sequences that end at the given element keyed by the sequence
# arithmetic difference. If the difference between the current elements
# is in the dictionary of the left element, it means that there are that
# many sequences with that difference that end up at that number, and
# we can extend them by adding the element under the right pointer.
#
# Time complexity: O(n^2) - We visit each pair of elements in the input.
# Space complexity: O(n^2) - For each element in the input, we store a
# maximum of n entries in the dictionary at its position in dp.
#
# Runtime: 1712 ms, faster than 66.46%
# Memory Usage: 52.4 MB, less than 81.71%
class DP:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        res = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                # The number of previous subsequences to which we could
                # add the value nums[i]
                count = dp[j][diff] if diff in dp[j] else 0
                dp[i][diff] += count + 1
                res += count
        return res


def test():
    executors = [
        Solution,
        DP,
    ]
    tests = [
        [[2, 2, 3, 4], 2],
        [[2, 4, 6, 8, 10], 7],
        [[7, 7, 7, 7, 7], 16],
        [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            4194050,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numberOfArithmeticSlices(t[0])
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
