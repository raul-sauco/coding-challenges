# 999. Available Captures for Rook
# 🟢 Easy
#
# https://leetcode.com/problems/available-captures-for-rook/
#
# Tags: Array - Matrix - Simulation

import timeit
from typing import List


# Iterate over the matrix rows and columns to find the rook, then travel
# on the four directions of movement from the rook's position until we
# either run out of cells to visit, find a bishop, or find a pawn, if
# the latter, add one to the result.
#
# Time complexity: O(1) - We visit all cells, limited to 64, constant
# time O(64) => O(1).
# Space complexity: O(1) - Constant space.
#
# Runtime: 30 ms, faster than 96.32%
# Memory Usage: 13.9 MB, less than 81.84%
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Travel through the board to find the rook.
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    break
            else:
                continue
            break
        res, row, col = 0, i, j
        # Up.
        i = row - 1
        while i >= 0 and board[i][col] != "B":
            if board[i][col] == "p":
                res += 1
                break
            i -= 1
        i = row + 1
        while i < len(board) and board[i][col] != "B":
            if board[i][col] == "p":
                res += 1
                break
            i += 1
        j = col - 1
        while j >= 0 and board[row][j] != "B":
            if board[row][j] == "p":
                res += 1
                break
            j -= 1
        j = col + 1
        while j < len(board[0]) and board[row][j] != "B":
            if board[row][j] == "p":
                res += 1
                break
            j += 1
        return res


def test():
    executors = [
        Solution,
    ]
    tests = [
        [
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", "R", ".", ".", ".", "p"],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
            ],
            3,
        ],
        [
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", "p", "p", "p", "p", "p", ".", "."],
                [".", "p", "p", "B", "p", "p", ".", "."],
                [".", "p", "B", "R", "B", "p", ".", "."],
                [".", "p", "p", "B", "p", "p", ".", "."],
                [".", "p", "p", "p", "p", "p", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
            ],
            0,
        ],
        [
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                ["p", "p", ".", "R", ".", "p", "B", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
            ],
            3,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numRookCaptures(t[0])
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
