# 417. Pacific Atlantic Water Flow
# 🟠 Medium
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/
#
# Tags: Array - Depth-First Search - Breath-First Search - Matrix

import timeit
from collections import deque
from typing import Deque, List, Set, Tuple


# Start at all the cells from which the water can flow directly to the
# Pacific, push them into a set and a deque, start processing the queue
# checking if the water can flow from the neighboring cells to the
# North, East, South and West into the cell that we are visiting, for
# cells where it can, push them into the set and the queue.
# Once we are done with the Pacific, do the same with the Atlantic.
# Return the intersection of the sets converting tuples to lists.
#
# Time complexity: O(n) - We visit each element 1 or 2 times.
# Space complexity: O(n) - The queue and the set may grow to the same
# size as the grid.
#
# Runtime: 270 ms, faster than 99.03%
# Memory Usage: 15.5 MB, less than 78.43%
class BFS:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Define a helper function that takes a queue of tuples
        # representing cells in the grid and adds to it all the cells
        # from which water can flow to them.
        def bfs(q: Deque[Tuple[int]], s: Set[Tuple[int]]) -> Set[Tuple[int]]:
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            while q:
                i, j = q.popleft()
                current_height = heights[i][j]
                # Only add neighbors if they are within bounds and the
                # water can flow into this cell from them.
                for dr, dc in directions:
                    row, col = i + dr, j + dc
                    key = (row, col)
                    if (
                        0 <= row < len(heights)
                        and 0 <= col < len(heights[0])
                        and heights[row][col] >= current_height
                        and key not in s
                    ):
                        q.append((row, col))
                        s.add(key)

            return s

        # Use a double ended queue to run BFS.
        p_queue = deque()
        a_queue = deque()
        # Get all the initial points from which the water can flow to
        # the pacific, the first row and column of the grid.
        pacific = set()
        atlantic = set()
        # Add the first column to the pacific set and the last to the
        # atlantic set.
        last_col_idx = len(heights[0]) - 1
        for i in range(len(heights)):
            p_queue.append((i, 0))
            a_queue.append((i, last_col_idx))
            pacific.add((i, 0))
            atlantic.add((i, last_col_idx))

        # Add the first row items to the pacific and the last row items
        # to the atlantic.
        last_row_idx = len(heights) - 1
        for j in range(len(heights[0])):
            p_queue.append((0, j))
            a_queue.append((last_row_idx, j))
            pacific.add((0, j))
            atlantic.add((last_row_idx, j))

        # Recursively add points from which the water can flow to the
        # current ones.
        pacific = bfs(p_queue, pacific)
        atlantic = bfs(a_queue, atlantic)

        # Convert the set of tuples to list of lists.
        return [list(point) for point in pacific.intersection(atlantic)]


def test():
    executors = [BFS]
    tests = [
        [
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ],
        [[[2, 1], [1, 2]], [[0, 0], [0, 1], [1, 0], [1, 1]]],
        [[[2, 1]], [[0, 0], [0, 1]]],
        [[[1]], [[0, 0]]],
        [[[3, 3, 4], [3, 2, 3], [4, 3, 3]], [[0, 2], [2, 0]]],
        [[[3, 3, 4], [3, 2, 4], [4, 3, 3]], [[0, 2], [1, 2], [2, 0]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.pacificAtlantic(t[0])
                result.sort()
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
