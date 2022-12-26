# 55. Jump Game
# 🟠 Medium
#
# https://leetcode.com/problems/jump-game/
#
# Tags: Array - Dynamic Programming - Greedy

import timeit
from typing import List


# Start at n=0 and explore the furthest position you can reach.
# Recursively explore the furthest position you can reach from there.
# If at any point you can reach the end of the array or further, return
# true, once all the possibilities have been explored, return false.
#
# Time complexity: O(n^2) - If the array contains small values and they
# fail towards the end, we will explore all combinations of values.
# Space complexity: O(n^2) - The call stack.
class BruteForce:
    def canJump(self, nums: List[int]) -> bool:
        def explore(n: int):
            if nums[n] + n >= len(nums) - 1:
                return True
            for i in range(nums[n], 0, -1):
                if explore(n + i):
                    return True
            return False

        return explore(0)


# Similar to the brute force algorithm but memorize positions that we
# have explored but do not lead to a solution. There is no need to
# memoize positions that return True because the True value propagates
# and terminates execution, returning True, as soon as the first one is
# found.
#
# Time complexity: O(n^2) - For each position, we may end up visiting
# each position after itself.
# Space complexity: O(n) - The dictionary could hold an entry for each
# element in nums.
#
# Runtime: 8078 ms, faster than 5.00%
# Memory Usage: 27.8 MB, less than 5.11%
class Memoization:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def explore(n: int):
            if n in memo:
                return memo[n]
            if nums[n] + n >= len(nums) - 1:
                return True
            for i in range(nums[n], 0, -1):
                if explore(n + i):
                    return True
            memo[n] = False
            return False

        return explore(0)


# Intuition: Mark the end of the array as our point to reach (goal) and
# start checking the positions before it. For each position, if we can
# reach the current goal from there i + nums[i] >= goal mark that
# position as the new goal and check if we can reach it from any of the
# previous positions.
#
# Time complexity: O(n) - We visit each position once.
# Space complexity: O(1) - Constant extra memory used.
#
# Runtime: 477 ms, faster than 97.37%
# Memory Usage: 15.2 MB, less than 82.53%
class Linear:
    def canJump(self, nums: List[int]) -> bool:
        # Initial goal, reaching the last position of the array.
        goal = len(nums) - 1
        # Iterate over all the positions except the last one.
        for i in range(len(nums) - 2, -1, -1):
            # If from the current position we can reach the current goal.
            if i + nums[i] >= goal:
                # Reaching this position becomes our current goal.
                goal = i
        # If our last goal is to reach the start position, we can jump
        # to the end.
        return goal == 0


# Front to back, store the index of the furthest position we can reach
# at any point, iterate over the input array positions, check if the
# current position could be reached, if it could not, return False, if
# it could, compare the best reach up to that point with the new reach
# we have from the current position and update it if better.
#
# Time complexity: O(n) - We visit each position once.
# Space complexity: O(1) - Constant extra memory used.
#
# Runtime: 477 ms Beats 95.93%
# Memory: 15.1 MB Beats 97.51%
class Greedy:
    def canJump(self, nums: List[int]) -> bool:
        # Store the maximum position we can reach from any index.
        reach, goal = 0, len(nums) - 1
        for i in range(len(nums)):
            # If we could not reach this index.
            if reach < i:
                return False
            # If we were able to reach this index.
            if (reach := max(reach, i + nums[i])) >= goal:
                return True


def test():
    executors = [
        BruteForce,
        Memoization,
        Linear,
        Greedy,
    ]
    tests = [
        [[0], True],
        [[1, 0], True],
        [[0, 1], False],
        [[2, 3, 1, 1, 4], True],
        [[10, 3, 1, 1, 4], True],
        [[3, 2, 1, 0, 4], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.canJump(t[0])
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
