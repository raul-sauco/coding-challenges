# Minimum Passes Of Matrix
# 🟠 Medium
#
# https://www.algoexpert.io/questions/minimum-passes-of-matrix
#
# Tags: Graph - Breadth-First Search

import timeit
from collections import deque


# Travel the matrix finding cells with negative values, every time one
# is found, perform a breadth-first search from that cell to compute if
# it is possible to reach a positive cell from it and, if yes, how many
# steps it would take. If any of the breadth first searches returns -1,
# we can immediately return -1, otherwise we return the maximum of
# all the step counts.
#
# Time complexity: O(m*n) - Where m and n are the number of rows and
# columns in the matrix.
# Space complexity: O(m*n) - The breadth first search queue could end
# up holding all cells in the matrix.
class Solution:
    def minimumPassesOfMatrix(self, matrix):
        res = 0

        def bfs(row, col) -> int:
            queue = deque([(row, col)])
            steps = 0
            while queue:
                # Process an entire level.
                steps += 1
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    neighbors = (
                        (x + 1, y),
                        (x - 1, y),
                        (x, y + 1),
                        (x, y - 1),
                    )
                    for i, j in neighbors:
                        if (
                            0 <= i < len(matrix)
                            and 0 <= j < len(matrix[0])
                            and matrix[i][j] != 0
                        ):
                            if matrix[i][j] > 0:
                                return steps
                            # Append negative numbers.
                            queue.append((i, j))
            # If the breadth first search does not find a solution, we
            # cannot convert this negative.
            return -1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] < 0:
                    steps = bfs(row, col)
                    if steps == -1:
                        return -1
                    if steps > res:
                        res = steps
        return res


def test():
    executors = [Solution]
    tests = [
        [[[0, -1, -3, 2, 0], [1, -2, -5, -1, -3], [3, 0, 0, -4, -1]], 3],
        [
            [
                [1, 0, 0, -2, -3],
                [-4, -5, -6, -2, -1],
                [0, 0, 0, 0, -1],
                [-1, 0, 3, 0, 3],
            ],
            -1,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimumPassesOfMatrix(t[0])
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
