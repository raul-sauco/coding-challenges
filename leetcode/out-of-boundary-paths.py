# https://leetcode.com/problems/out-of-boundary-paths/

# Tags: Dynamic Programming

import timeit

# 1e2 calls
# » Memoization         0.14043   seconds
# » Tabulation          0.6757    seconds

# For each position, we have four possible moves, we can explore them all using a dictionary to make sure we do not
# calculate the number of possible moves from a given state more than once.
# Visiting the same position multiple times is a valid move, therefore, our state needs to record the grid position
# and the remaining number of moves.
#
# Time complexity: O(m*n*maxMoves) We can go through each state a maximum of 1 time
# Space complexity: O(m*n*maxMoves) The size of the dictionary
#
# Runtime: 172 ms, faster than 68.29% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 18.2 MB, less than 47.57% of Python3 online submissions for Out of Boundary Paths.
class Memoization:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}

        # Calculate the number of moves possible with the remaining moves and current position
        def dfs(moves: int, row: int, col: int) -> int:
            key = (moves, row, col)
            if key in memo:
                return memo[key]

            # Base case, we are out of the grid, add this path to the result set
            if row == -1 or row == m or col == -1 or col == n:
                return 1

            # Base case, we don't have any moves left and we are still inside the grid
            if moves == 0:
                return 0

            # We are still in the grid and have moves left
            result = (
                dfs(moves - 1, row - 1, col)
                + dfs(moves - 1, row + 1, col)
                + dfs(moves - 1, row, col - 1)
                + dfs(moves - 1, row, col + 1)
            )

            memo[key] = result
            return result

            # TODO Check if we still can reach the boundary from this position with the remaining number of moves

        # Initial call
        return dfs(maxMove, startRow, startColumn) % 1000000007


# We can store the number of different ways we can reach a position using 2 2D matrixes. On each move, we recalculate
# the ways we can reach the given position, adding that value to the current ways to exit the matrix when the ball
# leaves the boundaries.
#
# Time complexity: O(m*n*maxMoves) We can go through each state a maximum of 1 time
# Space complexity: O(m*n) The size of the matrixes where we store possible paths information.
#
# Runtime: 762 ms, faster than 5.11% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 14.1 MB, less than 88.49% of Python3 online submissions for Out of Boundary Paths.
class Tabulation:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        # Memo
        current = [[0] * n for _ in range(m)]

        # Base case, we can reach the starting position in 0 moves
        current[startRow][startColumn] = 1

        # Number of ways we can exit the matrix
        paths = 0

        for _ in range(maxMove):

            # Current step memo to avoid counting m and n steps twice
            nxt = [[0] * n for _ in range(m)]

            for r, row in enumerate(current):  # Iterate rows
                for c, previous_count in enumerate(row):  # Iterate columns

                    # For each position, check its 4 adjacent positions
                    for new_row, new_col in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):

                        # If the new position is inside the matrix, increase the ways you can reach it by 1
                        if 0 <= new_row < m and 0 <= new_col < n:
                            nxt[new_row][new_col] += previous_count
                            nxt[new_row][new_col] %= MOD

                        # If the move takes the ball outside the matrix, increase the current ways to reach the
                        # boundary with the different ways that we can reach the position
                        else:
                            # if it is out of boundary
                            paths += previous_count
                            paths %= MOD

            # Update our tabulation data
            current = nxt

        return paths


def test():
    executors = [Memoization, Tabulation]
    tests = [
        # m n maxMove startRow startCol output
        [1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 4],
        [2, 2, 2, 0, 0, 6],
        [1, 3, 3, 0, 1, 12],
        [8, 50, 23, 5, 26, 914783380],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e2"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.findPaths(t[0], t[1], t[2], t[3], t[4])
                exp = t[5]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
