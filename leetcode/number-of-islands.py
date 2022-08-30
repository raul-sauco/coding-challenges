# 200. Number of Islands
# 🟠 Medium
#
# https://leetcode.com/problems/number-of-islands/
#
# Tags: Array - Depth-First Search - Breath-First Search - Union Find - Matrix

import timeit
from typing import List


# Iterate over the grid rows and columns until we find land. When we
# find land, iterate over that land turning all connected land to water,
# to mark it as seen.
#
# Time complexity: O(n) - We visit water positions once, land positions
# a max of 2 times. Linear to the size of the input.
# Space complexity: O(n) - The stack could grow to the same size as the
# input matrix, for example if al cells had land.
#
# Runtime: 262 ms, faster than 99.74%
# Memory Usage: 16.4 MB, less than 82.01%
class IterativeDFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if grid[row_idx][col_idx] == "1":
                    res += 1
                    # Mark all connected land as "seen".
                    # We can use 0 for that, we don't care to
                    # differentiate "water" and "seen"
                    stack = [(row_idx, col_idx)]
                    while stack:
                        i, j = stack.pop()
                        grid[i][j] = "0"
                        if i > 0 and grid[i - 1][j] == "1":
                            stack.append((i - 1, j))
                        if i < num_rows - 1 and grid[i + 1][j] == "1":
                            stack.append((i + 1, j))
                        if j > 0 and grid[i][j - 1] == "1":
                            stack.append((i, j - 1))
                        if j < num_cols - 1 and grid[i][j + 1] == "1":
                            stack.append((i, j + 1))

        return res


def test():
    executors = [IterativeDFS]
    tests = [
        [[["1"]], 1],
        [[["0"]], 0],
        [
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ],
        [
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numIslands(t[0])
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
