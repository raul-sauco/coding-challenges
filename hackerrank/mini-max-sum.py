# Mini Max Sum
# 🟢 Easy
#
# https://www.hackerrank.com/challenges/mini-max-sum/
#
# Tags: Array

import timeit
from typing import List, Tuple


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def miniMaxSum(self, arr: List[int]) -> Tuple[int]:
        # Get the cumulative sum, smallest and largest value in O(n)
        cum, greatest, smallest = 0, float("-inf"), float("inf")
        for val in arr:
            cum += val
            greatest = max(greatest, val)
            smallest = min(smallest, val)
        # The min is the sum minus the greatest element, the max is the
        # sum minus the smallest element.
        return (cum - greatest, cum - smallest)


def test():
    executors = [Solution]
    tests = [
        [[1, 3, 5, 7, 9], (16, 24)],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.miniMaxSum(t[0])
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
