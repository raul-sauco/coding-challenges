# 956. Tallest Billboard
# 🔴 Hard
#
# https://leetcode.com/problems/tallest-billboard/
#
# Tags: Array - Dynamic Programming

import timeit
from collections import defaultdict
from typing import List


# Keep a hashmap where the keys are the difference between the shortest
# and longest legs of the billboard and the value is the maximum height
# that we have been able to reach with that difference between the two
# legs. For each element in the input, we compute the result of the
# three options that can be taken, adding it to the shorter leg, the
# longer one, and not using it.
#
# Time complexity: O(n*m) - We iterate over all the n rods, for each, we
# iterate over all the possible keys in the dp hash map, that can take
# any value between 0 and the maximum gap m that we can have between the
# length of both legs.
# Space complexity: O(m) - The number of keys that we can have in the dp
# hashmap, it is the number of values that the gap can take and it could
# be equal to the sum of values in the rods vector, if all gap values
# were possible.
#
# Runtime 344 ms Beats 80.21%
# Memory 16.9 MB Beats 62.50%
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        rods.sort()
        total = sum(rods)
        rem = [0] * len(rods)
        for i in range(len(rods)):
            rem[i] = total
            total -= rods[i]

        dp = defaultdict(int)
        dp[0] = 0
        for i, r in enumerate(rods):
            next_dp = dp.copy()
            for diff, taller in dp.items():
                if diff + r <= rem[i]:
                    next_dp[diff + r] = max(next_dp[diff + r], taller + r)
                shorter = taller - diff + r
                new_diff = abs(shorter - taller)
                if new_diff <= rem[i]:
                    next_dp[new_diff] = max(
                        next_dp[new_diff], max(shorter, taller)
                    )
            dp = next_dp
        return dp[0]


# Neat solution by Lee@215, it merges both ideas in the editorial
# splitting the problem in two to reduce the exponential complexity
# while using the concepts of the dynamic programming solution.
#
# Time complexity: O(n*m) - Where n = len(rods) <= 20, s = sum(rods) <=
# 5000 and m = possible sums == possible keys = min(3^n/2, s)
# Space complexity: O(m) - The number of keys.
class Sol2:
    def tallestBillboard(self, rods: List[int]) -> int:
        def helper(rods):
            dp = {0: 0}
            for r in rods:
                for d, h in list(dp.items()):
                    dp[d + r] = max(dp.get(d + r, 0), h)
                    dp[abs(d - r)] = max(dp.get(abs(d - r), 0), h + min(d, r))
            return dp

        dp1, dp2 = helper(rods[: len(rods) // 2]), helper(
            rods[len(rods) // 2 :]
        )
        return max(h + d + dp2[d] for d, h in dp1.items() if d in dp2)


def test():
    executors = [
        Solution,
        Sol2,
    ]
    tests = [
        [[1, 2], 0],
        [[1, 2, 3, 6], 6],
        [[1, 2, 3, 4, 5, 6], 10],
        [
            [
                1,
                2,
                4,
                8,
                16,
                32,
                64,
                128,
                256,
                512,
                50,
                50,
                50,
                150,
                150,
                150,
                100,
                100,
                100,
                123,
            ],
            1023,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.tallestBillboard(t[0])
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
