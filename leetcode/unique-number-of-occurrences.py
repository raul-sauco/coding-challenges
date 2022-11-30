# 1207. Unique Number of Occurrences
# 🟢 Easy
#
# https://leetcode.com/problems/unique-number-of-occurrences/
#
# Tags: Array

import timeit
from collections import Counter
from typing import List


# A fast solution is to use Collections.Counter to get the count of
# occurrences of each value, then check if the count of unique values
# equals the total number of values, for example using a set.
#
# Time complexity: O(n)
# Space complexity: O(m) - Where m is the number of unique values in the
# input.
#
# Runtime: 39 ms, faster than 91.14%
# Memory Usage: 14 MB, less than 72.74%
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(c) == len(set(c.values()))


def test():
    executors = [
        Solution,
    ]
    tests = [
        [[1, 2, 2, 1, 1, 3], True],
        [[1, 2], False],
        [[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.uniqueOccurrences(t[0])
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
