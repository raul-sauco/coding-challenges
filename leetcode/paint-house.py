# 256. Paint House 🔒
# 🟠 Medium
#
# https://leetcode.com/problems/paint-house/ 🔒
#
# 515 · Paint House - LintCode
# https://www.lintcode.com/problem/515
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List


# We can use a dynamic programming top-down approach, for each step, we can pick the best decision taking into
# account the previous decisions.
#
# Time complexity: O(n) - We iterate over the number of houses.
class Solution:
    def min_cost(self, costs: List[List[int]]) -> int:

        # Initialize our dp array.
        dp = [0, 0, 0]
        for i in range(len(costs)):
            # The min cost to paint this house with color 0 is the actual cost + the best of the two possible
            # previous combinations.
            temp = [
                costs[i][0] + min(dp[1], dp[2]),
                costs[i][1] + min(dp[0], dp[2]),
                costs[i][2] + min(dp[0], dp[1]),
            ]
            dp = temp

        return min(dp)


def test():
    executors = [Solution]
    tests = [
        [
            [
                [14, 2, 11],
                [11, 14, 5],
                [14, 3, 10],
            ],
            10,
        ],
        [
            [
                [1, 2, 3],
                [1, 4, 6],
            ],
            3,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.min_cost(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
