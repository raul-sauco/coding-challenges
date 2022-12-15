# Min Rewards
# 🔴 Hard
#
# https://www.algoexpert.io/questions/min-rewards
#
# Tags: Greedy - Array

import timeit
from typing import List


# We want to minimize the number of rewards, start by trying to assign 1
# to all students, then iterate over the entire array in both directions
# checking student' scores against their neighbors and correcting the
# number of scores that the student with the highest score of the
# current pair will receive.
#
# Time complexity: O(n) - We iterate twice over the array and perform
# constant time operations.
# Space complexity: O(n) - We use an extra array in memory of the same
# size as the input.
class Solution:
    def minRewards(self, scores: List[int]):
        res = [1] * len(scores)
        # Left to right
        for i in range(1, len(scores)):
            if scores[i - 1] < scores[i]:
                res[i] = res[i - 1] + 1
        # Each score now is at the minimum it can be when considered
        # left to right, but it may need to be higher when comparing it
        # to its right neighbor.
        for i in range(len(scores) - 2, -1, -1):
            if scores[i] > scores[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
        # The minimum number of rewards that we can give.
        return sum(res)


def test():
    executors = [Solution]
    tests = [
        [[8], 1],
        [[8, 10], 3],
        [[15, 8, 10], 5],
        [[15, 18, 10], 4],
        [[8, 4, 2, 1, 3, 6, 7, 9, 5], 25],
        [[2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0], 52],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minRewards(t[0])
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
