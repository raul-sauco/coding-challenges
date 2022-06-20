# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import timeit
from typing import List

# Naive solution
#
# Runtime: 1683 ms, faster than 29.83% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 24.9 MB, less than 94.86 % of Python3 online submissions for Best Time to Buy and Sell Stock.
#
# Iterate over the prices from most recent to oldest:
#   Using an index increases execution time by 50%
#   for i in range(len(prices)-1, -1, -1):
#       p = prices[i]
#
# Using max() instead of if: triples execution time
#   max_profit = max(highest_future_price - p, max_profit)
#   highest_future_price = max(highest_future_price, p)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_future_price = max_profit = 0
        for p in reversed(prices):
            if p > highest_future_price:
                highest_future_price = p
            elif highest_future_price - p > max_profit:
                max_profit = highest_future_price - p
        return max_profit


# The forward solution ranks higher in LeetCode but runs in similar time locally.
#
# Runtime: 1406 ms, faster than 54.97% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 85.31 % of Python3 online submissions for Best Time to Buy and Sell Stock.
class FSolution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


def test():
    executor = [
        {'executor': Solution, 'title': 'Solution', },
        {'executor': FSolution, 'title': 'FSolution', },
    ]
    tests = [
        [[7, 1, 5, 3, 6, 4], 5],
        [[7, 6, 4, 3, 1], 0],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(1000000):
            for t in tests:
                sol = e['executor']()
                result = sol.maxProfit(t[0])
                assert result == t[1], f'{result} != {t[1]}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
