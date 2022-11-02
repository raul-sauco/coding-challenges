# 518. Coin Change II
# 🟠 Medium
#
# https://leetcode.com/problems/coin-change-ii/
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List

# 100 calls.
# » Memoized            0.06143   seconds
# » DP                  0.02302   seconds
# » DPO1                0.00874   seconds

# Use DFS to explore two paths at each point, using and not using the
# current coin value, once we decide to not use a current coin value, we
# cannot go back and decide to use it at a later step, this avoids
# having duplicate results like (1,2,2) and (2,1,2).
#
# Time complexity: O(m*n) - With m the number of coins and n the target
# amount, we can see that we will call dfs with a maximum of m*n
# combinations of arguments, since repeated calls will be stored, they
# will not be recomputed.
# Space complexity: O(m*n) - The size of the memo object. The call stack
# can grow to size max(m,n).
#
# Runtime: 980 ms, faster than 38.77%
# Memory Usage: 164.9 MB, less than 6.42%
class Memoized:
    def change(self, amount: int, coins: List[int]) -> int:
        # Store results already computed.
        memo = {}
        # Use manual caching, functools.cache fails with maximum
        # recursion exceeded, probably because the extra function call.
        def dfs(idx: int, s: int) -> int:
            if idx == len(coins) or s > amount:
                return 0
            if s == amount:
                return 1
            if (idx, s) in memo:
                return memo[(idx, s)]
            # The sum of ways to build amount - s using coins[i:]
            memo[(idx, s)] = dfs(idx, s + coins[idx]) + dfs(idx + 1, s)
            return memo[(idx, s)]

        return dfs(0, 0)


# Using a dp[i][j] we can store the number of ways to make up amount j
# using coins[:i], we can initialize all rows[0] like dp[i][0] = 0 which
# means that there is exactly one way to make up amount 0 with the given
# choice of coins: not using any of them. Then we can compute any
# dp[i][j] like the sum of the ways to make up j without using the last
# coin i: dp[i-1][j] plus the ways to make up j - coin using the same
# combination of coins: dp[i][j-coins[i-1]]
#
# Time complexity: O(m*n) - We iterate over the number of coins and, in
# the inner loop, over 0..amount.
# Space complexity: O(m*n) - The size of the dp object.
#
# Runtime: 471 ms, faster than 61.53%
# Memory Usage: 29.6 MB, less than 36.83%
class DP:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        for i in range(1, len(coins) + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        return dp[-1][-1]


# We can optimize the memory complexity of the previous solution, if we
# notice that we only ever need to access the results of: the same value
# of j and previous row, and previous values of j in the same row. That
# means that we can keep all the data we need in one array of size
# amount and overwrite it as we go because we will never need the values
# that we are overwriting after we used once.
#
# Time complexity: O(m*n) - We iterate over the number of coins and, in
# the inner loop, over coin..amount.
# Space complexity: O(n) - The size of the dp object.
#
# Runtime: 128 ms, faster than 99.67%
# Memory Usage: 13.9 MB, less than 98.95%
class DPO1:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * (amount)
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]


def test():
    executors = [
        Memoized,
        DP,
        DPO1,
    ]
    tests = [
        [3, [2], 0],
        [10, [10], 1],
        [5, [1, 2, 5], 4],
        [500, [1, 2, 5], 12701],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.change(t[0], t[1])
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
