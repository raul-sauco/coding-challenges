# 213. House Robber II
# 🟠 Medium
#
# https://leetcode.com/problems/house-robber-ii/
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List


# Very similar problem to LeetCode 198. House Robber, we only have to take into consideration the fact that the
# first and last houses are connected. That means that we have to choose one or the other. We can compute
# the best result if we take the first house, and leave the last one out, then the best if we leave the first
# house out, and take the first one, and select the best between them.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - We use a constant amount of memory.
#
# Runtime: 65 ms, faster than 14.31% of Python3 online submissions for House Robber II.
# Memory Usage: 13.8 MB, less than 98.12% of Python3 online submissions for House Robber II.
class TopDownDP:
    def rob(self, nums: List[int]) -> int:
        # Base case where we have less than 4 houses, we can only pick one.
        if len(nums) < 4:
            return max(nums)

        loot1 = loot2 = loot3 = loot4 = 0
        for i, n in enumerate(nums):
            if i != 0:
                # Skip the first house.
                loot1, loot2 = loot2, max(n + loot1, loot2)
            if i != len(nums) - 1:
                # Skip the last house.
                loot3, loot4 = loot4, max(n + loot3, loot4)

        # Pick the best option.
        return max(loot2, loot4)


# The memoized solution has a higher theoretical complexity but it performs better on the LeetCode tests.
# Locally it is slower than the DP solution, which makes more sense.
#
# Runtime: 34 ms, faster than 91.07% of Python3 online submissions for House Robber II.
# Memory Usage: 14.1 MB, less than 6.16% of Python3 online submissions for House Robber II.
class Memoized:
    def rob(self, nums: List[int]) -> int:
        # Base case where we have less than 4 houses, we can only pick one.
        if len(nums) < 4:
            return max(nums)

        # Otherwise return the best of the two options.
        return max(self.houseRobberI(nums[: len(nums) - 1]), self.houseRobberI(nums[1:]))

    def houseRobberI(self, nums):
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return memo[i]

        memo = {}
        return dp(len(nums) - 1)


def test():
    executors = [
        TopDownDP,
        Memoized,
    ]
    tests = [
        [[1], 1],
        [[2, 3, 2], 3],
        [[1, 2, 3, 1], 4],
        [[1, 2, 3], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.rob(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
