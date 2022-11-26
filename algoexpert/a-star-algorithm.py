# A* Algorithm
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/a*-algorithm
#
# Tags: Famous Algorithms

import timeit
from heapq import heappop, heappush
from typing import List


# Implement the A* algorithm.
#
# Time complexity: O(m*n*log(m*n)) - Where m is the number of rows and
# n is the number of columns in the input graph. We may visit each
# cell in the graph and push/pop them all from the priority queue.
# Space complexity: O(m*n) - The priority queue could hold one element
# per cell in the input.
class Solution:
    def aStarAlgorithm(
        self,
        startRow: int,
        startCol: int,
        endRow: int,
        endCol: int,
        graph: List[int],
    ) -> List[List[int]]:
        # Define a helper function that computes the Manhattan distance
        # between a cell in the graph and the destination.
        def md(r, c) -> int:
            return abs(r - endRow) + abs(c - endCol)

        # Define a function that reconstructs and returns the shortest
        # path found from start to end.
        def reconstructPath():
            path = [(endRow, endCol)]
            while path[-1][0] != startRow or path[-1][1] != startCol:
                path.append(cameFrom[path[-1]])
            return [list(cell) for cell in reversed(path)]

        # A priority queue of known nodes in the form of a tuple
        # (Manhattan distance, row, col).
        heap = [(md(startRow, startCol), startRow, startCol)]
        # Store each node's visited predecessor along the shortest path.
        cameFrom = {}
        # For node n, gScore[n] is the cost of the cheapest path from
        # start to n currently known.
        gScore = {
            (r, c): float("inf")
            for c in range(len(graph[0]))
            for r in range(len(graph))
        }
        gScore[(startRow, startCol)] = 0

        while heap:
            _, r, c = heappop(heap)
            if r == endRow and c == endCol:
                return reconstructPath()
            # Otherwise, visit the neighbors.
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                # If within bounds and not an obstacle.
                if (
                    0 <= i < len(graph)
                    and 0 <= j < len(graph[0])
                    and graph[i][j] == 0
                ):
                    gs = gScore[(r, c)] + 1
                    if gs < gScore[(i, j)]:
                        # This path to neighbor is better than any
                        # previous one. Record it.
                        cameFrom[(i, j)] = (r, c)
                        gScore[(i, j)] = gs
                        heappush(heap, (gs + md(i, j), i, j))
        return []


def test():
    executors = [Solution]
    tests = [
        [
            0,
            1,
            2,
            4,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 1],
                [0, 2],
                [0, 3],
                [0, 4],
                [1, 4],
                [2, 4],
            ],
        ],
        [
            0,
            1,
            2,
            4,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 1],
                [0, 0],
                [1, 0],
                [2, 0],
                [2, 1],
                [2, 2],
                [2, 3],
                [2, 4],
            ],
        ],
        [
            0,
            1,
            4,
            3,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 1, 1],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 1],
                [0, 0],
                [1, 0],
                [2, 0],
                [2, 1],
                [3, 1],
                [4, 1],
                [4, 2],
                [4, 3],
            ],
        ],
        [
            1,
            1,
            18,
            17,
            [
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
                [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            ],
            [],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.aStarAlgorithm(t[0], t[1], t[2], t[3], t[4])
                exp = t[5]
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
