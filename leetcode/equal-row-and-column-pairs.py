# 2352. Equal Row and Column Pairs
# 🟠 Medium
#
# https://leetcode.com/problems/equal-row-and-column-pairs/
#
# Tags: Array - Hash Table - Matrix - Simulation

import timeit
from typing import List


# Use a Trie-like structure, keys are the values in the cells, the mark
# for end-of-word also contains the number of columns that we have
# seen have the exact same sequence of values. First process rows or
# columns inserting all value sequences found, then iterate over the
# other checking for matches.
#
# Time complexity: O(n^2) - Where n is the row/column length, we visit
# twice each value in the grid.
# Space complexity: O(n^2) - We can have one entry in the trie per each
# value in the grid.
#
# Runtime 537 ms Beats 52.11%
# Memory 27 MB Beats 5.10%
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        root = {}
        for row in grid:
            current = root
            for num in row:
                if num not in current:
                    current[num] = {}
                current = current[num]
            if "count" in current:
                current["count"] += 1
            else:
                current["count"] = 1
        res = 0
        # Iterate over the columns.
        for c in range(len(grid[0])):
            current = root
            for r in range(len(grid)):
                num = grid[r][c]
                if num not in current:
                    break
                current = current[num]
            else:
                if "count" in current:
                    res += current["count"]
        return res


def test():
    executors = [Solution]
    tests = [
        [[[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1],
        [[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.equalPairs(t[0])
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
