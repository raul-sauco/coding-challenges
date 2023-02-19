# Max Profit With K Transactions
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/max-profit-with-k-transactions
#
# Tags: Dynamic Programming

import timeit
from typing import List


# The max profit each day depends on the max profit the previous day,
# whether we are holding stock or not, and the number of transactions
# that we have left.
#
# Time complexity: O(k*n) - The outer loop iterates over n positions
# where n is the number of prices, the inner loop iterates over k
# positions, each iteration of the inner loop computes two values at
# O(1) each.
# Space complexity: O(k) - The dp array has size k.
class Solution:
    def maxProfitWithKTransactions(self, prices: List[int], k: int) -> int:
        # The maximum profit with k-i transactions left, for each entry,
        # [0] represents the max profit holding stock, [1] represents
        # the max profit not holding stock.
        dp = [[float("-inf"), 0]] + [[None, 0] for _ in range(k)]
        # We can always obtain 0 profit not conducting any transactions.
        res = 0
        # Compute the max profit for each day.
        for d in range(len(prices)):
            today = dp[::]
            for i in range(1, len(dp)):
                # The max profit at day d with k-i transactions left.
                today[i][0] = max(
                    dp[i][0] if dp[i][0] is not None else float("-inf"),
                    dp[i - 1][1] - prices[d],
                )
                # Max not holding stock is max between yesterday not
                # holding stock with the same number of transactions
                # left
                today[i][1] = max(
                    dp[i][1] if dp[i][1] is not None else float("-inf"),
                    dp[i][0] + prices[d],
                )
                res = max(res, today[i][1])
            dp = today
        return res


def test():
    executors = [Solution]
    tests = [
        [[], 1, 0],
        [[20], 1, 0],
        [[3, 2, 5, 7, 1, 3, 7], 1, 6],
        [[5, 11, 3, 50, 60, 90], 2, 93],
        [[1, 100, 101, 200, 201, 300, 301, 400, 401, 500], 3, 499],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxProfitWithKTransactions(t[0], t[1])
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
