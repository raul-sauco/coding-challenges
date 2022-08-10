# 416. Partition Equal Subset Sum
# 🟠 Medium
#
# https://leetcode.com/problems/partition-equal-subset-sum/
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List


# To be able to partition into two equal subsets, we can compute the
# half-sum of the values and try to get an arrangement of elements that
# adds to that value. If we can manage to do that, we can partition into
# two equal subsets, because the remaining elements will also add to
# the half-sum. We can sort the array in reverse order and start
# iterating over the values. If we see any value bigger than target, we
# return false, otherwise we add this value to the number of possible
# sums we can make with the elements we have seen.
#
# Time complexity: O(n^2) - We visit each element and, for each we
# compute the sum of adding this value to all sums we have seen before.
# Space complexity: O(s) - We store a list in the range [0..target]
#
# Runtime: 580 ms, faster than 78.96%
# Memory Usage: 14.1 MB, less than 86.61%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # We are trying to find an array that adds up to half the sum.
        target, m = divmod(total, 2)
        # If the half-sum is not an integer, we cannot partition.
        if m != 0:
            return False
        # Store computed values in an array.
        dp = [0] + [False] * target
        # Sort the array in O(n*log(n))
        nums.sort(reverse=True)
        # If any value is bigger that target, return False.
        if nums[0] > target:
            return False
        for num in nums:
            # Compute the possible sums adding this value to the ones
            # that we have seen already. Compute in reverse order to
            # avoid using values computed on this loop.
            for i in range(target - num, 0, -1):
                if dp[i]:
                    # We can sum to dp[i + num]
                    dp[i + num] = True
            # We can sum to this value, using this number alone.
            dp[num] = True
            # If we can sum to target, return True now
            if dp[target]:
                return True
        # If we couldn't sum to target, return False.
        return False


def test():
    executors = [Solution]
    tests = [
        # [[1, 5, 11, 5], True],
        # [[1, 2, 3, 5], False],
        [[2, 2, 3, 5], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.canPartition(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
