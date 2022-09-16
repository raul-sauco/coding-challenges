# 1770. Maximum Score from Performing Multiplication Operations
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
#
# Tags: Array - Dynamic Programming

import timeit
from functools import cache
from typing import List

# 1 call
# » Recursive           2.01183   seconds
# » MemoizedRecursive   0.00018   seconds


# The brute force solution is to recursively explore all possibilities.
#
# Time complexity: O(2^m) - Where m is the length of the multiplier
# array and it is bounded to 1000.
# Space complexity: O(m) - The height of the call stack will equal the
# size of the multiplier array, maxing out at 1000.
#
# This solution would probably fail with Time Limit Exceeded.
#
# This implementation is the same as the Memoized version removing
# the caching mechanism.


# We can reduce the time complexity if we cache intermediate results
# taking into account the left and right-most elements that we have
# already used.
#
# Time complexity: O(m^2) - We calculate the result of each 2 values of
# left and right pointers once and keep the max, both values can vary in
# the range 0..m.
# Space complexity: O(m) - The height of the call stack will equal the
# size of the multiplier array, maxing out at 1000.
#
# This solution fails with Time Limit Exceeded.
class MemoizedRecursive:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Define a recursive function that returns the maximum score
        # that can be obtained from a portion of the input.
        @cache
        def dfs(l: int, r: int) -> int:
            # Compute the current index we are accessing in the
            # multipliers array.
            idx = l + (len(nums) - r - 1)
            # Base case, this is the last value in multipliers.
            if idx == len(multipliers) - 1:
                # Take the best of the two available options.
                return max(
                    multipliers[idx] * nums[l], multipliers[idx] * nums[r]
                )
            else:
                # Return the best of the two possible branch results.
                return max(
                    multipliers[idx] * nums[l] + dfs(l + 1, r),
                    multipliers[idx] * nums[r] + dfs(l, r - 1),
                )

        # Initial call.
        return dfs(0, len(nums) - 1)


# The iterative bottom-up approach is to compute intermediate results
# starting at the left of multipliers and saving them into a 2D array
# or a tuple-indexed dictionary.
#
# Time complexity: O(m^2) - We iterate over the pairs (0..m, 0..m)
# Space complexity: O(m^2) - The dictionary can grow to size O(m^2)
#
# Runtime: 6825 ms, faster than 72.67%
# Memory Usage: 124.1 MB, less than 5.05%
class BottomUpDP:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Store the best result found.
        res = float("-inf")
        # Use a dictionary to save intermediate results. Keys are tuples
        # (i, j) of the best result possible for combinations of having
        # the first i positions from the left and the first j positions
        # from the right.
        dp = {(0, 0): 0}
        # Iterate over the range 1..len(multipliers)
        for idx in range(len(multipliers)):
            mul = multipliers[idx]
            # Iterate over all the possibilities of the next dp position.
            for i in range(idx + 2):
                j = idx + 1 - i
                # The optimal solution for this subproblem is the best
                # between the optimal solution to the i-1 subproblem
                # picking the left element or the j+1 solution picking
                # the right element.
                dp[(i, j)] = max(
                    dp[(i - 1, j)] + mul * nums[i - 1] if i else float("-inf"),
                    dp[(i, j - 1)] + mul * nums[-j] if j else float("-inf"),
                )
                # When on the last external loop update the best result.
                if idx == len(multipliers) - 1 and dp[(i, j)] > res:
                    res = dp[(i, j)]
        return res


# We can optimize the space complexity of the previous algorithm once
# we realize that we ever only need a maximum of m precomputed values
# to calculate the next row.
# TODO:- fix this solution, currently is not working, indexing nums is wrong.
class BottomUpDPOptimized:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # The dynamic programming intermediate results.
        dp = [0] * len(multipliers)
        # Iterate over the number of operations we have to perform.
        for ops in range(len(multipliers)):
            # Make a copy of dp.
            last = dp.copy()
            mul = multipliers[ops]
            # Iterate over all the possibilities of the next dp position.
            for i in range(ops + 2):
                if not i:
                    dp[i] = last[i] + mul * nums[i + ops]
                elif i == ops + 1:
                    dp[i] = last[i - 1] + mul * nums[ops - i]
                else:
                    dp[i] = max(
                        last[i] + mul * nums[i + ops],
                        last[i - 1] + mul * nums[ops - i],
                    )
        return dp[0]


def test():
    executors = [
        MemoizedRecursive,
        BottomUpDP,
        # BottomUpDPOptimized,
    ]
    tests = [
        # [[1], [1], 1],
        # [[1, 2, 3], [3, 2, 1], 14],
        [[-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6], 102],
        [
            [
                555,
                526,
                732,
                182,
                43,
                -537,
                -434,
                -233,
                -947,
                968,
                -250,
                -10,
                470,
                -867,
                -809,
                -987,
                120,
                607,
                -700,
                25,
                -349,
                -657,
                349,
                -75,
                -936,
                -473,
                615,
                691,
                -261,
                -517,
                -867,
                527,
                782,
                939,
                -465,
                12,
                988,
                -78,
                -990,
                504,
                -358,
                491,
                805,
                756,
                -218,
                513,
                -928,
                579,
                678,
                10,
            ],
            [
                783,
                911,
                820,
                37,
                466,
                -251,
                286,
                -74,
                -899,
                586,
                792,
                -643,
                -969,
                -267,
                121,
                -656,
                381,
                871,
                762,
                -355,
                721,
                753,
                -521,
            ],
            6861161,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maximumScore(t[0], t[1])
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
