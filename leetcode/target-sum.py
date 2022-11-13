# 494. Target Sum
# 🟠 Medium
#
# https://leetcode.com/problems/target-sum/
#
# Tags: Array - Dynamic Programming - Backtracking

import timeit
from collections import Counter
from functools import cache
from typing import List


# Top down memoization solution using a dictionary as the memo object.
# each calls shifts the index one position forward and returns the
# result of the recursive call adding both the positive and negated
# value under the current pointer to the result.
#
# Time complexity: O(n^2) - We are avoiding calculating results that we
# have already stored in the memo, we will compute results for the same
# index and sum only once, there are approximately n^2 over the size of
# the nums input combinations of index and sum.
# Space complexity: O(n^2) - The memo will have one call for each of the
# possible combinations of index and current sum.
#
# Runtime: 973 ms, faster than 29.34%
# Memory Usage: 41.7 MB, less than 9.68%
class Memoization:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(i: int, sum: int) -> int:
            key = (i, sum)
            # Check the memo.
            if key in memo:
                return memo[key]
            # Stop this branch when we reach a leaf.
            if i == len(nums):
                memo[key] = int(sum == target)
                return memo[key]
            # Visit both branches.
            memo[key] = helper(i + 1, sum - nums[i]) + helper(
                i + 1, sum + nums[i]
            )
            return memo[key]

        return helper(0, 0)


# Similar solution to the memoization one but using functools cache
# instead of a manually managed dictionary.
#
# Time complexity: O(n^2)
# Space complexity: O(n^2)
#
# Runtime: 283 ms, faster than 88.90%
# Memory Usage: 41.8 MB, less than 8.12%
class MemoizationCache:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def helper(i: int, sum: int) -> int:
            # Stop this branch when we reach a leaf.
            if i == len(nums):
                return int(sum == target)
            # Visit both branches.
            return helper(i + 1, sum - nums[i]) + helper(i + 1, sum + nums[i])

        return helper(0, 0)


# 2D Dynamic programming solution.  We could use a 2D array of size n*t
# where n is the number of elements in the array nums and t is all the
# possible values that the sum could take, that is all the values
# between [-sum(nums), sum(nums)], each row represents the index of nums
# that we are visiting and each column represents a value, the cells
# represent how many different ways we have of arriving at that value.
# On each iteration, we use all the values on the previous row to
# compute the ways to calculate the values on the current row given the
# current value nums[i], we would return the value at index target on
# the last row.

# We can optimize the space usage of the proposed 2D Dynamic programming
# solution if we keep a dictionary of value: ways to sum up to it, then
# iterate over the items in nums, for each key in the dictionary, which
# represent a value that we could sum up on the previous iteration, we
# add its count to two values in the new dictionary, key+nums[i] and
# key-nums[i] because we could choose to add or subtract this value,
# then we update the dp dictionary with the values just computed before
# visiting the next index. The result is the value at index target after
# we visit all indexes.
#
# Time complexity: O(n*t) - Where n is the number of values in the input
# array nums and t is the number of values that the sum can take, or
# [-sum(nums)...sum(nums)].
# Space complexity: O(t) - Where t is the number of values that the sum
# can take, all values in [-sum(nums)...sum(nums)].
#
# Runtime: 304 ms, faster than 87.41%
# Memory Usage: 14.1 MB, less than 88.17%
class BottomUpLinkedIn:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = Counter([0])
        for num in nums:
            next = Counter()
            for key in dp.keys():
                next[key - num] += dp[key]
                next[key + num] += dp[key]
            dp = next
        return dp[target]


def test():
    executors = [
        Memoization,
        MemoizationCache,
        BottomUpLinkedIn,
    ]
    tests = [
        [[1], 1, 1],
        [[1, 1, 1, 1, 1], 3, 5],
        [
            [
                25,
                33,
                27,
                23,
                46,
                16,
                10,
                27,
                33,
                2,
                12,
                2,
                29,
                44,
                49,
                40,
                32,
                46,
                7,
                50,
            ],
            4,
            0,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findTargetSumWays(t[0], t[1])
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
