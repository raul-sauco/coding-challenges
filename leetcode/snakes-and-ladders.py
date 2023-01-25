# 909. Snakes and Ladders
# 🟠 Medium
#
# https://leetcode.com/problems/snakes-and-ladders/
#
# Tags: Array - Breadth-First Search - Matrix

import timeit
from heapq import heappop, heappush
from typing import List


# We want to find the minimum distance to travel from a node to another
# in an unweighted directed graph, each node has edges to the following
# 6 nodes and some nodes have extra edges. BFS is a good option to
# travel the unweighted graph because we move one edge at a time and
# count the number of edges (rolls) we take until we land in the target.
#
# Time complexity: O(n^2) - Potentially, from each node we can reach
# any other node but bfs will travel only one path because we only
# enqueue a node the first time we see it. The board is n*n so n^2 cells.
# Space complexity: O(n^2) - The dictionary could end up having one
# entry per cell in the input, the queue can hold an entire level, which
# could be more than half the board, for example in a 3x3 board.
#
# Runtime 105 ms Beats 97.10%
# Memory 14 MB Beats 67.63%
class BFS:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Store the length of one row.
        n = len(board)
        # Store the target index.
        target = n * n
        # Dictionary of {cells visited: number of rolls to land there}.
        visited = {1: 0}
        # A queue of cells that we landed at in the last roll.
        q = [1]
        for start_idx in q:
            for landing_idx in range(start_idx + 1, start_idx + 7):
                # Use the index to compute the corresponding position in
                # the board. This can be used as a template to convert
                # indexes between a flat array and a Boustrophedon style
                # matrix.
                row, col = (landing_idx - 1) // n, (landing_idx - 1) % n
                cell_value = board[~row][col if row % 2 == 0 else ~col]
                # If the cell is the start of a snake or ladder, we will
                # be landing at its end cell.
                if cell_value != -1:
                    landing_idx = cell_value
                # If we land in the target cell, return the number of
                # rolls needed to get there.
                if landing_idx == target:
                    return visited[start_idx] + 1
                # If this is the first time that we land in a given
                # position, mark it as visited and append it to the
                # queue.
                if landing_idx not in visited:
                    visited[landing_idx] = visited[start_idx] + 1
                    q.append(landing_idx)
        return -1


# Runtime 106 ms Beats 96.68%
# Memory 14.4 MB Beats 5.60%
class Dijkstra:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        # Flatten the input board to access snakes and ladders easily.
        cells = [-1] + [
            item
            for i, row in enumerate(reversed(board))
            for item in (row[::-1] if i % 2 else row)
        ]
        least_rolls = [0] + [float("inf")] * (n * n)
        # A recursive function that walks 6 steps from the start
        # branching into any directions that the player could go.
        def move(pos: int, rolls: int, steps: int) -> None:
            if steps == 0 or pos > target:
                return
            # We can reach this position in this many rolls.
            heappush(heap, (rolls, pos))
            # If this position has a snake or a ladder, we can reach
            # that position in the same number of rolls.
            if cells[pos] != -1:
                move(cells[pos], rolls, steps)
            # We can reach the next position with one more move.
            move(pos + 1, rolls, steps - 1)

        # A priority queue with tuples that contain:
        # (number of rolls to get here, position) initialized with the
        # position 1 and 0 rolls.
        heap = [(0, -1)]
        # We are guaranteed to be able to reach the target.
        while heap:
            rolls_prev, start = heappop(heap)
            rolls = rolls_prev + 1
            for i in range(1, 7):
                landing_pos = -start + i
                if cells[landing_pos] != -1:
                    landing_pos = cells[landing_pos]
                if landing_pos == target:
                    return rolls
                # Regular cell.
                if rolls < least_rolls[landing_pos]:
                    least_rolls[landing_pos] = rolls
                    heappush(heap, (rolls, -landing_pos))
        return -1


def test():
    executors = [
        BFS,
        Dijkstra,
    ]
    tests = [
        [[[-1, -1], [-1, 3]], 1],
        [[[1, 1, -1], [1, 1, 1], [-1, 1, 1]], -1],
        [
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ],
            4,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.snakesAndLadders(t[0])
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
