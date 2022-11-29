# Min Number Of Coins For Change
# 🟠 Medium
#
# https://www.algoexpert.io/questions/min-number-of-coins-for-change
#
# Tags: Dynamic Programming

import timeit
from typing import List


# The classic coin change problem.
#
# Time complexity: O(m*n) - Where m is the number of different
# denominations available and n is the target amount, for each value
# between 1 and the target amount, we will explore all the denominations.
# Space complexity: O(n) - We store an array of intermediate results of
# the same length as the target amount.
class BottomUpDP:
    def minNumberOfCoinsForChange(
        self, n: int, denominations: List[int]
    ) -> int:
        # Initialize a dp array, we can always build the amount 0 using
        # 0 coins.
        dp = [0] + [float("inf")] * n
        # Iterate over the amounts from zero to amount checking if we
        # can use any of the available coins to build up to that amount
        # with fewer coins that previously used.
        for i in range(1, len(dp)):
            for d in denominations:
                if i >= d and dp[i - d] + 1 < dp[i]:
                    dp[i] = dp[i - d] + 1
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]


def test():
    executors = [BottomUpDP]
    tests = [
        [0, [1], 0],
        [3, [2], -1],
        [11, [1, 2, 5], 3],
        [7, [1, 5, 10], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minNumberOfCoinsForChange(t[0], t[1])
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
