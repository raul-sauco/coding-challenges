# 523. Continuous Subarray Sum
# 🟠 Medium
#
# https://leetcode.com/problems/continuous-subarray-sum/
#
# Tags: Array - Hash Table - Math - Prefix Sum

import timeit
from typing import List


# Compute the prefix sums then iterate over each combination of two
# indexes checking if the sum of values between them is a multiple of k.
#
# Time complexity: O(n^2) - We iterate over all the combinations of two
# indexes.
# Space complexity: O(n) - The prefix sum array has the same length as
# the input.
#
# This solution fails with Time Limit Exceeded.
class Naive:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Compute an array of prefix sums.
        pre = [nums[0]] + ([0] * (len(nums) - 1))
        for i in range(1, len(nums)):
            pre[i] = nums[i] + pre[i - 1]
        # Iterate over all pairs of two indexes.
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                range_sum = pre[j]
                if i > 0:
                    range_sum -= pre[i - 1]
                if range_sum % k == 0:
                    return True
        return False


# Iterate over the input computing the cumulative sum up to the current
# index, calculate sum[0:i] % k and store the result in a hashmap, if we
# ever find a repeated value, the sum of values between the indexes that
# resulted in the same remainder will be a multiple of k.
#
# Time complexity: O(n) - We iterate over the array once.
# Space complexity: O(k) - The hashmap holds the result of mod K
# operations so it can grow at most to size k.
#
# Runtime: 1563 ms, faster than 71.44%
# Memory Usage: 33.3 MB, less than 39.30%
class UseHashMap:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Use a hashmap. Initialize it with a zero to represent the sum
        # of values at the index left of 0.
        seen = {0: 0}
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            rem = current_sum % k
            if rem % k not in seen:
                seen[rem] = i + 1
            # If we have seen this sum in a previous index.
            elif seen[rem] < i:
                return True
        return False


def test():
    executors = [
        Naive,
        UseHashMap,
    ]
    tests = [
        [[0], 1, False],
        [[10], 10, False],
        [[5, 10, 35], 10, True],
        [[23, 2, 4, 6, 7], 6, True],
        [[23, 2, 4, 6, 6], 7, True],
        [[23, 2, 6, 4, 7], 6, True],
        [[23, 2, 6, 4, 7], 13, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.checkSubarraySum(t[0], t[1])
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
