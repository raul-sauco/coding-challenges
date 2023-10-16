# 119. Pascal's Triangle II
# 🟢 Easy
#
# https://leetcode.com/problems/pascals-triangle-ii/
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List


# Iterate over n number of rows, for each row, iterate over the row
# elements backwards computing their new value as the sum of the element
# at the same position plus the one at the previous position on the
# previous row.
#
# Time complexity: O(n^2) - We iterate n rows, for each row, we iterate
# over all the row elements.
# Space complexity: O(n) - We use an extra array of size n.
#
# Runtime 35 ms Beats 77.91%
# Memory 16.04 MB Beats 96.64%
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row


def test():
    executors = [Solution]
    tests = [
        [0, [1]],
        [1, [1, 1]],
        [3, [1, 3, 3, 1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.getRow(t[0])
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
