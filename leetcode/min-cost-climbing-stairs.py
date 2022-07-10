# https://leetcode.com/problems/min-cost-climbing-stairs/

import timeit
from typing import List

# Tags: Array - Dynamic Programming

# 1e5 runs:
# » BottomUpVarTab      0.2765    seconds
# » BottomUpTabulation  0.36439   seconds
# » TopDownTabulation   0.67027   seconds

# Optimize the memory usage of the bottom-up approach using two variables
#
# Time Complexity O(n) - we visit each element once
# Space Complexity O(1) - we store intermediate results in 3 variables independently of the input size
#
# Runtime: 94 ms, faster than 45.82% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14.1 MB, less than 44.40% of Python3 online submissions for Min Cost Climbing Stairs.
class BottomUpVarTab:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b, c = 0, 0, 0
        for i in range(len(cost) - 1, -1, -1):
            c = cost[i] + min(b, a)
            a, b = b, c
        return min(b, a)


# Turn the top-down approach around for bottom-up
#
# Time Complexity O(n) - we visit each element once
# Space Complexity O(n) - we store intermediate results a list that depends on the input size
#
# Runtime: 60 ms, faster than 94.46% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 13.9 MB, less than 97.40% of Python3 online submissions for Min Cost Climbing Stairs.
class BottomUpTabulation:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 2)
        for i in range(len(cost) - 1, -1, -1):
            memo[i] = cost[i] + min(memo[i + 1], memo[i + 2])
        return min(memo[0], memo[1])


# 1D tabulation
#
# Time Complexity O(n) - we visit each element once
# Space Complexity O(n) - we store intermediate results a list that depends on the input size
#
# Runtime: 60 ms, faster than 94.46% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14 MB, less than 75.93% of Python3 online submissions for Min Cost Climbing Stairs.
class TopDownTabulation:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0  # We can start at the top
        min_costs = [float("inf") for _ in range(len(cost) + 2)]
        min_costs[0] = min_costs[1] = 0  # We can reach them for "free"

        # Start at 0 and record minimum cost of moving forward
        for i in range(len(cost)):
            min_costs[i + 1] = min(min_costs[i + 1], min_costs[i] + cost[i])
            min_costs[i + 2] = min(min_costs[i + 2], min_costs[i] + cost[i])
        return min_costs[len(cost)]


def test():
    executors = [BottomUpVarTab, BottomUpTabulation, TopDownTabulation]
    tests = [
        [[10, 15, 20], 15],
        [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6],
        [[], 0],
        [[10, 1], 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.minCostClimbingStairs(t[0])
                expected = t[1]
                assert result == expected, f"{result} != {expected} for test {i} using {executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
