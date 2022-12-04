# First Duplicate Value
# 🟠 Medium
#
# https://www.algoexpert.io/questions/first-duplicate-value
#
# Tags: Array

import timeit


# Iterate over the array using the values found as indexes for the same
# array, negate the values at the positions indicated by the values we
# find, if we encounter a value that points to an index that has already
# been negated, that is the first duplicate.
#
# Time complexity: O(n) - We iterate over the input once.
# Space complexity: O(1) - We use constant extra memory.
class Solution:
    def firstDuplicateValue(self, array):
        for val in array:
            # Find the index to which this value is associated.
            if val < 0:
                val = -val
            i = val - 1
            # If the value at that index has been modified, this is the
            # first duplicate value, return it.
            if array[i] < 0:
                return val
            # Negate the value at index i to mark that we have seen this
            # value already.
            array[i] = -array[i]
        return -1


def test():
    executors = [Solution]
    tests = [
        [[], -1],
        [[1], -1],
        [[3, 1, 3, 1, 1, 4, 4], 3],
        [[2, 1, 5, 2, 3, 3, 4, 2], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.firstDuplicateValue(t[0])
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
