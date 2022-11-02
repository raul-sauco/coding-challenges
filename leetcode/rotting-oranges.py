# 994. Rotting Oranges
# 🟠 Medium
#
# https://leetcode.com/problems/rotting-oranges/
#
# Tags: Array - Breadth-First Search - Matrix

import timeit
from collections import deque
from typing import List


# Travel the grid searching for rotten oranges, when one is found,
# spread the rot 4-directionally from there.
#
# Time complexity: O(n) - We consider each element a max of 3 times.
# Space complexity: O(1) - If we don't consider the input grid.
#
# Runtime: 111 ms, faster than 13.10%
# Memory Usage: 14.1 MB, less than 10.19%
class DFSTwoLoops:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Define a recursive function that spreads the rot.
        # If the current row/col position is valid and fresh, or it
        # can be rotted faster via this route, update its value and
        # recursively call the function for its 4 directions.
        def spreadRot(row: int, col: int, step: int):
            # It will take one minute more to spread the rot from here.
            step -= 1
            # Check if we need to rot this cell.
            if grid[row][col] == 1 or grid[row][col] < step:
                grid[row][col] = step
            # Check 4-directionally if it makes sense to spread the rot
            # to that cell. We check if we are within bounds and have an
            # orange that either is fresh or can be rotten quicker from
            # this route.
            if row > 0 and (
                grid[row - 1][col] == 1 or step > grid[row - 1][col]
            ):
                spreadRot(row - 1, col, step)
            if row < len(grid) - 1 and (
                grid[row + 1][col] == 1 or step > grid[row + 1][col]
            ):
                spreadRot(row + 1, col, step)
            if col > 0 and (
                grid[row][col - 1] == 1 or step > grid[row][col - 1]
            ):
                spreadRot(row, col - 1, step)
            if col < len(grid[0]) - 1 and (
                grid[row][col + 1] == 1 or step > grid[row][col + 1]
            ):
                spreadRot(row, col + 1, step)

        # Travel the grid starting at the top-left corner to find rotten
        # oranges and spread the rot from them.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    # Spread the rot 4-directionally.
                    spreadRot(i, j, 1)

        # Set the max time to rot
        max_time_to_rot = 0
        # Travel the matrix to get the value of the orange that took
        # longest to rot, it is the minimum value from the matrix.
        # This loop also checks if there are any oranges that did not
        # rot.
        for row in grid:
            for val in row:
                # If some oranges didn't rot, return -1
                if val == 1:
                    return -1
                # While all oranges did rot, check the longest it took
                if val < max_time_to_rot:
                    max_time_to_rot = val

        return -max_time_to_rot


# Using BFS, we explore the grid and find all rotten and fresh oranges,
# we push the rotten ones into a queue and count the fresh ones.
# After that we start looping through the elements in the queue popping
# rotten oranges and rotting the ones next to them, each time that we
# empty the queue we add 1 unit of time to the counter. When we are
# out of rotten oranges we check if we rotted all fresh oranges. If yes,
# we return the number of units of time it took, if there are fresh
# oranges left, we return -1
#
# Time complexity: O(n) - We visit each element of the grid once.
# Space complexity: O(n) - The queue may grow to the same size as the grid.
#
# Runtime: 78 ms, faster than 58.05%
# Memory Usage: 14 MB, less than 10.19%
class BFS:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Keep elements in a queue.
        queue = deque()
        # Keep count of the number of fresh oranges.
        fresh_oranges = 0
        # Visit all elements of the grid.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Add one to the number of fresh oranges seen.
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    # Append the rotten orange to the queue.
                    queue.append((i, j))

        # Keep track of the time cycle.
        minutes = 0
        # Pop elements from the queue.
        while queue and fresh_oranges:
            minutes += 1
            # Empty the queue of its current elements in this cycle.
            for _ in range(len(queue)):
                # Get the coordinates from the queue
                i, j = queue.popleft()
                # Try to spread the rot from this element.
                # Up
                if 0 < i and grid[i - 1][j] == 1:
                    queue.append((i - 1, j))
                    grid[i - 1][j] = 0
                    fresh_oranges -= 1
                # Down
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    queue.append((i + 1, j))
                    grid[i + 1][j] = 0
                    fresh_oranges -= 1
                # Left
                if 0 < j and grid[i][j - 1] == 1:
                    queue.append((i, j - 1))
                    grid[i][j - 1] = 0
                    fresh_oranges -= 1
                # Right
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    queue.append((i, j + 1))
                    grid[i][j + 1] = 0
                    fresh_oranges -= 1

        # Check if there are any fresh oranges left.
        if fresh_oranges:
            return -1
        # Otherwise return the number of minutes used.
        return minutes


# An improvement over the previous solution, same logic but we use a for
# loop to condense the four directions of travel along which the rot
# can spread.
class BFSForDir:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Keep elements in a queue.
        queue = deque()
        # Keep count of the number of fresh oranges.
        fresh_oranges = 0
        # Visit all elements of the grid.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Add one to the number of fresh oranges seen.
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    # Append the rotten orange to the queue.
                    queue.append((i, j))

        # Define the four possible directions of travel.
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Keep track of the time cycle.
        minutes = 0
        # Pop elements from the queue.
        while queue and fresh_oranges:
            minutes += 1
            # Empty the queue of its current elements in this cycle.
            for _ in range(len(queue)):
                # Get the coordinates from the queue
                i, j = queue.popleft()
                # Use the directions list to compute movements.
                for dr, dc in dir:
                    row, col = i + dr, j + dc
                    if (
                        0 <= row < len(grid)
                        and 0 <= col < len(grid[0])
                        and grid[row][col] == 1
                    ):
                        queue.append((row, col))
                        grid[row][col] = 2
                        fresh_oranges -= 1

        # Check if there are any fresh oranges left.
        if fresh_oranges:
            return -1
        # Otherwise return the number of minutes used.
        return minutes


def test():
    executors = [
        BFS,
        DFSTwoLoops,
        BFSForDir,
    ]
    tests = [
        [[[0]], 0],  # No oranges, return 0
        [
            [
                [2, 1, 1],
                [1, 1, 0],
                [0, 1, 1],
            ],
            4,
        ],
        [
            [
                [2, 1, 1],
                [0, 1, 1],
                [1, 0, 1],
            ],
            -1,
        ],  # (2,0) never rots, return -1
        [[[0, 2]], 0],  # No oranges, return 0
        [
            [
                [2, 1, 1, 0],
                [1, 1, 0, 0],
                [0, 1, 2, 1],
                [0, 1, 1, 1],
            ],
            2,
        ],
        [
            [
                [2, 1, 1, 0],
                [1, 1, 0, 0],
                [0, 1, 2, 1],
                [1, 0, 1, 1],
            ],
            -1,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                # The solutions modify the grid, need to pass a copy.
                # https://stackoverflow.com/a/6533065/2557030
                result = sol.orangesRotting([row[:] for row in t[0]])
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
