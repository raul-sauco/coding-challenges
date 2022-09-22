# 130. Surrounded Regions
# 🟠 Medium
#
# https://leetcode.com/problems/surrounded-regions/
#
# Tags: Array - Depth-First Search - Breath-First Search - Union Find -
# Matrix

import timeit
from collections import deque
from typing import List


# Visit all the cells around the perimeter, any cell with an "O" its
# enqueued to be processed and marked "safe" from capture. Once we are
# done with the perimeter, start visiting the cells in the queue marking
# them safe and enqueueing any adjacent cell that has an "O". When we
# run out of cells in the queue, we know that any other "O" cells are
# not safe from capture, we can visit all cells in the board, any cell
# with an "O" that has not been marked as "safe" gets captured.
#
# Time complexity: O(m*n) - We visit all cells in the board 1 or 2 times.
# Space complexity: O(m*n) - The queue can grow in size linearly with
# the size of the input.
#
# Runtime: 137 ms, faster than 97.70%
# Memory Usage: 15.2 MB, less than 91.46%
class BFS:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        adj = ((0, 1), (0, -1), (1, 0), (-1, 0))
        # Visit all cells in the 4 borders marking all Os in them and
        # all their adjacent Os as safe.
        q = deque()
        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == "O":
                    board[i][j] = "o"
                    q.append((i, j))
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == "O":
                    board[i][j] = "o"
                    q.append((i, j))
        # Process the elements in the queue
        while q:
            i, j = q.popleft()
            # Add valid neighbors to the queue.
            for k, l in adj:
                x, y = i + k, j + l
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    board[x][y] = "o"
                    q.append((x, y))
        # We have marked all positions that cannot be captured, capture
        # the others.
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "o":
                    board[i][j] = "O"
        return board


# TODO add a union find solution.


def test():
    executors = [BFS]
    tests = [
        [[["X"]], [["X"]]],
        [
            [["X", "X"], ["X", "O"], ["X", "X"], ["X", "O"]],
            [["X", "X"], ["X", "O"], ["X", "X"], ["X", "O"]],
        ],
        [
            [
                ["O", "X", "X"],
                ["X", "O", "X"],
                ["X", "X", "O"],
                ["X", "O", "X"],
            ],
            [
                ["O", "X", "X"],
                ["X", "X", "X"],
                ["X", "X", "O"],
                ["X", "O", "X"],
            ],
        ],
        [
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.solve(t[0])
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
