# Detect Arbitrage
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/detect-arbitrage
#
# Tags: Graphs

import timeit


# For each currency, recursively compute the maximum amount of other
# currencies that we can obtain, every time that we best the amount of
# one currency, use it to check how many of all other currencies we
# could potentially buy using the new amount.
# TODO: Check the solution that uses Bellman-Ford, it may be better.
#
# Time complexity: O(n^3) - The outer loop goes over n elements, the
# middle loop iterates over all currencies that have been updated in
# the last iteration of the inner loop, the inner loop iterates over all
# currencies checking if we can use the updated amount of base currency
# to obtain more of this currency than previously we thought it was
# possible.
# Space complexity: O(n) - The exchange array x has length n and the
# updated set will grow to n-1 in the first loop, because all other
# currencies will be updated.
class Solution:
    def detectArbitrage(self, exchangeRates) -> bool:
        n = len(exchangeRates)
        # Try starting with one unit of each currency.
        for i in range(n):
            # The max amount of other currencies that we have figured
            # out how to get using 1 unit of i.
            x = [float("-inf")] * n
            x[i] = 1
            # Exchange rates that have become better in the last
            # iteration.
            updated = set([i])
            # Compute the exchange after one change.
            while updated:
                base = updated.pop()
                # How many base units do we have?
                amount = x[base]
                # Iterate over all other currencies checking how many
                # units we would get using amount units of base. If the
                # transaction results in a worst result than previous
                # transactions, cancel it.
                for desired in range(n):
                    if desired == base:
                        continue
                    rate = exchangeRates[base][desired]
                    total = amount * rate
                    if total > x[desired]:
                        # If this is the base currency, we have detected
                        # arbitrage.
                        if desired == i:
                            return True
                        x[desired] = total
                        updated.add(desired)
        # We have made all transactions possible and we have not detected
        # arbitrage being a possibility.
        return False


def test():
    executors = [Solution]
    tests = [
        [[[1, 2], [0.4, 1]], False],
        [
            [
                [1, 0.8631, 0.5903],
                [1.1586, 1, 0.6849],
                [1.6939, 1.46, 1],
            ],
            True,
        ],
        [
            [
                [1, 0.5, 0.25, 2],
                [2, 1, 0.5, 4],
                [4, 2, 1, 8],
                [0.5, 0.25, 0.0125, 1],
            ],
            False,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.detectArbitrage(t[0])
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
