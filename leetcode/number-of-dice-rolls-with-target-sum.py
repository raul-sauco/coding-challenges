# 1155. Number of Dice Rolls With Target Sum
# 🟠 Medium
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
#
# Tags:

import timeit
from functools import cache


# The brute force solution would generate the k^n combinations and check
# how many match the target.
#
# Time complexity: O(k^n) - For each dice n, the decision tree splits in
# k different branches.
# Space complexity: O(k) - The depth of the call stack.
#
# This solution would fail with Time Limit Exception.
class BruteForce:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        # Define a recursive function that generates the next dice roll.
        # It takes the number of dice left and the current sum as
        # parameters and returns how many ways there are of adding up to
        # the target starting there.
        def roll(dice: int, sum: int) -> int:
            # Base case, no rolls left.
            if not dice:
                # return int(sum == target)
                return 1 if sum == target else 0
            # Compute the total results.
            total = 0
            for i in range(1, k + 1):
                total += roll(dice - 1, sum + i)
            return total

        # Initial call
        return roll(n, 0) % MOD


# The memoized solution is similar to the brute force solution but
# stores results that have already been computed and reuses them.
#
# Time complexity: O(n^2) - The number of
# Space complexity: O(n^2) - The number of intermediate results that get
# stored in cache.
#
# Modding only the final result:
# Runtime: 881 ms, faster than 46.81%
# Memory Usage: 21.8 MB, less than 7.7%
#
# Modding all intermediate results, less memory more time:
# Runtime: 1297 ms, faster than 26.32%
# Memory Usage: 20.4 MB, less than 20.73%
class Memoized:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        # Define a recursive function that generates the next dice roll.
        # It takes the number of dice left and the current sum as
        # parameters and returns how many ways there are of adding up to
        # the target starting there.
        @cache
        def roll(dice: int, sum: int) -> int:
            # Base case, no rolls left.
            if not dice:
                # return int(sum == target)
                return 1 if sum == target else 0
            # Compute the total results.
            total = 0
            for i in range(1, k + 1):
                total += roll(dice - 1, sum + i)
            return total % MOD

        # Initial call
        return roll(n, 0)


def test():
    executors = [
        # BruteForce,
        Memoized,
    ]
    tests = [
        [1, 6, 3, 1],
        [2, 6, 7, 6],
        [10, 5, 50, 1],
        [30, 30, 500, 222616187],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numRollsToTarget(t[0], t[1], t[2])
                exp = t[3]
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
