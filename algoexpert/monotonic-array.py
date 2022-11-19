# Monotonic Array
# 🟠 Medium
#
# https://www.algoexpert.io/questions/monotonic-array
#
# Tags: Arrays

import timeit
from typing import List


# Iterate over the input values. Use the first time a value is different
# to its preceding element to determine if the monotonic array should be
# non-increasing or non-decreasing, then make sure that all following
# values comply, if we find any value that breaks the tonic, return False.
#
# Time complexity: O(n) - We visit each value once and do O(1) operations.
# Space complexity: O(1) - Constant space.
class Solution:
    def isMonotonic(self, array: List[int]) -> bool:
        if len(array) < 3:
            return True
        # Should it be decreasing?
        dec = None
        prev = array[0]
        for val in array[1:]:
            # Skip equal values
            if val == prev:
                continue
            # Use the first decreasing or non-decreasing value
            # to determine the ordering.
            if dec is None:
                dec = val < prev
            # If we have already determined the tonic.
            elif (dec and val > prev) or (not dec and val < prev):
                return False
            prev = val
        return True


def test():
    executors = [Solution]
    tests = [
        [[], True],
        [[1], True],
        [[2, 1], True],
        [[-1, -5, -10, -1100, -900, -1101, -1102, -9001], False],
        [[-1, -5, -10, -1100, -1100, -1101, -1102, -9001], True],
        [[1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11], False],
        [[-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isMonotonic(t[0])
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
