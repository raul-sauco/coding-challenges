# 286. Walls and Gates
# 🟠 Medium
#
# https://leetcode.com/problems/walls-and-gates/
#
# Tags: Array - Matrix - Breadth-First Search

import timeit
from collections import deque
from typing import List

# Use a variable for this the value that represents infinity in this
# problems.
INF = 2147483647


# Using breadth first search, we first queue all gates, then iterate over
# the queue adding infinity nodes to it, then BFS using the queue, for
# each position in the queue, check which of its neighbors is accessible
# update its value with the distance traveled from the gate and add it
# to the queue to process its neighbors on the next iteration.
#
# Time complexity: O(n) - We visit each node a max of 2 times.
# Space complexity: O(n) - The queue could grow to the same size as the
# matrix.
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]):
        q = deque()
        # Traverse the matrix adding gates to the queue.
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j))
        # Define the possible moves.
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # Process the queue
        while q:
            a, b = q.popleft()
            for dir in directions:
                # Compute the 4 directional positions from the current
                # position and check if we need to update them.
                i, j = tuple(i + j for i, j in zip((a, b), dir))
                if (
                    0 <= i < len(rooms)
                    and 0 <= j < len(rooms[0])
                    and rooms[i][j] == INF
                ):
                    rooms[i][j] = rooms[a][b] + 1
                    q.append((i, j))
        return rooms


def test():
    executors = [Solution]
    tests = [
        [[[-1]], [[-1]]],
        [[[-1], [0]], [[-1], [0]]],
        [[[0, -1], [INF, INF]], [[0, -1], [1, 2]]],
        [
            [
                [INF, -1, 0, INF],
                [INF, INF, INF, -1],
                [INF, -1, INF, -1],
                [0, -1, INF, INF],
            ],
            [
                [3, -1, 0, 1],
                [2, 2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4],
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.wallsAndGates(t[0])
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
