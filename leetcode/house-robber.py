# 198. House Robber
# 🟠 Medium
#
# https://leetcode.com/problems/house-robber/
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List

# 1e4 calls:
# » BruteForce          0.09572   seconds
# » MemoizedDFS         0.0783    seconds
# » TopDownDP           0.02946   seconds
# » TwoVariables        0.02686   seconds

# For either house, we choose to take it, and skip the next one, or to
# skip it, leaving us free to take the next one. We can start designing
# the brute force solution.
#
# Time complexity: O(2^n) - For each element in the input array, we can
# make two decisions.
# Space complexity: O(2^n) - The call stack will grow to accommodate 2
# calls per each item in nums.
#
# This solution would fail with Time Limit Exceeded. Even so, we can use
# it as a building block for better solutions because it will help us
# decide the steps needed to solve the problem without introducing any
# extra complexity.
class BruteForce:
    def rob(self, nums: List[int]) -> int:
        # Define a recursive function that returns the best result of
        # stealing from the houses from an index forward.
        def dfs(houses: List[int]) -> int:
            # Base cases, if we have no houses left to visit, return 0.
            if not houses:
                return 0
            # If we only have one house, return its value.
            if len(houses) == 1:
                return houses[0]
            # Otherwise, call the function for the two options that we
            # have at the current position:
            # - We can rob this house, add its value to the counter and
            #   calculate the best of the array left after
            #   we remove this house and the next.
            # - We can skip this house and return the best of the array
            #   left after removing it.
            # Return the best result.
            return max(houses[0] + dfs(houses[2:]), dfs(houses[1:]))

        return dfs(nums)


# We can replicate the logic of the brute force solution, but memoize
# partial results. To make memoization easier, instead of slicing the
# array on each call, we can pass the index of the house at which we
# want to start checking.
#
# Time complexity: O(n) - We only calculate the best results once per
# index of nums.
# Space complexity: O(n) - The call stack can only have n calls on it.
#
# Runtime: 37 ms, faster than 82.80%
# Memory Usage: 13.9 MB, less than 19.08%
class MemoizedDFS:
    def rob(self, nums: List[int]) -> int:
        # Store partial results in a dictionary indexed by the position
        # of the house that we are deciding to rob or not at that place
        # on the decision tree.
        memo = {}
        # Define a recursive function that returns the best result of
        # stealing from the houses from an index forward.
        def dfs(idx: int) -> int:
            # If we have calculated this value before, return it.
            if idx in memo:
                return memo[idx]
            # Base cases, if we have no houses left to visit, return 0.
            if idx == len(nums):
                return 0
            # If we only have one house, return its value.
            if idx == len(nums) - 1:
                return nums[-1]
            # Otherwise, call the function for the two options that we
            # have at the current position:
            # - We can rob this house, add its value to the counter and
            #   calculate the best of the array left after
            #   we remove this house and the next.
            # - We can skip this house and return the best of the array
            #   left after removing it.
            # Return the best result.
            result = max(nums[idx] + dfs(idx + 2), dfs(idx + 1))
            memo[idx] = result
            return result

        return dfs(0)


# We can apply the same idea, as in the brute force solution, to
# calculate if we would get the best profit by robbing, or skipping a
# house, but use dynamic programming instead of recursion. The previous
# solutions gave us a clue to the fact that we can determine the max we
# can rob by either taking the house and the accumulated total skipping
# the next house or by skipping the current house and taking the
# accumulated total at the next house.
#
# best[i] = max(nums[i] + best[i + 2], best[i + 1])
#
# We can easily build a bottom-up dynamic programming solution based on
# that. In this particular problem, it is easy to turn it around to
# obtain a top-down solution as well:
#
#   best[i] = max(nums[i] + best[i-2], best[i-1])
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - We can use the input array to calculate.
#
# Runtime: 24 ms, faster than 99.53%
# Memory Usage: 14 MB, less than 20.34%
class TopDownDP:
    def rob(self, nums: List[int]) -> int:
        # Edge cases
        if len(nums) < 3:
            return max(nums)
        # At index 0 we don't have any choices, at index one we either
        # take house 0 or 1:
        nums[1] = max(nums[0], nums[1])
        # At any other index, decide if it is better to rob the house or
        # not rob it.
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[-1]


# We can improve on the top-down solution by storing the most amount of
# loot in two variables instead of updating the values on the input array.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - We use a constant amount of memory.
#
# Runtime: 29 ms, faster than 97.15%
# Memory Usage: 13.8 MB, less than 97.62%
class TwoVariables:
    def rob(self, nums: List[int]) -> int:
        loot1 = loot2 = 0
        for n in nums:
            loot1, loot2 = loot2, max(n + loot1, loot2)
        return loot2


def test():
    executors = [
        BruteForce,
        MemoizedDFS,
        TopDownDP,
        TwoVariables,
    ]
    tests = [
        [[0, 0], 0],
        [[0, 1], 1],
        [[2, 1, 1, 2], 4],
        [[1, 2, 3, 1], 4],
        [[2, 7, 9, 3, 1], 12],
        [[1, 1, 18, 1, 1, 18], 37],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.rob([*t[0]])
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
