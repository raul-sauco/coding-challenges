# 1833. Maximum Ice Cream Bars
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-ice-cream-bars/
#
# Tags: Array - Greedy - Sorting

import timeit
from typing import List


# Sort the costs and iterate over them buying as many ice creams,
# greedily choosing the cheapest first, until we either bought all of
# the ice cream or run out of coins.
#
# Time complexity: O(n*log(n)) - Sorting the costs has the highest
# complexity.
# Space complexity: O(n) - Sorting in Python takes linear space.
#
# Runtime 1114 ms Beats 52.62%
# Memory 27.9 MB Beats 61.26%
class CompareSort:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res, remaining_coins = 0, coins
        for cost in costs:
            if cost > remaining_coins:
                break
            remaining_coins -= cost
            res += 1
        return res


# Use bucket sort to improve the time complexity, we first place all the
# ice cream in an array of frequencies indexed by their price, then
# iterate over that array to compute how many ice creams we can buy.
#
# Time complexity: O(n+p) - We iterate over p positions, where p is the
# highest value in the costs array, then we iterate, to save the
# frequencies into the buckets array we iterate over the n elements on
# the input array costs.
# Space complexity: O(p) - The buckets array has a size p where p is the
# highest cost in the input.
#
# Runtime 1251 ms Beats 48.95%
# Memory 28.1 MB Beats 17.54%
class BucketSort:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Initialize an array of buckets with costs frequencies.
        buckets = [0] * (max(costs) + 1)
        for cost in costs:
            buckets[cost] += 1
        res, remaining_coins = 0, coins
        # Iterate over the costs from the cheapest end buying as many
        # ice cream as possible.
        for cost in range(len(buckets)):
            # If we don't have enough coins to buy one, exit.
            if remaining_coins < cost:
                break
            # Skip empty frequencies.
            if buckets[cost] == 0:
                continue
            # Compute the number of ice creams of this price that we
            # can buy with the remaining coins, it could be all of them.
            can_buy_count = min(buckets[cost], remaining_coins // cost)
            remaining_coins -= can_buy_count * cost
            res += can_buy_count
        return res


def test():
    executors = [
        CompareSort,
        BucketSort,
    ]
    tests = [
        [[1, 3, 2, 4, 1], 7, 4],
        [[10, 6, 8, 7, 7, 8], 5, 0],
        [[1, 6, 3, 1, 2, 5], 20, 6],
        [[4, 7, 6, 4, 4, 2, 2, 4, 8, 8], 41, 9],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxIceCream(t[0], t[1])
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
