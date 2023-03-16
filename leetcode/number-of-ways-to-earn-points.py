# 2585. Number of Ways to Earn Points
# 🔴 Hard
#
# https://leetcode.com/problems/number-of-ways-to-earn-points/
#
# Tags: Array - Dynamic Programming

import json
import os
import timeit
from functools import cache
from typing import List


# The recursive memoized solution, define a function that takes in an
# index, the number of values of that type that we can still use, and a
# target, and returns the number of different ways that we can arrive at
# that target from that state. At each level of the call stack we make
# two calls, that would be O(2^n) without memoization, using memoization
# the maximum number of calls equals the number of different arguments
# that the function can receive, that is n*max(count)*t, the number of
# questions * the maximum value of count * the possible values that
# the target can take 0..t.
#
# Time complexity: O(n*c*t) -  n: the number of questions * c: the
# maximum value of count * t the possible values that the target can
# take 0..t.
# Space complexity: O(min(n*c, t)) - The execution branch where we take
# all the questions possible would have a call stack of height n*c if
# the target was big enough to not go to zero after taking all the
# available points, otherwise the call stack height would be limited by
# the value of target.
#
# This solution fails with Time Limit Exceeded.
class Memoization:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # A function that gets an index for the types array, the number
        # of questions of that type that we have not picked yet, and the
        # current target for which we are aiming and returns the number
        # of ways to add up to t from the given state.
        @cache
        def helper(i: int, rem: int, t: int) -> int:
            # If we have gone over the target, or gone passed the end
            # index, this path did not lead to a solution.
            if i == len(types) or t < 0:
                return 0
            # If we have counted to the target, this is a solution.
            if t == 0:
                return 1
            res = helper(i, rem - 1, t - types[i][1]) if rem else 0
            # If there is a next position.
            res += helper(
                i + 1, types[i + 1][0] if i < len(types) - 1 else 0, t
            )
            return res

        return helper(0, types[0][0], target) % (10**9 + 7)


# A very interesting solution from Lee215
# https://leetcode.com/problems/number-of-ways-to-earn-points/solutions/3258120
# It simplifies quite a bit the code and improves the runtime a lot.
#
# Time complexity: O(n*c*t) -  n: the number of questions * c: the
# maximum value of count * t the possible values that the target can
# take 0..t.
# Space complexity: O(t) - The size of the DP array used.
#
# Runtime 1911 ms Beats 88.15%
# Memory 14 MB Beats 74.70%
class DP:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # A dp array that represents the ways to add up to i.
        dp, MOD = [1] + [0] * target, 10**9 + 7
        # For each question count and mark (points) given.
        for count, mark in types:
            # Iterate backwards over the dp array checking if we can
            # add another way to get there using the current combination
            # of values and index.
            for i in reversed(range(target + 1)):
                # Check backwards all the indexes from which we could
                # reach i using the given count and mark.
                for k in range(1, min(count, i // mark) + 1):
                    dp[i] = (dp[i] + dp[i - mark * k]) % MOD
        return dp[-1]


def test():
    executors = [
        Memoization,
        DP,
    ]
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(
        os.path.join(__location__, "number-of-ways-to-earn-points.json")
    ) as json_file:
        tests = json.load(json_file)
        for executor in executors:
            start = timeit.default_timer()
            for _ in range(1):
                for col, t in enumerate(tests):
                    sol = executor()
                    result = sol.waysToReachTarget(t[0], t[1])
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
