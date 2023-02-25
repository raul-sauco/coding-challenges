# 121. Best Time to Buy and Sell Stock
# 🟢 Easy
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List


# The max profit will come from buying at the lowest price possible and
# selling at the highest possible price after that lowest price. We can
# keep a variable with the lowest price that we have seen so far, for
# each element, first we check if its value is less than the current
# lowest price, if it is, we update lowest price and move to the next
# element, if it isn't, we check if the profit of buying at the current
# lowest price and selling at this price is better than the current
# maximum profit, if it is, we update it. Once we iterate over all
# prices, we return the maximum profit found.
#
# Time complexity: O(n) - We visit each price once and do O(1) work.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 904 ms Beats 99.35%
# Memory 24.9 MB Beats 96.97%
class DP:
    def maxProfit(self, prices: List[int]) -> int:
        # Store the minimum value seen.
        lowest_price, max_profit = prices[0], 0
        for price in prices[1:]:
            # If this price is lower than the lowest, update it.
            if price < lowest_price:
                lowest_price = price
            # Else check if this could give us the max profit.
            elif (profit := price - lowest_price) > max_profit:
                max_profit = profit
        return max_profit


# Similar to the previous solution but starts at the end of the array
# and works backwards keeping the value of the highest future price
# seen and using that to compute the max profit.
#
# Time complexity: O(n) - We visit each price once and do O(1) work.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 903 ms Beats 99.42%
# Memory 24.9 MB Beats 96.97%
class BottomUpDP:
    def maxProfit(self, prices: List[int]) -> int:
        highest_future_price = max_profit = 0
        for p in reversed(prices):
            if p > highest_future_price:
                highest_future_price = p
            elif highest_future_price - p > max_profit:
                max_profit = highest_future_price - p
        return max_profit


def test():
    executors = [
        DP,
        BottomUpDP,
    ]
    tests = [
        [[7], 0],
        [[7, 6, 4, 3, 1], 0],
        [[7, 1, 5, 3, 6, 4], 5],
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
