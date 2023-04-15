# 2218. Maximum Value of K Coins From Piles
# 🔴 Hard
#
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
#
# Tags: Array - Dynamic Programming - Prefix Sum

import timeit
from itertools import accumulate
from typing import List


# Use an array of size k+1 to store computed results, iterate over each
# pile and each value i in the range k..0, dp[i] represents the best
# way we have found to pick i coins at the current pile, we can update
# dp[i] as the best way to pick between 0 and k coins from the current
# pile, or between 0 and all the coins if len(pile) < k.
#
# Time complexity: O(m*min(n,k)*k) - Where m is the number of piles, n
# is the max number of coins in any pile and k is the number of coins
# that we can pick in total.
# Space complexity: O(max(n,k)) - The dp array has size k+1, we also
# use an array of prefix sums for each pile with a max size of n.
#
# Runtime 3112 ms Beats 97.48%
# Memory 14.3 MB Beats 97.48%
class DP:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # The best way to pick k coins at the moment.
        dp = [0] * (k + 1)
        # Iterate over each pile.
        for pile in piles:
            # Transform pile into an array of prefix sums.
            pile = [0] + list(accumulate(pile))
            for i in reversed(range(1, k + 1)):
                dp[i] = max(
                    pile[j] + dp[i - j] for j in range(min(len(pile), i + 1))
                )
        return dp[-1]


def test():
    executors = [DP]
    tests = [
        [[[1, 100, 3], [7, 8, 9]], 2, 101],
        [[[1, 10, 3], [7, 8, 9], [8, 20, 10], [50, 25, 18]], 3, 93],
        [
            [
                [100],
                [100],
                [100],
                [100],
                [100],
                [100],
                [1, 1, 1, 1, 1, 1, 700],
            ],
            7,
            706,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxValueOfCoins(t[0], t[1])
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
