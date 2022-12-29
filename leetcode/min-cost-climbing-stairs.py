# 746. Min Cost Climbing Stairs
# 🟢 Easy
#
# https://leetcode.com/problems/min-cost-climbing-stairs/
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List

# 1e5 runs:
# » TopDownTabulation   0.67027   seconds
# » BottomUpTabulation  0.36439   seconds
# » BottomUpVarTab      0.2765    seconds


# 1D tabulation
#
# Time Complexity O(n) - We will visit each element once.
# Space Complexity O(n) - We store intermediate results a list that
# depends on the input size.
#
# Runtime: 60 ms, faster than 94.46%
# Memory Usage: 14 MB, less than 75.93%
class TopDownTabulation:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0  # We can start at the top.
        min_costs = [float("inf") for _ in range(len(cost) + 2)]
        min_costs[0] = min_costs[1] = 0  # We can reach them for "free".

        # Start at 0 and record minimum cost of moving forward.
        for i in range(len(cost)):
            min_costs[i + 1] = min(min_costs[i + 1], min_costs[i] + cost[i])
            min_costs[i + 2] = min(min_costs[i + 2], min_costs[i] + cost[i])
        return min_costs[len(cost)]


# Turn the top-down approach around for bottom-up.
#
# Time Complexity O(n) - We will visit each element once.
# Space Complexity O(n) - We store intermediate results a list of the
# same size as the input.
#
# Runtime: 60 ms, faster than 94.46%
# Memory Usage: 13.9 MB, less than 97.40%
class BottomUpTabulation:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 2)
        for i in range(len(cost) - 1, -1, -1):
            memo[i] = cost[i] + min(memo[i + 1], memo[i + 2])
        return min(memo[0], memo[1])


# Optimize the memory usage of the bottom-up approach using two
# variables.
#
# Time Complexity O(n) - We visit each element once.
# Space Complexity O(1) - We store intermediate results in 3 variables
# independently of the input size.
#
# Runtime: 56 ms, faster than 95.86%
# Memory Usage: 13.9 MB, less than 97.40%
class BottomUpVarTab:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            a, b = b, cost[i] + min(b, a)
        return min(b, a)


def test():
    executors = [
        TopDownTabulation,
        BottomUpTabulation,
        BottomUpVarTab,
    ]
    tests = [
        [[], 0],
        [[10, 1], 1],
        [[10, 15, 20], 15],
        [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minCostClimbingStairs(t[0])
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
