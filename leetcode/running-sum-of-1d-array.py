# 1480. Running Sum of 1d Array
# 🟢 Easy
#
# https://leetcode.com/problems/running-sum-of-1d-array/
#
# Tags: Array - Prefix Sum

import timeit
from typing import List


# Iterate over the elements in the input computing the prefix sum.
#
# Time complexity: O(n) - We visit each element and do constant work for each.
# Space complexity: O(1) - We use constant extra space.
#
# Runtime 95 ms Beats 6.24%
# Memory 14.1 MB Beats 25.39%
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            nums[i] = sum
        return nums


# Similar logic to the previous solution but mutate the input array.
#
# Time complexity: O(n) - We visit each element and do constant work for each.
# Space complexity: O(1) - We use constant extra space.
#
# Runtime 97 ms Beats5.37%
# Memory 13.9 MB Beats 92.56%
class InPlace:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


def test():
    executors = [
        Solution,
        InPlace,
    ]
    tests = [
        [[1, 2, 3, 4], [1, 3, 6, 10]],
        [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5]],
        [[3, 1, 2, 10, 1], [3, 4, 6, 16, 17]],
        [[1, 1, 8, -90, 1], [1, 2, 10, -80, -79]],
        [[], []],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.runningSum([*t[0]])
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
