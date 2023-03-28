# 983. Minimum Cost For Tickets
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-cost-for-tickets/
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List


# The brute force solution looks at each day in the days array and, for
# each, it checks the result of either of the three options, buy a day,
# week or month ticket.
#
# Time complexity: O(n^3) - There are n days and each day the decision
# tree splits in 3.
# Space complexity: O(n) - The call stack will reach a height of n.
#
# This solution probably fails with TLE.
class BruteForce:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # A function that explores the recursive tree by splitting into
        # the three decisions that we can make.
        def dfs(idx: int, covered_until: int, current_cost: int) -> int:
            # Base case, we covered the entire year.
            if idx == len(days):
                return current_cost
            # If we are covered by the last tickets, skip this index.
            if covered_until >= days[idx]:
                return dfs(idx + 1, covered_until, current_cost)
            return min(
                dfs(idx + 1, days[idx], current_cost + costs[0]),
                dfs(idx + 1, days[idx] + 6, current_cost + costs[1]),
                dfs(idx + 1, days[idx] + 29, current_cost + costs[2]),
            )

        return dfs(0, 0, 0)


# The minimal cost at any given day when we need to travel will be the
# best between: the best 30 days past plus the cost of a 30 day ticket,
# the best 7 days past plus the cost of a 7 day ticket or the best 1 day
# past plus the cost of a 1 day ticket. If we don't need to travel, we
# can maintain the same best cost as the day before.
#
# Time complexity: O(n) - Where n is the last day we need to travel,
# days[-1] and it has an upper bound of 365, then O(n) ≈ O(1).
# Space complexity: O(n) - The dp array goes from 0 to days[-1].
#
# Runtime 39 ms Beats 91.51%
# Memory 13.8 MB Beats 83.75%
class DP:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] + [None] * days[-1]
        # The next index on the days array that we need to cover.
        idx = 0
        for i in range(1, len(dp)):
            # We need to travel today.
            if i == days[idx]:
                # Shift the index pointer.
                idx += 1
                dp[i] = min(
                    dp[i - 1] + costs[0],
                    costs[1] + (dp[i - 7] if i >= 7 else 0),
                    costs[2] + (dp[i - 30] if i >= 30 else 0),
                )
            # No need to travel, maintain yesterday's cost.
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


def test():
    executors = [
        BruteForce,
        DP,
    ]
    tests = [
        [[1, 4, 6, 7, 8, 20], [2, 7, 15], 11],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.mincostTickets(t[0], t[1])
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
