# 931. Minimum Falling Path Sum
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-falling-path-sum/
#
# Tags: Array - Dynamic Programming - Matrix

import timeit
from typing import List


# The bottom-up dynamic programming solution stores the last row of
# minimum sums and uses it to compute the current row up to the last one
# then returns the minimum sum on the row.
#
# Time complexity: O(m*n) - The number of rows * columns, each cell will
# be visited once.
# Space complexity: O(m) - We use one row of values worth of extra
# memory.
#
# Runtime 232 ms Beats 70.91%
# Memory 14.7 MB Beats 91.12%
class BottomUpDP:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # A row of minimum sums up to the one we are computing.
        dp = matrix[0][::]
        for i in range(1, len(matrix)):
            # A new array to update the values for the current row.
            row = dp[::]
            for j in range(len(matrix[0])):
                # The minimum value to add to this cell.
                minimum = dp[j]
                if j > 0 and dp[j - 1] < minimum:
                    minimum = dp[j - 1]
                if j < len(matrix[0]) - 1 and dp[j + 1] < minimum:
                    minimum = dp[j + 1]
                row[j] = matrix[i][j] + minimum
            dp = row
        return min(dp)


# If we are allowed to mutate the input matrix, we can optimize the
# memory complexity storing intermediate results directly in the matrix,
# iterate over the rows using the previous row's results to update the
# current one.
#
# Time complexity: O(m*n) - The number of rows * columns, each cell will
# be visited once.
# Space complexity: O(1) - We use constant space, but we mutate the
# input, which may not be allowed.
#
# Runtime 236 ms Beats 70.41%
# Memory 14.9 MB Beats 40.57%
class BottomUpDPO1:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(
                    matrix[i - 1][max(0, j - 1)],
                    matrix[i - 1][j],
                    matrix[i - 1][min(n - 1, j + 1)],
                )
        return min(matrix[-1])


def test():
    executors = [
        BottomUpDP,
        BottomUpDPO1,
    ]
    tests = [
        [[[-19, 57], [-40, -5]], -59],
        [[[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minFallingPathSum(t[0])
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
