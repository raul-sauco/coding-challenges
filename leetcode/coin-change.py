# 322. Coin Change
# 🟠 Medium
#
# https://leetcode.com/problems/coin-change/
#
# Tags: Array - Breath-First Search - Dynamic Programming

import timeit
from typing import List

# TODO add the memoization solution.

# We can use a bottom-up approach to find the solution. We can use an
# array dp with size amount initialized with MAX_INT. For each position
# and each coin value, we check how many coins we would need to get
# there if that was the last coin we had used. If we are at index i,
# then we check the value dp[i-coin] against the current best that we
# have in dp[i], if using the coin that we are visiting results in a
# better path, we update the best path on dp[i].
#
# Time complexity: O(n*amount) - First we sort on O(n*log(n)), then we
# visit each index of dp, of size len(amount) and, for each, possibly
# visit all the coins.
# Space complexity: O(amount) - Our DP array has size amount + 1.
#
# Runtime: 2455 ms, faster than 42.18%
# Memory Usage: 14.2 MB, less than 86.98%
class BottomUpDP:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float("inf")
        # Store the best result found, initialize with inf.
        dp = [0] + [MAX] * amount
        # Sort the input array to break out of the inner loop when we
        # get coins bigger than the input we are checking.
        coins.sort()
        # Compute the values one at a time.
        for i in range(1, amount + 1):
            # For each position on dp, find the least amount of coins
            # needed to get there.
            for coin in coins:
                # When we see a coin value bigger than the index, we
                # can move to the next index because sorted the input
                # in a previous step, all coins after will be greater.
                if i - coin < 0:
                    break
                # If using this coin to get to this value is a better
                # option, update the shortest combination to get here.
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If we could not find any combination to add up to this amount
        # return -1.
        if dp[-1] == float("inf"):
            return -1
        # Return the minimum number of coins needed to get to amount.
        return dp[-1]


# Similar solution, but using list comprehension instead of the nested
# for loop.
#
# Runtime: 2601 ms, faster than 35.01%
# Memory Usage: 14.4 MB, less than 42.47%
class BottomUpShorter:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float("inf")
        # Store the best result found, initialize with inf.
        dp = [0] + [MAX] * amount
        # Sort the input array to break out of the inner loop when we
        # get coins bigger than the input we are checking.
        coins.sort()
        # Compute the values one at a time.
        for i in range(1, amount + 1):
            # For each position on dp, find the least amount of coins
            # needed to get there. We can use min and list comprehension
            # to get the minimum amount of coins that amount to i.
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        # If we could not find any combination to add up to this amount
        # return -1.
        if dp[-1] == float("inf"):
            return -1
        # Return the minimum number of coins needed to get to amount.
        return dp[-1]


def test():
    executors = [
        BottomUpDP,
        BottomUpShorter,
    ]
    tests = [
        [[1, 2, 5], 11, 3],
        [[2], 3, -1],
        [[1], 0, 0],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.coinChange(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
