# 901. Online Stock Span
# 🟠 Medium
#
# https://leetcode.com/problems/online-stock-span/
#
# Tags: Stack - Design - Monotonic Stack - Data Stream

import timeit

from sortedcontainers import SortedList


class NaiveStockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        span = 0
        for i in range(len(self.prices) - 1, -1, -1):
            if self.prices[i] <= price:
                span += 1
                continue
            break
        return span


# Use a monotonic stack, each element contains the price and the number
# of consecutive days at which the stock was at a price not greater than
# that price on that day. When we add a new element, we start the count
# of days at one, the current day, then check the stack and pop any
# elements where the price is smaller adding the number of consecutive
# days at, or below, that price, to the current count. Then add the
# current price and result to the stack and return the result.
#
# Time complexity: O(n) - Average cost for the next method is O(1), some
# calls may be more expensive, but the total calls to stack.append and
# stack pop will be n where n each is the number of calls to next.
# Space complexity: O(n) - The stack may hold all prices if they are
# non-increasing.
#
# Runtime: 923 ms, faster than 58.78%
# Memory Usage: 19.4 MB, less than 70.93%
class StockSpanner:
    def __init__(self):
        # A monotonic decreasing stack where the entries are
        # (val, count), the value in the stack and the count of values
        # equal to, or smaller than, itself that the value has
        # contiguously to its left.
        self.prices = []

    def next(self, price: int) -> int:
        count = 1
        while self.prices and self.prices[-1][0] <= price:
            # Pop the tuple of (price, count of lesser to its left)
            count += self.prices.pop()[1]
        self.prices.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


def test():
    executors = [
        NaiveStockSpanner,
        StockSpanner,
    ]
    tests = [
        [
            [
                "StockSpanner",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
            ],
            [[], [100], [80], [60], [70], [60], [75], [85]],
            [None, 1, 1, 1, 2, 1, 4, 6],
        ],
        [
            [
                "StockSpanner",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
            ],
            [[], [28], [14], [28], [35], [46], [53], [66], [80], [87], [88]],
            [None, 1, 1, 3, 4, 5, 6, 7, 8, 9, 10],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    result = getattr(sol, call)(t[1][i][0])
                    exp = t[2][i]
                    assert result == exp, (
                        f"\033[93m» {result} <> {exp}\033[91m for"
                        + f" test {col} assertion {i} "
                        + f"using \033[1m{executor.__name__}"
                    )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
