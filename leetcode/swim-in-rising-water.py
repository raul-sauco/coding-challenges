# 778. Swim in Rising Water
# 🔴 Hard
#
# https://leetcode.com/problems/swim-in-rising-water/
#
# Tags: Array - Binary Search - Depth-First Search - Breadth-First Search
# Union Find - Heap (Priority Queue) - Matrix

import timeit
from heapq import heappop, heappush
from typing import List


# We can use a modified version of Dijkstra to solve this problem, we
# start at 0, 0 and start visiting its neighbors, each time we visit a
# neighbor, we compute the fastest time at which we can get there and
# push it, together with its coordinates, into a min heap, once we have
# visited all the neighbors of the current cell, we pop the next one
# from the heap. Since we are always popping the cell that we can visit
# fastest, we know that we will be updating their neighbors with the
# fastest time possible to arrive at that cell.
#
# Time complexity: O(n^2*log(n)) - We may push and pop each cell into
# the heap at a log(n^2) cost, equivalent to 2*log(n).
# Space complexity: O(n^2) - Both the heap and the copy of the grid
# can, or do, have n*n elements.
#
# Runtime: 110 ms, faster than 93.76%
# Memory Usage: 14.3 MB, less than 97.32%
class Dijkstra:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # The size of the square grid N == NUM_ROWS == NUM_COLS.
        N = len(grid)
        # Make a copy of the graph with current best distances.
        board = [[float("inf")] * N for _ in range(N)]
        # Use a heap of tuples for nodes we need to visit.
        # (distance, row_idx, col_idx)
        # Push the first node and update the best time in which we can
        # get to it.
        heap = [(grid[0][0], 0, 0)]
        board[0][0] = grid[0][0]
        while heap:
            _, r, c = heappop(heap)
            # Mark this node as visited.
            # board[r][c] = dis
            # The 4 possible directions of travel.
            dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for i, j in dir:
                # If still within boundaries and we haven't visited it
                # previously.
                if (
                    0 <= r + i < N
                    and 0 <= c + j < N
                    and board[r + i][c + j] == float("inf")
                ):
                    # The cost will be the max of the current cost and
                    # the height of the cell we want to visit.
                    cost = max(grid[r + i][c + j], board[r][c])
                    # If we are at the target cell, return this value.
                    if r + i == c + j == N - 1:
                        return cost
                    # Otherwise, push this cell into the heap to visit
                    # it when its distance is the shortest in the heap.
                    heappush(heap, (cost, r + i, c + j))
                    board[r + i][c + j] = cost
        # For boards where we don't iterate over neighbors, return here.
        return board[-1][-1]


# Optimize the previous solution getting rid of the copy grid and
# mutating the input instead to mark visited nodes.
#
# Time complexity: O(n^2*log(n)) - We may push and pop each cell into
# the heap at a log(n^2) cost, equivalent to 2*log(n).
# Space complexity: O(n^2) - The heap can still grow to the same size
# as the input.
#
# Runtime: 247 ms, faster than 32.54%
# Memory Usage: 14.3 MB, less than 94.85%
class DijkstraOptimized:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # The size of the square grid N == NUM_ROWS == NUM_COLS.
        N = len(grid)
        # Base case.
        if N == 1:
            return grid[0][0]
        # Use a heap of tuples for nodes we need to visit. Push 0,0.
        heap = [(grid[0][0], 0, 0)]
        grid[0][0] = -1
        while heap:
            dis, r, c = heappop(heap)
            # The 4 possible directions of travel.
            for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                # If still within boundaries and we haven't visited it
                # previously.
                if (
                    0 <= r + i < N
                    and 0 <= c + j < N
                    and grid[r + i][c + j] != -1
                ):
                    # The cost will be the max of the current cost and
                    # the height of the cell we want to visit.
                    cost = max(grid[r + i][c + j], dis)
                    # If we are at the target cell, return this value.
                    if r + i == c + j == N - 1:
                        return cost
                    # Otherwise, push this cell into the heap.
                    heappush(heap, (cost, r + i, c + j))
                    # Mark the cell as visited.
                    grid[r + i][c + j] = -1


def test():
    executors = [
        Dijkstra,
        DijkstraOptimized,
    ]
    tests = [
        [[[0]], 0],
        [[[0, 2], [1, 3]], 3],
        [
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ],
            16,
        ],
        [
            [
                [0, 1, 4, 3, 4],
                [24, 2, 22, 21, 5],
                [22, 23, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ],
            18,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.swimInWater(t[0])
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
