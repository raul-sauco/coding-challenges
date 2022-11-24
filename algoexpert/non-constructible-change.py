# Non Constructible Change
# 🟢 Easy
#
# https://www.algoexpert.io/questions/non-constructible-change
#
# Tags: Arrays

import timeit
from typing import List


# The solution will be the first gap between the sum of coins we have
# and the next coin available to us.
#
# Time complexity: O(n) - We iterate over all coins in O(n) but they
# need to be previously sorted on O(n*log(n)).
# Space complexity: O(1) - If we don't consider the space needed for
# sorting, which in python can be n/2 => O(n).
class Solution:
    def nonConstructibleChange(self, coins: List[int]):
        coins.sort()
        s = 0
        for coin in coins:
            # If the next coin is greater than the sum of coins that
            # we have seen plus one, we won't be able to build that
            # amount.
            if coin > s + 1:
                break
            s += coin
        return s + 1


def test():
    executors = [Solution]
    tests = [
        [[1, 1, 1, 1, 1], 6],
        [[5, 7, 1, 1, 2, 3, 22], 20],
        [[1, 5, 1, 1, 1, 10, 15, 20, 100], 55],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.nonConstructibleChange(t[0])
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
