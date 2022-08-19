# 45. Jump Game II
# 🟠 Medium
#
# https://leetcode.com/problems/jump-game-ii/
#
# Tags: Array - Dynamic Programming - Greedy

import timeit
from typing import List


# The brute force solution would explore all possibilities, from each
# position, take all possible jumps, once we get to the end, compare
# that result to the best found so far.
#
# Time complexity: O(2^n) - For each option we explore all possibilities
# it amounts to choosing to take, or not, each element of the array.
# Space complexity: O(n) - The call stack can grow to the depth of the
# input array.
#
# This solution would fail with Time Limit Exceeded.
class BruteForceDFS:
    def jump(self, nums: List[int]) -> int:
        # Store the current shortest number of jumps found.
        self.best = float("inf")
        # Define a function that explores jumps from a given position.
        # It receives the index of the position that is exploring and
        # returns the minimum number of jumps to get from that position
        # to the end of the array.
        def dfs(idx: int) -> int:
            # Base case, we are at the end of the array.
            if idx == len(nums) - 1:
                return 0
            # Base case, if the element at the current index is 0, we
            # will not be able to reach the end from here.
            if nums[idx] == 0:
                return float("inf")
            # Explore the result of all options if the jump would keep
            # us within the bounds of the array.
            jumps = [
                dfs(idx + j)
                for j in range(1, nums[idx] + 1)
                if idx + j < len(nums)
            ]
            # We keep the best option out of all of them and add the
            # jump needed to get there to the result.
            return min(jumps) + 1

        # Initial call.
        return dfs(0)


# We can improve the previous solution if we avoid recalculating the
# best result from an index once we have calculated it, we could use
# functools.cache for that, which would be more efficient, or manually
# keep results in a dictionary.
#
# Time complexity: O(n^2) - We calculate all possibilities from each
# index once.
# Space complexity: O(n) - We store an array of length n.
#
# This solution would fail with Time Limit Exceeded because there is a
# better one.
class MemoizedDFS:
    def jump(self, nums: List[int]) -> int:
        # Store results already calculated in an array, it could also be
        # a dictionary, but we can use the fact that the key would be
        # the index of an array of known length.
        memo = [None] * len(nums)
        memo[-1] = 0
        # Define a function that explores jumps from a given position.
        # It receives the index of the position that is exploring and
        # returns the minimum number of jumps to get from that position
        # to the end of the array.
        # @cache would be more efficient than the dictionary.
        def dfs(idx: int) -> int:
            # Use the memoized result if existing.
            if memo[idx] is not None:
                return memo[idx]
            # Base case, we are at the end of the array.
            if idx == len(nums) - 1:
                return 0
            # Base case, if the element at the current index is 0, we
            # will not be able to reach the end from here.
            if nums[idx] == 0:
                memo[idx] = float("inf")
                return memo[idx]
            # Explore the result of all options if the jump would keep
            # us within the bounds of the array.
            memo[idx] = (
                min(
                    [
                        dfs(idx + j)
                        for j in range(1, nums[idx] + 1)
                        if idx + j < len(nums)
                    ]
                )
                + 1
            )
            # We keep the best option out of all of them and add the
            # jump needed to get there to the result.
            return memo[idx]

        # Initial call.
        return dfs(0)


# The bottom-up DP version of the previous solution starts at the first
# index and "jumps" to all the possible positions checking if the result
# of jumping there from the current position is better than the best
# option explored so far.
#
# Time complexity: O(n^2) - This solution is not more effective than the
# memoized solution, we still explore every possible jump from the
# position that we are visiting.
# Space complexity: O(n) - The size of the DP array.
#
# This solution would probably fail with Time Limit Exceeded.
class DP:
    def jump(self, nums: List[int]) -> int:
        dp = [0] + [float("inf")] * (len(nums) - 1)
        # Iterate over the input taking all possible "jumps".
        for i in range(len(nums)):
            # Calculate the result of all possible jumps.
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    # If taking this jump would reduce the number of jumps
                    # to get to i+j, that is the best jump seen so far.
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        # Return the best jump to get to the end of the array.
        return dp[-1]


# Visit each element of the array but do it in groups, we can see it as
# treating each group as a level and the algorithm as BFS. For each
# level, keep track of the farthest position we could jump to from this
# level. When we get to the end of the level, add one to the number of
# jumps that we have taken, and update the current level by updating the
# last element we can explore to match the farthest element we can
# reach from this level.
# The algorithm repeatedly calculates the farthest point we can reach
# from any of the positions that we can reach given the current number
# of jumps, then "jump" once more and continue calculating. Each element
# is only explored once.
#
# Time complexity: O(n) - Each element is visited once.
# Space complexity: O(1) - Constant space.
#
# Runtime: 155 ms, faster than 84.71%
# Memory Usage: 15.1 MB, less than 59.64%
class Greedy:
    def jump(self, nums: List[int]) -> int:
        # Store the number of jumps we have taken, the farthest we can
        # jump right now and the last index of the window we are
        # exploring in this jump.
        jumps = current_end = current_farthest = 0
        # Iterate over the input except the last element.
        for i in range(len(nums) - 1):
            # The farthest we can jump is the max of the current
            # farthest we have seen and the current jump.
            current_farthest = max(current_farthest, i + nums[i])
            # If we are at the current end, we need to jump.
            if i == current_end:
                # We need to jump to keep exploring.
                jumps += 1
                # Greedily take (up to) the best jump we can make.
                current_end = current_farthest
        # Return minimum number of jumps to get to the end.
        return jumps


def test():
    executors = [
        BruteForceDFS,
        MemoizedDFS,
        DP,
        Greedy,
    ]
    tests = [
        [[2, 3, 1, 1, 4], 2],
        [[2, 3, 0, 1, 4], 2],
        [[2, 3, 0, 1, 4, 0, 0, 0, 2, 8, 7, 3], 5],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.jump(t[0])
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
