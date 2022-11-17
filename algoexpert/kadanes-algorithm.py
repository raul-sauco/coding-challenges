# Kadane's Algorithm
# 🟠 Medium
#
# https://www.algoexpert.io/questions/kadane's-algorithm
#
# Tags: Famous Algorithms

import timeit
from itertools import accumulate
from typing import List

# » Naive               0.02286   seconds
# » Kadanes             0.00534   seconds

# Create an array of prefix sums, then iterate over every pair of
# indexes computing the sum of the elements between them by subtracting
# the prefix sum before the start of the interval from the prefix sum
# after the interval.
#
# Time complexity: O(n^2) - The nested loop that checks every pair of
# indexes.
# Space complexity: O(n) - The prefix sum array.
class Naive:
    def kadanesAlgorithm(self, array: List[int]) -> int:
        # Compute prefix sums.
        res, ps = float("-inf"), [0] + list(accumulate(array))
        for i in range(len(ps)):
            for j in range(i + 1, len(ps)):
                res = max(res, ps[j] - ps[i])
        return res


# Use Kadane's algorithm to compute the sum in O(n).
#
# Time complexity: O(n) - We visit each element once and do O(1) work.
# Space complexity: O(1)
class Kadanes:
    def kadanesAlgorithm(self, array: List[int]) -> int:
        max_at_index = array[0]
        res = array[0]
        for i in range(1, len(array)):
            max_at_index = max(array[i], array[i] + max_at_index)
            res = max(res, max_at_index)
        return res


def test():
    executors = [
        Naive,
        Kadanes,
    ]
    tests = [
        [[-10], -10],
        [[-2, 1], 1],
        [[3, 4, -6, 7, 8, -18, 100], 100],
        [[3, 4, -6, 7, 8, -15, 100], 101],
        [[3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4], 19],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1000):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.kadanesAlgorithm(t[0])
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
