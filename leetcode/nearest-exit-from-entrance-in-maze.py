# 1926. Nearest Exit from Entrance in Maze
# 🟠 Medium
#
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
#
# Tags: Array - Breadth-First Search - Matrix

import timeit
from collections import deque
from typing import List


# Use BFS to visit cells one level at a time from the entrance, if we
# detect an exit, return the number of steps up to that point, if we
# run out of cells to visit and cannot detect an exit, return -1.
#
# Time complexity: O(m*n) - We will visit each cell once, there are m
# rows and n columns.
# Space complexity: O(m*n) - We could end up adding n/2 cells to the
# queue.
#
# Runtime: 749 ms, faster than 97.63%
# Memory Usage: 14.7 MB, less than 55.57%
class BFS:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Use BFS, count the steps needed.
        q = deque([entrance])
        # Mark cells we visit as visited.
        maze[entrance[0]][entrance[1]] = "+"
        steps = 0
        while q:
            steps += 1
            # Pop an entire level.
            for _ in range(len(q)):
                r, c = q.popleft()
                # Try to move in the four directions from this cell.
                for i, j in ((r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= i < len(maze)
                        and 0 <= j < len(maze[0])
                        and maze[i][j] == "."
                    ):
                        # Check if this is an exit.
                        if (
                            i == 0
                            or j == 0
                            or i == len(maze) - 1
                            or j == len(maze[0]) - 1
                        ):
                            return steps
                        # If not an exit, push it into the queue and mark
                        # visited, if we use the number of steps, it
                        # improves visualization on the debugger.
                        maze[i][j] = steps  # "+"
                        q.append((i, j))
        # If we cannot arrive at any exit, return -1
        return -1


def test():
    executors = [
        BFS,
    ]
    tests = [
        # [[[".", "+"]], [0, 0], -1],
        # [[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0], 2],
        # [
        #     [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
        #     [1, 2],
        #     1,
        # ],
        [
            [
                ["+", ".", "+", "+", "+", "+", "+"],
                ["+", ".", "+", ".", ".", ".", "+"],
                ["+", ".", "+", ".", "+", ".", "+"],
                ["+", ".", ".", ".", ".", ".", "+"],
                ["+", "+", "+", "+", ".", "+", "."],
            ],
            [0, 1],
            7,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.nearestExit(t[0], t[1])
                exp = t[2]
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
