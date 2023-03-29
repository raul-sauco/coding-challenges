# 1402. Reducing Dishes
# 🔴 Hard
#
# https://leetcode.com/problems/reducing-dishes/
#
# Tags: Array - Dynamic Programming - Greedy - Sorting

import timeit
from typing import List


# Solving the problem efficiently becomes easy once we make a few
# observations, it is always better to take all positive values, it is
# also always better to put greater values to the right, so we can start
# by taking all positive values sorted and multiplied by their indexes + 1
# Then, every time we add a negative value, it is better to pick the
# greater one (closer to zero) and try it on the furthest left index, 0.
# The result of adding that value will be adding the negative value * 1 to
# the result, and shifting all the previous values to the right one
# position, which we can compute as being equal to the current sum of
# values in the vector. If the result of adding this value is a gain, do
# it, otherwise, stop trying to add values and return the result.
#
# Time complexity: O(n*log(n)) - Sorting the positive and negative values
# vectors has the highest complexity, everything else is O(n) we iterate
# over the values to split them into positive and negative, iterate over
# the positive values to create the initial sum and result and then
# iterate over the negative values checking if it is worth adding them in
# O(1) time.
# Space complexity: O(n) - The positive and negative vectors.
#
# Runtime 40 ms Beats 81.65%
# Memory 13.9 MB Beats 77.85%
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res, curr_sum = 0, 0
        for val in sorted(satisfaction, reverse=True):
            if curr_sum > -val:
                res += curr_sum + val
                curr_sum += val
            else:
                break
        return res


def test():
    executors = [Solution]
    tests = [
        [[1], 1],
        [[4, 3, 2], 20],
        [[-1, -4, -5], 0],
        [[-1, -8, 0, 5, -9], 14],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxSatisfaction(t[0])
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
