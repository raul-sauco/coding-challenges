# 36. Valid Sudoku
# 🟠 Medium
#
# https://leetcode.com/problems/valid-sudoku/
#
# Tags: Array - Hash Table - Matrix

import timeit
from collections import defaultdict
from typing import List


# Maintain a set for each of: row, column, box. When we visit a new
# cell, check if the same value has been seen before in the same row,
# column or box, if yes, return False, the Sudoku is not valid,
# otherwise push the value into the matching sets and continue.
# If we iterate over all the board without finding any invalid value,
# return True
#
# Time complexity: O(1) - We iterate over the board elements and, for
# each, perform some O(1) operations. Since the number of elements on
# the board is limited to 81, constant time. If the number of elements
# did not have a maximum, it would be O(n).
# Space complexity: O(1) - Same reason as above, the number of elements
# is limited to a max of 81, so then is the size of the sets.
#
# Runtime: 124 ms, faster than 72.73%
# Memory Usage: 14 MB, less than 35.50%
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create dictionaries to store numbers that we have seen.
        (rows, cols, boxes) = (
            defaultdict(set),
            defaultdict(set),
            defaultdict(set),
        )

        # Iterate over all the positions on the board adding the value
        # of non-empty cells to the corresponding sets, row, col and
        # section.
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                val = board[row_idx][col_idx]
                # Skip empty cells.
                if val == ".":
                    continue
                sets = [
                    rows[row_idx],
                    cols[col_idx],
                    boxes[(row_idx // 3, col_idx // 3)],
                ]
                # For each corresponding set, check if the same value
                # is already in the set. If not seen, add it.
                for s in sets:
                    if val in s:
                        return False
                    s.add(val)

        # If we can visit all values without finding any conflict, the
        # input is a valid Sudoku.
        return True


def test():
    executors = [Solution]
    tests = [
        [
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        ],
        [
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            False,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.isValidSudoku(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
