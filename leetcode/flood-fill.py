# https://leetcode.com/problems/flood-fill/

import timeit
from collections import deque
from typing import List

# Tags: Array - Depth-First Search - Breadth-First Search - Matrix

# 1e4 calls
# » BFSIdiomatic        0.02159   seconds
# » BFSIterative        0.02747   seconds
# » DFSRecursion        0.04758   seconds
# » DFSRecPythonic      0.05156   seconds

# Improve the algorithm using a queue to store pixels that need to be visited and a set to mark pixels as already visited.
# This is an improvement over keeping an n-size call stack.
#
# Runtime: 109 ms, faster than 57.10% of Python3 online submissions for Flood Fill.
# Memory Usage: 14 MB, less than 90.12% of Python3 online submissions for Flood Fill.
class BFSIterative:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        match_color, m, n = image[sr][sc], len(image), len(image[0])
        if match_color == color:
            return image

        # Use a queue for elements waiting to be processed
        queue = deque([(sr, sc)])

        # While there are elements in the queue, get the next one
        while queue:
            x, y = queue.popleft()

            # Update its color
            image[x][y] = color

            # We don't need to store visited positions in a set. We can check the color, if we have visited, it will
            # have been updated to `color`. We can merge this check with checking that it has `match_color`
            # and only worry about pixels that match the pre-replaced color of the target pixel.

            # Then append the neighbors that should be updated and are within image bounds
            if x > 0 and image[x - 1][y] == match_color:
                queue.append((x - 1, y))
            if x < m - 1 and image[x + 1][y] == match_color:
                queue.append((x + 1, y))
            if y > 0 and image[x][y - 1] == match_color:
                queue.append((x, y - 1))
            if y < n - 1 and image[x][y + 1] == match_color:
                queue.append((x, y + 1))

        return image


# This is a, in my opinion, more readable version, using a for loop to pass the positions that we need to check.
#
# Time complexity O(n) - we might end up visiting every pixel at most once
# Space complexity O(n) - we may have every pixel on the queue depending on the shape of the input matrix
#
# Runtime: 71 ms, faster than 98.93% of Python3 online submissions for Flood Fill.
# Memory Usage: 14 MB, less than 65.80% of Python3 online submissions for Flood Fill.
class BFSIdiomatic:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        match_color, m, n = image[sr][sc], len(image), len(image[0])

        # If the color is the same, we don't need to do anything. We would only `update` pixels with the same value as
        # the target color.
        if match_color == color:
            return image

        # Use a queue for elements waiting to be processed
        queue = deque([(sr, sc)])
        queued = {(sr, sc)}

        # While there are elements in the queue, pop the next one
        while queue:
            x, y = queue.popleft()

            # Update its color
            image[x][y] = color

            # Instead of checking individually, use a for loop to check the four target positions
            # This method has the extra advantage that it would be easier to add positions to be checked,
            # i.e. the diagonals.
            for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):

                # Check if this position would be within bounds, it has the match color and it has not been queued already
                if (
                    0 <= a < m
                    and 0 <= b < n
                    and image[a][b] == match_color
                    and (a, b) not in queued
                ):
                    queued.add((a, b))
                    queue.append((a, b))

        return image


# Naively, we recursively call the function for all pixels connected to the given one
#
# Time complexity O(n) - we might end up visiting every pixel at most once
# Space complexity O(n) - we may have a function call for every pixel on the call stack
#
# Runtime: 94 ms, faster than 72.21% of Python3 online submissions for Flood Fill.
# Memory Usage: 14.2 MB, less than 13.89% of Python3 online submissions for Flood Fill.
class DFSRecursion:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        match_color = image[sr][sc]

        def colorFromPixel(sr: int, sc: int):
            # Color only pixels that are the same color as the selected pixel
            if image[sr][sc] == match_color:
                image[sr][sc] = color
                if sr > 0 and image[sr - 1][sc] == match_color:
                    colorFromPixel(sr - 1, sc)
                if sr < len(image) - 1 and image[sr + 1][sc] == match_color:
                    colorFromPixel(sr + 1, sc)
                if sc > 0 and image[sr][sc - 1] == match_color:
                    colorFromPixel(sr, sc - 1)
                if sc < len(image[0]) - 1 and image[sr][sc + 1] == match_color:
                    colorFromPixel(sr, sc + 1)

        if match_color != color:
            colorFromPixel(sr, sc)
        return image


# Same as above but use some python idioms
#
# This solution is nice to show how to use some python idioms but it is less efficient because it calls the recursive
# function more times than the previous solution.
# The check to see if the position is valid takes place after the function has been called, this means that the function
# gets called for positions with invalid indexes. In a big table this probably results in a big performance hit even
# though the complexity remains the same.
class DFSRecPythonic:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]

        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][
                col
            ] != orig_color:
                return
            image[row][col] = color
            [
                traverse(row + x, col + y)
                for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))
            ]

        if orig_color != color:
            traverse(sr, sc)
        return image


def test():
    executors = [BFSIdiomatic, BFSIterative, DFSRecursion, DFSRecPythonic]
    tests = [
        [
            [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
            1,
            1,
            2,
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ],
        [
            [[1, 1, 1], [1, 1, 0], [1, 1, 1]],
            1,
            1,
            2,
            [[2, 2, 2], [2, 2, 0], [2, 2, 2]],
        ],
        [[[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]],
        [[[0]], 0, 0, 1, [[1]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.floodFill(t[0], t[1], t[2], t[3])
                expected = t[4]
                assert (
                    result == expected
                ), f"\033[93m» {result} <> {expected}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
