# 980. Unique Paths III
# 🔴 Hard
#
# https://leetcode.com/problems/unique-paths-iii/
#
# Tags: Array - Backtracking - Bit Manipulation - Matrix

import timeit
from typing import List


# One way to solve this problem is to use depth-first search, the two
# points to keep in mind are:
# - We need to be able to determine which cells we have visited already
#   in order to avoid visiting them again.
# - We need to be able to determine if we have visited all the empty
#   cells, once we reach the destination, to decide if the path taken is
# a valid path.
# We can solve the first problem updating the value of the cells when we
# visit them, then resetting it when we backtrack. To determine if we
# have visited all empty cells, we can count them before we start the
# depth-first search, then simply keep count of the number of cells that
# we have visited along the current branch of the dfs.
#
# Time complexity: O(3(m*n)) - At each step we can take up to three
# different paths, not four because we can never go back to the cell
# that we came from.
# Space complexity: O(m*n) - The call stack can grow to the size of the
# input grid.
#
# Runtime 46 ms Beats 98.34%
# Memory 13.8 MB Beats 93.68%
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Sizes and number of empty cells.
        m, n, empties, start = len(grid), len(grid[0]), 1, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empties += 1
                elif grid[i][j] == 1:
                    start = (i, j)
        # Define a depth-first search function that makes all the
        # possible next moves from a given cell and backtracks them.
        def bt(row: int, col: int, remaining_empties: int) -> int:
            # The position is out of bounds or the cell is an obstacle.
            if (
                (not 0 <= row < m)
                or (not 0 <= col < n)
                or grid[row][col] == -1
            ):
                return 0
            # The position is the ending square.
            if grid[row][col] == 2:
                # Check that we have visited all empties.
                return 1 if not remaining_empties else 0
            # The current cell is an empty cell. Mark it visited.
            grid[row][col] = -1
            remaining_empties -= 1
            # Try to visit its neighbors.
            res = sum(
                [
                    bt(row - 1, col, remaining_empties),
                    bt(row + 1, col, remaining_empties),
                    bt(row, col - 1, remaining_empties),
                    bt(row, col + 1, remaining_empties),
                ]
            )
            # Backtrack
            remaining_empties += 1
            grid[row][col] = 0
            return res

        return bt(start[0], start[1], empties)


def test():
    executors = [Solution]
    tests = [
        [[[0, 1], [2, 0]], 0],
        [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4],
        [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.uniquePathsIII(t[0])
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
