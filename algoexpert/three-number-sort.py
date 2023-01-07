# Three Number Sort
# 🟠 Medium
#
# https://www.algoexpert.io/questions/three-number-sort
#
# Tags: Sorting

import timeit
from collections import Counter


# Count the frequencies of the digits in the input array, then use these
# frequencies to determine how many positions to update to a given digit
# on the result.
#
# Time complexity: O(n) - Two passes, one to get the frequencies and one
# to update the positions to their result values.
# Space complexity: O(1) - Only a counter of size 3 of extra memory is
# used, we could also use 3 variables instead, or 2 variables and
# use them combined to compute the third.
class Solution:
    def threeNumberSort(self, array, order):
        # Get the frequencies, there are only 3 so O(1) space.
        freq = Counter(array)
        # Iterate over digits in the given order.
        nxt_idx = 0
        for digit in order:
            # Update as many positions to this number as in the original
            # input.
            for _ in range(freq[digit]):
                array[nxt_idx] = digit
                nxt_idx += 1
        return array


def test():
    executors = [Solution]
    tests = [
        [[], [1, 2, 3], []],
        [[3, 2, 1], [1, 2, 3], [1, 2, 3]],
        [[1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1], [0, 0, 0, 1, 1, 1, -1, -1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.threeNumberSort(t[0], t[1])
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
