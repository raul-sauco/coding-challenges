# Remove Islands
# 🟠 Medium
#
# https://www.algoexpert.io/questions/remove-islands
#
# Tags: Array - Matrix - Graph - Depth-First Search

import timeit
from typing import List


# Use depth first search to mark all island cells 4 directionally
# adjacent to a cell in the edge of the matrix as safe, then visit all
# cells in the matrix removing any island that has not been marked as
# safe.
#
# Time complexity: O(m*n) - Where m is the number of rows and n is the
# number of columns.
# Space complexity: O(1) - The exercise asks us to mutate the input
# matrix in place, if we didn't want to we could create a copy using
# O(m*n) memory.
class Solution:
    def removeIslands(self, matrix: List[List[int]]) -> List[List[int]]:
        NUM_ROWS, NUM_COLS = len(matrix), len(matrix[0])
        # Define a function that turns all 1s of a given island into 2s.
        def dfs(r: int, c: int) -> None:
            # Mark this cell as adjacent to the edge.
            matrix[r][c] = 2
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for rc, cc in dir:
                tr = r + rc
                tc = c + cc
                if (
                    0 <= tr < NUM_ROWS
                    and 0 <= tc < NUM_COLS
                    and matrix[tr][tc] == 1
                ):
                    dfs(tr, tc)

        # Update all 1s adjacent to a border.
        for c in range(NUM_COLS):
            if matrix[0][c]:
                dfs(0, c)
            if matrix[NUM_ROWS - 1][c]:
                dfs(NUM_ROWS - 1, c)
        for r in range(NUM_ROWS):
            if matrix[r][0]:
                dfs(r, 0)
            if matrix[r][NUM_COLS - 1]:
                dfs(r, NUM_COLS - 1)

        # Remove the islands.
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if matrix[r][c] == 1:
                    matrix[r][c] = 0
                elif matrix[r][c] == 2:
                    matrix[r][c] = 1

        return matrix


def test():
    executors = [Solution]
    tests = [
        [[[1]], [[1]]],
        [
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
        ],
        [
            [
                [1, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 1],
                [0, 0, 1, 0, 1, 0],
                [1, 1, 0, 0, 1, 0],
                [1, 0, 1, 1, 0, 0],
                [1, 0, 0, 0, 0, 1],
            ],
            [
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1],
            ],
        ],
        [
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.removeIslands(t[0])
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
