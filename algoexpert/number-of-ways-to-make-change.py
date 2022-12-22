# Number Of Ways To Make Change
# 🟠 Medium
#
# https://www.algoexpert.io/questions/number-of-ways-to-make-change
#
# Tags: Dynamic Programming

import timeit


# Use a recursive function that explores the decision tree by, at each
# step, deciding to use the coin at the current index we are exploring
# or skip it, once we skip a coin, we never use it again later.
#
# Time complexity: O(2^n) - At each level the decision tree splits into
# two, there are n levels where n is the amount we want to build.
# Space complexity: O(n) - The size of the call stack.
class BruteForce:
    def numberOfWaysToMakeChange(self, n, denoms):
        # The index we are exploring and the current sum we have built,
        # it returns the number of ways to sum up to n starting here.
        def dfs(i: int, current: int) -> int:
            # Base case, we built the sum.
            if current == n:
                return 1
            # Base case, we have gone over the value or have run out of
            # denominations to try.
            if current > n or i == len(denoms):
                return 0
            # Recursive call.
            return dfs(i, current + denoms[i]) + dfs(i + 1, current)

        return dfs(0, 0)


# Same logic as the previous solution but we memoize results to avoid
# computing the same branches multiple times.
#
# Time complexity: O(n^2) - We will compute all combinations of index
# and sum we can have, if we have the "1" denomination, that will be
# n^2 combinations.
# Space complexity: O(n) - The height of the call stack.
class Memoized:
    def numberOfWaysToMakeChange(self, n, denoms):
        # A dictionary of dfs call parameters: result.
        memo = {}
        # The index we are exploring and the current sum we have built,
        # it returns the number of ways to sum up to n starting here.
        def dfs(i: int, current: int) -> int:
            # Base case, we built the sum.
            if current == n:
                return 1
            # Base case, we have gone over the value or have run out of
            # denominations to try.
            if current > n or i == len(denoms):
                return 0
            # Check if we have precomputed this branch.
            key = (i, current)
            if key in memo:
                return memo[key]
            # Recursive call.
            res = dfs(i, current + denoms[i]) + dfs(i + 1, current)
            memo[key] = res
            return res

        return dfs(0, 0)


# Use the same logic to arrive at a dynamic programming solution, for
# each amount between 0 and n, we can add all the denominations to
# arrive at the next change we can construct.
#
# Time complexity: O(n*d) - We will compute all combinations of index
# and denomination that are possible.
# Space complexity: O(n) - The dp array has size n.
class DP:
    def numberOfWaysToMakeChange(self, n, denoms):
        # We have one way of arriving at target 0, not using any coins.
        dp = [1] + [0] * n
        # Denominations need to be on the outer loop to make sure that
        # once we "move on" from a denomination, we don't use it again.
        # This prevents having repeated combinations.
        for denom in denoms:
            for amount in range(1, n + 1):
                idx = amount - denom
                if idx >= 0 and dp[idx]:
                    dp[amount] += dp[idx]
        return dp[-1]


def test():
    executors = [
        BruteForce,
        Memoized,
        DP,
    ]
    tests = [
        [6, [1, 5], 2],
        [12, [2, 3, 7], 4],
        [10, [1, 5, 10, 25], 4],
        [25, [1, 5, 10, 25], 13],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numberOfWaysToMakeChange(t[0], t[1])
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
