# 944. Delete Columns to Make Sorted
# 🟢 Easy
#
# https://leetcode.com/problems/delete-columns-to-make-sorted/
#
# Tags: Array - String

import timeit
from typing import List


# Iterate over the columns, then a nested loop iterates over the strings
# after the first one comparing that string/column character with the
# one on the same position on the previous string, if we find one
# character that does not follow the lexicographical order, we add one
# to the result and break out of the column loop.
#
# Time complexity: O(m*n) - We will visit each character in each string
# in the input.
# Space complexity: O(1) - Constant extra memory used.
#
# Runtime 162 ms Beats 75.16%
# Memory 14.5 MB Beats 93.5%
class Iterative:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        # Iterate over all columns.
        for j in range(len(strs[0])):
            # Iterate over all strings except the first.
            for i in range(1, len(strs)):
                if strs[i][j] < strs[i - 1][j]:
                    res += 1
                    break
        return res


# Use zip to rearrange the strings into lists corresponding to the
# columns, then check that each character has a lexicographical value
# equal or more than the preceding one.
#
# Time complexity: O(m*n) - We will visit each character in each string
# in the input.
# Space complexity: O(m*n) - The zip(*strs) expression makes a copy of
# the input in memory.
#
# Runtime 129 ms Beats 91.16%
# Memory 14.6 MB Beats 61.89%
class BuiltIn:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(
            any(col[i - 1] > col[i] for i in range(1, len(col)))
            for col in zip(*strs)
        )


def test():
    executors = [
        Iterative,
        BuiltIn,
    ]
    tests = [
        [["a", "b"], 0],
        [["zyx", "wvu", "tsr"], 3],
        [["cba", "daf", "ghi"], 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minDeletionSize(t[0])
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
