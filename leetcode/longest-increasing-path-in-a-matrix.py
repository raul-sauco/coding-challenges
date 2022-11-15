# 329. Longest Increasing Path in a Matrix
# 🔴 Hard
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
#
# Tags: Array - Dynamic Programming - Depth-First Search - Breadth-First
# Search - Graph - Topological Sort - Memoization - Matrix

import timeit
from collections import deque
from functools import cache
from typing import List


# One way to go about solving this problem is to visit each position in
# the matrix and checking what is the longest increasing path that we
# can take from there.
#
# Time complexity: O(4^(m*n)) - At each point we can take a maximum of 4
# different choices.
# Space complexity: O(m*n) - The seen dictionary and the call stack can
# both end up holding all the matrix elements.
class BruteForce:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        seen = set()

        def dfs(row, col) -> int:
            seen.add((row, col))
            # The smallest path is this cell by itself.
            longest = 1
            for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                i, j = row + x, col + y
                if (
                    0 <= i < len(matrix)
                    and 0 <= j < len(matrix[0])
                    and (i, j) not in seen
                    and matrix[i][j] > matrix[row][col]
                ):
                    longest = max(longest, 1 + dfs(i, j))
            seen.remove((row, col))
            return longest

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res


# Once we realize that we are not required to keep track of the cells
# that have been visited, because any cells with values greater than the
# current cell, the only ones that we want to visit, could not have been
# visited previously in the strictly increasing path, since their value
# is greater than the current cell's, the problem becomes much simpler
# and easier to memoize, we only need to store the longest combination
# that can be built from any (row, col) combination.
#
# Time complexity: O(m*n) - We will compute the path from each cell only
# once, once we have it, it gets cached.
# Space complexity: O(m*n) - We are storing one path value for each cell
# in the matrix.
#
# Runtime: 524 ms, faster than 86.63%
# Memory Usage: 19.4 MB, less than 18.60%
class Memoization:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0

        @cache
        def dfs(row, col) -> int:
            # The smallest path is this cell by itself.
            longest = 1
            for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                i, j = row + x, col + y
                if (
                    0 <= i < len(matrix)
                    and 0 <= j < len(matrix[0])
                    and matrix[i][j] > matrix[row][col]
                ):
                    longest = max(longest, 1 + dfs(i, j))
            return longest

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res


# Construct a directed acyclic graph using the elements in the matrix
# based on the possible travel between cells given the constrains of the
# problem. Iterate over the matrix storing the indegree of a given cell
# in an auxiliary matrix, use a q to do BFS, add all elements with a 0
# indegree to the queue in this iteration. Then start visiting adjacent
# cells using BFS while keeping track of the path length. When we visit
# a cell, we decrease their indegree by 1, once it reaches 0, we add it
# to the queue to be processed.
#
# Time complexity: O(m*n) - We visit each cell once during preprocessing
# and once during BFS.
# Space complexity: O(m*n) - The auxiliary matrix is the same size as
# the input, the queue could grow to the same size as the input.
#
# Runtime: 489 ms, faster than 90.38%
# Memory Usage: 14.8 MB, less than 89.47%
class TopologicalSorting:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        NUM_ROWS, NUM_COLS, q = len(matrix), len(matrix[0]), deque([])
        # Store cells indegree in a matrix.
        indegree = [[0] * NUM_COLS for _ in range(NUM_ROWS)]
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                incoming = 0
                for r, c in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if (
                        0 <= r < NUM_ROWS
                        and 0 <= c < NUM_COLS
                        and matrix[r][c] < matrix[i][j]
                    ):
                        # We could travel from (r, c) to (i, j)
                        incoming += 1
                if not incoming:
                    q.append((i, j))
                else:
                    indegree[i][j] = incoming
        res = 0
        while q:
            res += 1
            # Pop an entire level.
            for _ in range(len(q)):
                i, j = q.popleft()
                for r, c in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if (
                        0 <= r < NUM_ROWS
                        and 0 <= c < NUM_COLS
                        and matrix[r][c] > matrix[i][j]
                    ):
                        # We could travel from (i, j) to (r, c)
                        indegree[r][c] -= 1
                        # We are only interested in the longest path,
                        # wait until we arrive at this cell from the
                        # longest possible incoming path before
                        # processing it, i.e. adding it to the queue.
                        if not indegree[r][c]:
                            q.append((r, c))
        return res


def test():
    executors = [
        # BruteForce,
        Memoization,
        TopologicalSorting,
    ]
    tests = [
        [[[1]], 1],
        [[[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4],
        [[[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4],
        [
            [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
                [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
                [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
                [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
                [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
                [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
                [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
                [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
                [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
                [119, 118, 117, 116, 115, 114, 113, 112, 111, 110],
                [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
                [139, 138, 137, 136, 135, 134, 133, 132, 131, 130],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            140,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestIncreasingPath(t[0])
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
