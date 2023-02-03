# 1091. Shortest Path in Binary Matrix
# 🟠 Medium
#
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
#
# Tags: Array - Breadth-First Search - Matrix - A* Algorithm

import timeit
from collections import deque
from heapq import heappop, heappush
from typing import List


# When we want to calculate shortest paths in a matrix, one of the best
# algorithms is BFS, we can make it even more efficient if we do BFS
# from both the end and the start.
#
# Time complexity: O(n) - Breadth-first search will process nodes one
# level at a time, it could visit all cells in the grid.
# Space complexity: O(log(n)) - The queue will hold at most log(n) cells
# at one time, one level.
#
# Runtime 553 ms Beats 92.57%
# Memory 14.7 MB Beats 58.96%
class BFS:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Base case the start of end cells are not accessible.
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1
        # A queue from the start position and a queue from the end
        # position.
        qa = deque([(0, 0)])
        qb = deque([(n - 1, n - 1)])
        # A set of nodes visited from the start and nodes visited from
        # the end.
        va, vb = set([(0, 0)]), set([(n - 1, n - 1)])
        # Define a function that returns neighbors of a cell that need
        # to be visited.
        def getNeighbors(row, col):
            cells, moves = [], (-1, 0, 1)
            for i in moves:
                for j in moves:
                    cell = (row + i, col + j)
                    if (
                        0 <= cell[0] < n
                        and 0 <= cell[1] < n
                        and grid[cell[0]][cell[1]] == 0
                        and (i or j)
                    ):
                        cells.append(cell)
            return cells

        # The number of levels that we have traveled.
        l = 0
        # If one of the queues is empty, the path is blocked.
        while qa and qb:
            l += 1
            # Consume the entire level in qa.
            for _ in range(len(qa)):
                ra, ca = qa.popleft()
                for nei in getNeighbors(ra, ca):
                    # If we have visited this cell from the end, return the
                    # number of visited cells.
                    if nei in vb:
                        return 2 * l
                    # If we have visited this cell from the start already,
                    # skip it, otherwise process it.
                    if nei not in va:
                        qa.append(nei)
                        va.add(nei)
            # Consume the entire level in qb.
            for _ in range(len(qb)):
                rb, cb = qb.popleft()
                for nei in getNeighbors(rb, cb):
                    if nei in va:
                        return 2 * l + 1
                    if nei not in vb:
                        qb.append(nei)
                        vb.add(nei)
        return -1


# Another efficient approach would be to use the A* algorithm, it uses
# an heuristic to greedily start exploring cells that are more likely to
# get us to the destination faster than if we explored all cells in each
# level.
#
# Time complexity: O(n*log(n)) - With n the number of cells in the grid,
# we could push/pop each cell in and out of the heap, each operation has
# a log(n) cost.
# Space complexity: O(n) - The score structure has one entry per cell.
#
# Runtime 639 ms Beats 74.57%
# Memory 16.8 MB Beats 5.91%
class AStarSolution:
    def shortestPathBinaryMatrix(self, grid: List[int]) -> List[List[int]]:
        # Define a helper function that computes the heuristic distance
        # between a cell in the graph and the destination. A valid
        # heuristic is the maximum of the rows, cols left to the
        # destination.
        def getDist(r, c) -> int:
            return -min(r, c)
            # Equivalent to return min((n - 1 - r), n - 1 - c)

        # Define a function that reconstructs the path traveled and
        # returns the number of cells visited.
        def pathLength():
            path = [(endRow, endCol)]
            while path[-1][0] != startRow or path[-1][1] != startCol:
                path.append(cameFrom[path[-1]])
            return len(path)

        # Define a function that returns neighbors of a cell that need
        # to be visited.
        def getNeighbors(row, col):
            cells, moves = [], (-1, 0, 1)
            for i in moves:
                for j in moves:
                    cell = (row + i, col + j)
                    if (
                        0 <= cell[0] < n
                        and 0 <= cell[1] < n
                        and grid[cell[0]][cell[1]] == 0
                        and (i or j)
                    ):
                        cells.append(cell)
            return cells

        # The grid is square.
        n = len(grid)
        # For this problem, start and end are the grid corners.
        startRow, startCol, endRow, endCol = 0, 0, n - 1, n - 1
        # Base case, gridlock.
        if grid[startRow][startCol] == 1 or grid[endRow][endCol] == 1:
            return -1
        # A priority queue of known nodes in the form of a tuple
        # (Manhattan distance, row, col).
        heap = [(getDist(startRow, startCol), startRow, startCol)]
        # Store each node's visited predecessor along the shortest path.
        cameFrom = {}
        # For node n, gScore[n] is the cost of the cheapest path from
        # start to n currently known.
        gScore = {
            (r, c): float("inf")
            for c in range(len(grid[0]))
            for r in range(len(grid))
        }
        gScore[(startRow, startCol)] = 0

        while heap:
            _, r, c = heappop(heap)
            if r == endRow and c == endCol:
                return pathLength()
            # Otherwise, visit the neighbors.
            for i, j in getNeighbors(r, c):
                # If within bounds and not an obstacle.
                if (
                    0 <= i < len(grid)
                    and 0 <= j < len(grid[0])
                    and grid[i][j] == 0
                ):
                    gs = gScore[(r, c)] + 1
                    if gs < gScore[(i, j)]:
                        # This path to neighbor is better than any
                        # previous one. Record it.
                        cameFrom[(i, j)] = (r, c)
                        gScore[(i, j)] = gs
                        heappush(heap, (gs + getDist(i, j), i, j))
        return -1


def test():
    executors = [
        BFS,
        AStarSolution,
    ]
    tests = [
        [[[0]], 1],
        [[[0, 1], [1, 0]], 2],
        [[[0, 0, 0], [1, 0, 0], [1, 1, 0]], 3],
        [[[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4],
        [[[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1],
        [
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            5,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.shortestPathBinaryMatrix(t[0])
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
