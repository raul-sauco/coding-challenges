# 1569. Number of Ways to Reorder Array to Get Same BST
# 🔴 Hard
#
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
#
# Tags: Array - Divide and Conquer - Dynamic Programming - Tree - Union Find
# - Binary Search Tree - Memoization - Combinatorics - Binary Trees

import timeit
from math import comb
from typing import List


# Use the first value in the array as the root of the subtree, then
# recursively call the function with the values that will fall into the
# left and right sub-tree, adjust the combination of the results with
# the ways we can intermingle values from the right and left subtrees.
#
# Time complexity: O(n^2) - Each call we iterate all the remaining
# values, the values decrease by 1 in each call.
# Space complexity: O(n) - The height of the call stack, in each call it
# decreases by 1.
#
# Runtime  ms Beats %
# Memory  MB Beats %
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 1_000_000_007

        def dfs(nums):
            if len(nums) < 3:
                return 1
            left = [x for x in nums if x < nums[0]]
            return (
                dfs(left)
                * dfs([x for x in nums if x > nums[0]])
                * comb(len(nums) - 1, len(left))
                % mod
            )

        return (dfs(nums) - 1) % mod


def test():
    executors = [Solution]
    tests = [
        [[2, 1, 3], 1],
        [[3, 4, 5, 1, 2], 5],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numOfWays(t[0])
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
