# 1293. Shortest Path in a Grid with Obstacles Elimination
# 🔴 Hard
#
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
#
# Tags: Array - Breath-First Search - Matrix

import timeit
from collections import deque
from heapq import heappop, heappush
from typing import List


# Use BFS to visit cells in the grid keeping track of combinations of
# row/col/removals that we have seen already.
#
# Time complexity: O(m*n*k) - We may visit each combination of row,
# column and number of removals before we find a solution or decide that
# there isn't one.
# Space complexity: O(m*n*k) - Both the visited set and the queue will
# grow linearly in size with the size of the input.
#
# Runtime: 79 ms, faster than 95.42%
# Memory Usage: 15.3 MB, less than 76.48%
class BFS:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
        # If k is big enough, ignore the obstacles.
        if k > (NUM_ROWS - 1 + NUM_COLS - 1):
            return NUM_ROWS - 1 + NUM_COLS - 1
        # Use a queue of (distance traveled, removals used, row, col)
        q = deque([(0, 0, 0, 0)])
        # The four directions we travel to get to the neighbors.
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # Store combinations that we have pushed into the heap already.
        seen = {(0, 0, 0, 0)}
        while q:
            moves, rem, row, col = q.popleft()
            for x, y in dirs:
                # Get the neighbor's cell row and column.
                n_row, n_col = row + x, col + y
                # If the cell is within bounds.
                if 0 <= n_row < NUM_ROWS and 0 <= n_col < NUM_COLS:
                    dist = moves + 1

                    # If the cell is not an obstacle.
                    if not grid[n_row][n_col]:
                        q_item = (dist, rem, n_row, n_col)
                        set_item = (rem, n_row, n_col)
                        if set_item not in seen:
                            if n_row == NUM_ROWS - 1 and n_col == NUM_COLS - 1:
                                return dist
                            q.append(q_item)
                            seen.add(set_item)
                    elif rem < k:
                        q_item = (dist, rem + 1, n_row, n_col)
                        set_item = (rem + 1, n_row, n_col)
                        if set_item not in seen:
                            q.append(q_item)
                            seen.add(set_item)

        # We could not reach the target.
        return -1


# Use a modified version of Dijkstra where we push into the heap current
# distance traveled plus the number of obstacles removed. We also keep
# track of the best time to get to a cell for each of the possible
# values of k. This is not an optimization over the BFS solution because
# we cannot greedily keep the shortest travel time to a cell without
# taking into account the number of obstacles that we have removed. I am
# keeping this solution here because it was the first one I came up with
# and it passes the tests.
#
# Time complexity: O(m*n*k*log(m*n*k)) - We may visit each combination
# of row/col/removals once, for each, we may push and pop from the heap.
# Space complexity: O(m*n*k) - Both the heap and the dp object can grow
# to that size.
#
# Runtime: 162 ms, faster than 74.62%
# Memory Usage: 19.9 MB, less than 43.79%
class Dijkstra:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
        # If k is big enough, ignore the obstacles.
        if k > (NUM_ROWS - 1 + NUM_COLS - 1):
            return NUM_ROWS - 1 + NUM_COLS - 1
        # Use a heap of (distance traveled, removals used, row, col)
        heap = [(0, 0, 0, 0)]
        # Use a grid of m*n*k size to store the best time to get to each
        # cell while still having k removals.
        dp = [
            [[float("inf") for _ in range(k + 1)] for _ in range(NUM_COLS)]
            for _ in range(NUM_ROWS)
        ]
        dp[0][0] = [0] * (k + 1)
        # The four directions we travel to get to the neighbors.
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # Store combinations that we have pushed into the heap already.
        seen = {(0, 0, 0, 0)}
        # Process positions on the heap while there are still any.
        while heap:
            # removals done, moves taken, row, col
            moves, rem, row, col = heappop(heap)
            for x, y in dirs:
                # Get the neighbor's cell row and column.
                n_row, n_col = row + x, col + y
                # If the cell is within bounds.
                if 0 <= n_row < NUM_ROWS and 0 <= n_col < NUM_COLS:
                    dist = moves + 1
                    # If the cell is not an obstacle.
                    if not grid[n_row][n_col]:
                        # If this distance is better that the previous
                        # best with this number of removals, update it.
                        comb = (dist, rem, n_row, n_col)
                        if dist < dp[n_row][n_col][rem] and comb not in seen:
                            if n_row == NUM_ROWS - 1 and n_col == NUM_COLS - 1:
                                return dist
                            dp[n_row][n_col][rem] = dist
                            # If we update the value, we want to
                            # reprocess travel from this cell.
                            heappush(heap, comb)
                            seen.add(comb)
                    # If the neighbor is an obstacle and we have
                    # removals left on this branch. If we don't have any
                    # removals left, this branch dies.
                    elif rem < k:
                        comb = (dist, rem + 1, n_row, n_col)
                        if comb not in seen:
                            dp[n_row][n_col][rem + 1] = dist
                            heappush(heap, comb)
                            seen.add(comb)
        # We have traveled all possible paths and could not find a way
        # to reach the target cell.
        return -1


def test():
    executors = [
        BFS,
        Dijkstra,
    ]
    tests = [
        [[[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1, -1],
        [[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1, 6],
        [
            [
                [0, 0, 1, 0, 1, 1, 1, 0],
                [1, 1, 0, 1, 0, 1, 0, 0],
                [1, 1, 0, 0, 1, 0, 1, 1],
                [1, 1, 0, 1, 0, 1, 0, 0],
                [1, 0, 0, 1, 0, 1, 0, 1],
                [0, 0, 1, 1, 1, 0, 0, 1],
                [0, 1, 0, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 0, 0, 0, 0, 1],
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 1, 0, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 1, 1],
                [0, 1, 0, 0, 0, 0, 1, 0],
                [1, 1, 1, 0, 1, 0, 0, 0],
                [1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 1, 0, 0, 1, 0],
                [1, 1, 1, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 1, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 0, 0, 0, 1, 1],
                [0, 1, 0, 0, 1, 0, 0, 1],
                [1, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 1, 0],
            ],
            3,
            -1,
        ],
        [
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
                [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
            ],
            27,
            24,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.shortestPath(t[0], t[1])
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
