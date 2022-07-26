# 1706. Where Will the Ball Fall
# 🟠 Medium
#
# https://leetcode.com/problems/where-will-the-ball-fall/
#
# Tags: Array - Dynamic Programming - Depth-First Search - Matrix - Simulation

import timeit
from typing import List


# Simulate the balls falling through the grid keeping an array positions, dp, of size n that records where the
# i-th ball is on the m-th move. If a ball gets stuck, update its position to -1 and ignore it on further moves.
#
# Time complexity: O(m*n) - We calculate each value of position (n) for each move of the balls (m).
# Space complexity: O(n) - We store a list of size n in memory.
#
# Runtime: 326 ms, faster than 49.46% of Python3 online submissions for Where Will the Ball Fall.
# Memory Usage: 14.3 MB, less than 84.62% of Python3 online submissions for Where Will the Ball Fall.
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row_length = len(grid[0])
        # Initialize the positions to each row.
        positions = [n for n in range(row_length)]

        # Iterate over each row of the grid calculating where the ball will move to.
        for row in grid:
            for idx, position in enumerate(positions):

                # Only compute for balls that are not blocked already
                if position != -1:

                    # Check the next move of the ball based on its current position and the value of the grid on
                    # that position, 1 means the ball will fall right, -1 left.
                    # move = row[position] => move == 1: right, move == -1: left
                    if row[position] == 1:
                        # The ball wants to move right.
                        # Check if we are on the last column or the column to the right has a -1.
                        if position < len(grid[0]) - 1 and row[position + 1] == 1:
                            # Nothing is stopping it from moving right.
                            positions[idx] += 1
                        else:
                            positions[idx] = -1
                    else:
                        # The ball wants to move left.
                        # Check if we are on the first column or the column to the left has a -1.
                        if position > 0 and row[position - 1] == -1:
                            # Nothing is stopping it from moving left.
                            positions[idx] -= 1
                        else:
                            positions[idx] = -1

        return positions


def test():
    executors = [Solution]
    tests = [
        [
            [
                [1, 1, 1, -1, -1],
                [1, 1, 1, -1, -1],
                [-1, -1, -1, 1, 1],
                [1, 1, 1, 1, -1],
                [-1, -1, -1, -1, -1],
            ],
            [1, -1, -1, -1, -1],
        ],
        [
            [[-1]],
            [-1],
        ],
        [
            [
                [1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1],
                [1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1],
            ],
            [0, 1, 2, 3, 4, -1],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findBall(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()

# drawTree(deserializeStringArrayToBinaryTree("[1,2]"))
