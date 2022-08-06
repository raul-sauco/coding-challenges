# 377. Combination Sum IV
# 🟠 Medium
#
# https://leetcode.com/problems/combination-sum-iv/
#
# Tags: Array - Dynamic Programming

import timeit
from collections import defaultdict
from functools import cache
from typing import List


# The brute force approach splits each branch into n branches, with n
# being the input size len(nums) at each step. If at any point the
# result equals target, it adds one to the ways to calculate the result.
# If the sum of elements selected on the branch goes over the target, it
# stops working on that branch.
#
# Time complexity: O(n^t) - n is the number of values in the input and t
# is the target value because in the worst case it could be the height
# of the tree.
# Space complexity: O(n^t) - For the call stack, same as above.
#
# The brute force solution would probably fail with Time Limit Exceeded.
#
# We can easily convert this solution to a memoized solution caching
# the results, for example using functools.cache, though it would be
# possible to use a dictionary with target values as keys and number
# of results for that target value as values.
#
# Time complexity: O(t) - Since we are memoizing the result for each
# possible value that the current target could have, and the value can
# only be an integer, we will make at most t calls.
# Space complexity: O(t) - For the call stack, we will make at most t
# calls. If we used a dictionary, it would be a max of size t.
#
# Runtime: 47 ms, faster than 84.07%
# Memory Usage: 14.4 MB, less than 7.44%
class Memoized:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Define a function that calculates how many different ways
        # there are to combine the elements of nums to get a target.
        @cache
        def dfs(t: int) -> None:
            if t < 0:
                # We have gone over the target, this branch did not
                # lead to a result.
                return 0
            if t == 0:
                # The last value we computed lead to a match, return 1
                return 1
            # Return the sum of dfs on all the list elements.
            return sum([dfs(t - n) for n in nums])

        # Initial call
        return dfs(target)


# We can build the dynamic programming bottom-up if we iterate over each
# value current target (ct) from 1..target. For each value ct, we
# iterate over all nums where num <= ct, and assign
#
# dp[ct] += dp[ct - num]
#
# The ways to get to the current target ct are all the ways we have
# found previously, plus how many ways we had to get the target ct-num
# because we know we can add num to any of these ways to get ct.
#
# Time complexity: O(t*n) - We iterate t times on the outer loop and n
# times on the inner loop on the worst case. Sorting the input array and
# breaking out of the inner loop when num > ct speeds the process but
# does not change the overall complexity.
# Space complexity: O(t) - We store an array of t values. Another option
# is to keep a dictionary, on the best case its size would be smaller,
# but on the tests the solution that uses the array performs better.
#
# Using defaultdict(int):
# Runtime: 53 ms, faster than 72.51%
# Memory Usage: 13.9 MB, less than 80.97%
#
# Using a prefilled array of length target + 1:
# Runtime: 37 ms, faster than 97.54%
# Memory Usage: 13.9 MB, less than 48.19%
class BottomUpDP:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Sorting the input lets us break of the inner loop faster.
        nums.sort()
        # Prefill the array with the base case + 0s
        dp = [1] + [0] * target
        # Iterate over 1..target.
        for ct in range(1, target + 1):
            for num in nums:
                # When we reach a value > ct, we know that we cannot use
                # this, or any of the next values, break.
                if num > ct:
                    break
                # Add the ways to sum to ct - num to dp[ct]
                dp[ct] += dp[ct - num]
        # Return the number of ways we found to add up to target.
        return dp[target]


def test():
    executors = [
        Memoized,
        BottomUpDP,
    ]
    tests = [
        [[10, 2, 7, 6, 1, 5], 8, 51],
        [[1, 2, 3], 4, 7],
        [[9], 3, 0],
        [[2], 1, 0],
        [[2], 2, 1],
        [[2, 3, 6, 7], 7, 4],
        [[2, 3, 5], 8, 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.combinationSum4(t[0], t[1])
                exp = t[2]
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
