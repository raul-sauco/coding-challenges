# 542. 01 Matrix
# 🟠 Medium
#
# https://leetcode.com/problems/01-matrix/
#
# Tags: Array - Dynamic Programming - Breadth-First Search - Matrix

import timeit
from typing import List


# Use BFS and a matrix with the current shortest distance between any
# cell and land to compute the shortest distance between any cell and
# land, we will only process cells the first time that we land in them
# because the level keeps increasing.
#
# Time complexity: O(m+n) - We will visit m*n cells.
# Space complexity: O(m+n) - The distance matrix has the same size as
# the input matrix, m rows and n columns.
#
# Runtime 654 ms Beats 73.33%
# Memory 17.3 MB Beats 41.48%
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[float("inf")] * n for _ in range(m)]
        current_level, level = [], 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    current_level.append((i, j))
                    dist[i][j] = 0
        while current_level:
            next_level = []
            level += 1
            # Process all cells at this level.
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
        return dist


def test():
    executors = [Solution]
    tests = [
        [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]],
        [[[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.updateMatrix(t[0])
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
