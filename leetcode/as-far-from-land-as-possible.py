# 1162. As Far from Land as Possible
# 🟠 Medium
#
# https://leetcode.com/problems/as-far-from-land-as-possible/
#
# Tags: Array - Dynamic Programming - Breadth-First Search - Matrix

import timeit
from typing import List


# Use BFS and a matrix with the current shortest distance between any
# cell and land to compute the shortest distance between any cell and
# land, we will only revisit cells when the new distance to land is
# less than the shortest previous distance found, which may, in turn,
# influence its neighbors by providing a shorter path to land.
#
# Time complexity: O(m+n) - We can travel a maximum of n levels, on each
# level, we will only visit cells to which we have not previously found
# a shorter route, in total we will visit m*n cells during the BFS.
# Space complexity: O(m+n) - The distance matrix has the same size as
# the input matrix, m rows and n columns.
#
# Runtime 548 ms Beats 82.97%
# Memory 14.6 MB Beats 64.75%
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # A matrix of distances to land.
        dist = [[float("inf")] * n for _ in range(m)]
        # Use a stack to do a per-level BFS.
        current_level, level = [], 0
        # Add land cells to the first level.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    current_level.append((i, j))
                    # Mark this cell as 0 units away from land.
                    dist[i][j] = 0
        # If the grid has no water or land, return -1.
        if not len(current_level) or len(current_level) == (m * n):
            return -1
        # Keep exploring as long as the current level has any elements.
        while current_level:
            next_level = []
            level += 1
            # Process one level at a time.
            for _ in range(len(current_level)):
                r, c = current_level.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    # The cell needs to be within boundaries, it should
                    # not be land and we should not have a shorter path
                    # to land already.
                    if 0 <= nr < m and 0 <= nc < n and level < dist[nr][nc]:
                        dist[nr][nc] = level
                        next_level.append((nr, nc))
            current_level = next_level
        return level - 1


def test():
    executors = [Solution]
    tests = [
        [[[1]], -1],
        [[[0]], -1],
        [[[0, 0], [0, 0], [0, 0]], -1],
        [[[1, 1], [1, 1], [1, 1]], -1],
        [[[1, 0], [0, 0], [1, 0]], 2],
        [[[1, 0, 1], [0, 0, 0], [1, 0, 1]], 2],
        [[[1, 0, 0], [0, 0, 0], [0, 0, 0]], 4],
        [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], -1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxDistance(t[0])
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
