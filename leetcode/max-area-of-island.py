# https://leetcode.com/problems/max-area-of-island/


# Tags: Array - Depth-First Search - Breadth-First Search - Union Find - Matrix

import timeit
from collections import defaultdict
from typing import List


# Iterate over the matrix elements one row at a time.
# For each 1 found, check if we need to create a new island or merge it into an existing one
# If the top and left elements belong to different islands, merge them.
#
# Time complexity: O(n*m) where m is the size of the biggest island in the worst case if we need to
# correct the island the points belong to in each iteration
# Space complexity: O(n) for the default dictionary with sets. A maximum of n tuple elements n/2 tuples and
# n/2/island count sets.
#
# Runtime: 1771 ms, faster than 5.02% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.8 MB, less than 73.08% of Python3 online submissions for Max Area of Island.
class Iterative:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = defaultdict(set)
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i > 0 and grid[i - 1][j] > 0) or (
                        j > 0 and grid[i][j - 1] > 0
                    ):
                        # Check what needs to be merged
                        # First merge left
                        if i > 0 and grid[i - 1][j] > 0:
                            key = grid[i - 1][j]
                            islands[key].add((i, j))
                            grid[i][j] = key
                            if j > 0 and grid[i][j - 1] > 0:
                                # Merge the top set with the left set
                                # Update all elements to point to the new set, add them to the new set
                                for element in islands[grid[i][j - 1]]:
                                    islands[key].add(element)
                                    grid[element[0]][element[1]] = key
                        else:
                            # the element to the left is 0 but the one above is part of an island
                            key = grid[i][j - 1]
                            islands[key].add((i, j))
                            grid[i][j] = key

                    else:
                        # Create a new island group under the first free key
                        key = len(islands) + 1
                        islands[key].add((i, j))
                        grid[i][j] = key

                    size = len(islands[key])
                    if size > max_area:
                        max_area = size

        return max_area


# Iterate over the grid positions and, when land is found, calculate the size of the island, using DFS, and mark
# it explored.
#
# Time complexity: O(n) n == rows * cols == num elements in the grid. Each element is visited once
# Space complexity: O(n) The call stack could grow up to the size of the matrix
#
# Runtime: 238 ms, faster than 39.18% of Python3 online submissions for Max Area of Island.
# Memory Usage: 16.5 MB, less than 69.88% of Python3 online submissions for Max Area of Island.
class DFSRecursive:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col) -> int:
            # If out of bounds, water or seen, return 0
            if (
                row < 0
                or row == num_rows
                or col < 0
                or col == num_cols
                or grid[row][col] == 0
            ):
                return 0

            # Otherwise mark it as seen and compute the size of the island recursively
            grid[row][col] = 0
            return (
                1
                + dfs(row - 1, col)
                + dfs(row + 1, col)
                + dfs(row, col - 1)
                + dfs(row, col + 1)
            )

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area


# Similar to the  previous approach but use a loop and stack approach to do DFS instead of recursion.
#
# Time complexity: O(n) - we visit each point on the matrix once
# Space complexity: O(n) - The stack would be of size n in the worst case
#
# Runtime: 218 ms, faster than 50.62% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.3 MB, less than 89.31% of Python3 online submissions for Max Area of Island.
class DFSIterative:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col) -> int:
            # If out of bounds, water or seen, return 0
            if (
                row < 0
                or row == num_rows
                or col < 0
                or col == num_cols
                or grid[row][col] == 0
            ):
                return 0

            # Otherwise mark it as seen and compute the size of the island recursively
            grid[row][col] = 0
            return (
                1
                + dfs(row - 1, col)
                + dfs(row + 1, col)
                + dfs(row, col - 1)
                + dfs(row, col + 1)
            )

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    area = 0
                    stack = [(row, col)]
                    while stack:
                        i, j = stack.pop()
                        # If we haven't visited this point before
                        if grid[i][j]:
                            # Mark this point as visited
                            grid[i][j] = 0
                            # Add to the size
                            area += 1
                            # Add all valid neighbors to the stack
                            if i > 0 and grid[i - 1][j]:
                                stack.append((i - 1, j))
                            if i < num_rows - 1 and grid[i + 1][j]:
                                stack.append((i + 1, j))
                            if j > 0 and grid[i][j - 1]:
                                stack.append((i, j - 1))
                            if j < num_cols - 1 and grid[i][j + 1]:
                                stack.append((i, j + 1))

                    max_area = max(max_area, area)

        return max_area


def test():
    executors = [
        # Iterative,
        # DFSRecursive,
        DFSIterative,
    ]
    tests = [
        [
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1],
            ],
            4,
        ],
        [
            [
                [0, 1],
                [1, 1],
            ],
            3,
        ],
        [[[1, 1]], 2],
        [
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ],
            6,
        ],
        [[[0, 0, 0, 0, 0, 0, 0, 0]], 0],
        [[[1]], 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.maxAreaOfIsland(t[0].copy())
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
