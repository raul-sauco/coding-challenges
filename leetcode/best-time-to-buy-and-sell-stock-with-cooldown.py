# 309. Best Time to Buy and Sell Stock with Cooldown
# 🟠 Medium
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
#
# Tags: Array - Dynamic Programming

import timeit
from functools import cache
from typing import List

# The brute force solution explores all possible paths, to buy or not to
# buy when we don't hold any stock and to sell and not to sell when we
# do hold stock.
#
# Time complexity: O(2^n) - On each level the decision tree doubles in
# size.
# Space complexity: O(n) - Where n is the size of the prices list, the
# call stack can grow to a max of size n, limited to 5000.
#
# This solution would fail with Time Limit Exceeded.

# The memoized solution improves over the brute force version storing
# branches that have been computed to avoid repeated work. To do that
# we can use the functools @cache annotation.
#
# Time complexity: O(n^2) - We compute each of the n^2 results once.
# Space complexity: O(n) - Where n is the size of the prices list, the
# call stack can grow to a max of size n, limited to 5000.
#
# Runtime: 63 ms, faster than 77.31%
# Memory Usage: 18.4 MB, less than 28.7%
class Memoized:
    def maxProfit(self, prices: List[int]) -> int:
        # Define a recursive function that takes one of two options
        # available to it and returns the profit obtained by the
        # most profitable of the two.
        @cache
        def mp(i: int, has_stock: bool) -> int:
            # Base case, we have considered all days.
            if i >= len(prices):
                return 0
            # If we don't hold any stock, we can buy or not buy.
            if not has_stock:
                buy = mp(i + 1, True) - prices[i]
                do_not_buy = mp(i + 1, False)
                return max(buy, do_not_buy)
            # If we hold stock, we can sell or not sell.
            else:
                sell = mp(i + 2, False) + prices[i]
                do_not_sell = mp(i + 1, True)
                return max(sell, do_not_sell)

        # Initial call.
        return mp(0, False)


# Define a two-dimensional dp object that stores the following data.
# dp[i][0]: Max profit obtained at i while also holding stock.
# dp[i][1]: Max profit obtained at i while not holding stock and
# the next day is not a cooldown day.
# dp[i][2]: Max profit obtained at i while not holding stock and
# the next day must be a cooldown day.
# Then iterate over the prices in the input using them to update the
# max profit possible on each day.
#
# Time complexity: O(n) - The loop iterates n times and for each does
# O(1) work.
# Space complexity: O(n) - We store three values for each position of
# the index.
#
# Runtime: 78 ms, faster than 61.76%
# Memory Usage: 14.4 MB, less than 56.82%
class BottomUpDP:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(prices) + 1)]
        # Before we start, it is impossible to be holding stock.
        dp[0][0] = float("-inf")
        for i in range(1, len(prices) + 1):
            price = prices[i - 1]
            # The max profit holding stock at this index.
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - price)
            # The max profit not holding stock at this index but maybe
            # with cooldown the next day.
            dp[i][1] = max(dp[i - 1][0] + price, dp[i - 1][1])
            # The max profit not holding stock and not having cooldown
            # the next day.
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[-1])


# Optimize the space complexity of the previous solution by only storing
# the data for the previous position.
#
# Time complexity: O(n) - The loop iterates n times and for each does
# O(1) work.
# Space complexity: O(1) - We only store one array of length 3.
#
# Runtime: 63 ms, faster than 77.31%
# Memory Usage: 14 MB, less than 96.67%
class SOBottomUpDP:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [float("-inf"), 0, 0]
        for i in range(len(prices)):
            price = prices[i]
            prev = dp.copy()
            # The max profit holding stock at this index.
            dp[0] = max(prev[0], prev[2] - price)
            # The max profit not holding stock at this index but maybe
            # with cooldown the next day.
            dp[1] = max(prev[0] + price, prev[1])
            # The max profit not holding stock and not having cooldown
            # the next day.
            dp[2] = max(prev[1], prev[2])
        return max(dp)


def test():
    executors = [
        Memoized,
        BottomUpDP,
        SOBottomUpDP,
    ]
    tests = [
        [[1], 0],
        [[1, 2, 3, 0, 2], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxProfit(t[0])
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
