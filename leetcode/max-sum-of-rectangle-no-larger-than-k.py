# 363. Max Sum of Rectangle No Larger Than K
# 🔴 Hard
#
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
#
# Tags: Array - Binary Search - Matrix - Prefix Sum - Ordered Set

import bisect
import timeit
from typing import List

from sortedcontainers import SortedList


# Calculate the prefix sums of all the matrix positions, and use them to
# calculate the range sums for each possible combination of top-left and
# bottom-right.
#
# Time complexity: O((m*n)^3) - We loop through all col/row positions
# and, for each, calculate the range sum using each possible top-right
# corner value.
# Space complexity: O(m*n) - The sum matrix has the same size as the
# input. We could even overwrite the input matrix to have a complexity
# of O(1) but it would not really improve performance.
#
# This solution would fail with Time Limit Exceeded.
class PrefixSum:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        NUM_ROWS = len(matrix)
        NUM_COLS = len(matrix[0])
        # Store the max range sum < k.
        result = float("-inf")
        # Create a matrix of prefix sums.
        sums_grid = [[None] * NUM_COLS for _ in range(NUM_ROWS)]
        # Iterate over all the grid positions calculating the prefix
        # sums O(m*n).
        for i in range(NUM_ROWS):
            # Restart the row sum for each row.
            row_sum = 0
            for j in range(NUM_COLS):
                # Add the current value to the current row sum.
                row_sum += matrix[i][j]
                # If we are on the first row, the total is the row sum.
                if i == 0:
                    sums_grid[i][j] = row_sum
                # If we are not on the first row, add the range sum of
                # the cell above.
                else:
                    sums_grid[i][j] = row_sum + sums_grid[i - 1][j]
                # We have the prefix sum at this i,j and all previous
                # values of i,j, calculate all possible range sums with
                # this position as the bottom-right corner.
                for top_row in range(i + 1):
                    for left_col in range(j + 1):
                        # Calculate the sum of the range as the prefix
                        # sum of the bottom-right corner minus the
                        # missing sections.
                        range_sum = sums_grid[i][j]
                        # If we are removing rows from the top.
                        if top_row > 0:
                            range_sum -= sums_grid[top_row - 1][j]
                        # If we are removing columns from the left.
                        if left_col > 0:
                            range_sum -= sums_grid[i][left_col - 1]
                            # If we removed both rows and columns, we
                            # removed the top-left section of the grid
                            # twice, read its sum one time.
                            if top_row > 0:
                                range_sum += sums_grid[top_row - 1][
                                    left_col - 1
                                ]
                        if result < range_sum <= k:
                            result = range_sum
        return result


# Calculate the prefix sum of all rows. Iterate over every possible
# combination of two columns and compute the sum of the values of each
# row between these two columns, then iterate over the values on each of
# the rows, which are row sums, and find the combination of start and
# end column that gives the biggest integer <= k.
#
# Time complexity: O(m^2*n*log(n)) - Iterating over each pair of columns
# m^2, for each pair, iterate over n column sums, add each element to
# the sorted sums list in log(n) and find the maxSumSubarray also log(n).
# Space complexity: O(m) - The row sums array is the only thing we keep
# in memory besides constant space variables.
#
# Using a regular list and bisect.insort()
# Runtime: 5867 ms, faster than 37.59%
# Memory Usage: 14.5 MB, less than 96.45%
#
# Using sortedcontainers.SortedList() at O(log(n)) - should be faster
# but it runs slower on the tests. Tests results are very inconsistent
# for this problem, maybe this solution is more performant but the
# server was under a higher load.
# Runtime: 7327 ms, faster than 24.12%
# Memory Usage: 15.4 MB, less than 11.35%
class RowSum:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # Define a function that takes in an array and finds the max
        # subsequence that is still less than k.
        def maxSumSubarray(row_sums):
            # Store the current best.
            res = float("-inf")
            # Store the sum of the elements that we have processed.
            current_sum = 0
            # Keep a sorted list of the sums that we find, later we can
            # use this sorted list to binary search the closest value
            # that fulfills the equation right - left >= k
            sorted_sums = SortedList([float("inf")])
            for val in row_sums:
                # SortedList.add is O(log(n)) instead of other solutions
                # that use bisect.insort at O(n) cost.
                sorted_sums.add(current_sum)
                current_sum += val
                # The leftmost insertion point of the value that
                # fulfills the equation coincides with the index of the
                # element that gives us the sum closest to k.
                i = bisect.bisect_left(sorted_sums, current_sum - k)
                temp_best = current_sum - sorted_sums[i]
                # If we find an exact match, no need to keep looking.
                if temp_best == k:
                    return temp_best
                # If the value found is better than our current best,
                # update it.
                if temp_best > res:
                    res = temp_best
            return res

        # Store the number of rows and columns to make the code more
        # readable.
        num_rows, num_cols = len(matrix), len(matrix[0])
        # Iterate over all matrix positions constructing row prefix sums.
        for row_idx in range(num_rows):
            for col_idx in range(num_cols - 1):
                matrix[row_idx][col_idx + 1] += matrix[row_idx][col_idx]
        # Initialize the result variable.
        res = float("-inf")
        # For each possible pair of columns.
        for l in range(num_cols):
            for r in range(l, num_cols):
                # For each possible pair of columns, use list
                # comprehension to compute an array of row sums.
                row_sums = [
                    matrix[i][r] - (matrix[i][l - 1] if l > 0 else 0)
                    for i in range(num_rows)
                ]
                # Use an auxiliary function to find the rectangle sum
                # closest to k given the current left and right columns.
                temp = maxSumSubarray(row_sums)
                # If the temporarily highest value closest to k is k, no
                # need to keep computing, return the value.
                if temp == k:
                    return k
                # If we have a higher value than the highest found
                # previously, update our current best.
                if temp > res:
                    # More efficient than res = max(temp, res)
                    res = temp
        return res


def test():
    executors = [
        PrefixSum,
        RowSum,
    ]
    tests = [
        [[[1, 0, 1], [0, -2, 3]], 2, 2],
        [[[2, 2, -1]], 3, 3],
        [
            [
                [-82, 10, 41, 43, -34],
                [92, -84, 81, 34, -91],
                [-6, -76, 75, 38, 22],
                [-81, -47, -70, -74, 82],
            ],
            100,
            97,
        ],
        [
            [
                [5, -4, -3, 4],
                [-3, -4, 4, 5],
                [5, 1, 5, -4],
            ],
            3,
            2,
        ],
        [
            [
                [16, 12, -97, 73, -99, -33, 74, -97, -97, 28],
                [19, -11, -73, -64, 15, -4, -45, 73, -68, -21],
                [-46, -69, -16, -94, 77, -67, 99, 22, -73, 9],
                [33, 38, -37, 15, 78, -38, 28, -88, 42, 77],
                [14, -16, -58, 25, -51, -81, 17, 40, 29, -53],
                [-27, 30, -26, -95, -20, 89, 83, 73, 56, -79],
                [39, -79, -90, -28, -73, 36, 20, 7, -30, 82],
                [-26, -1, 55, 17, 70, 6, 40, 27, -27, -54],
                [-73, 41, 31, 57, 1, 100, 93, -38, 51, -76],
                [30, 21, 77, -12, -63, -21, 19, 61, 55, -92],
            ],
            24,
            24,
        ],
        [
            [
                [84, 75, -63, 21, -25, 15, 77, 63, -18, 18],
                [87, 18, 79, 95, -8, 19, 68, 23, 49, 63],
                [-38, 30, -76, -54, -11, -50, 27, -38, -48, -83],
                [1, 42, 86, 73, 5, 41, -25, 48, 93, 87],
                [-30, 52, -6, 77, 27, -92, -6, 79, -47, -70],
                [-26, 68, 42, 52, 76, 75, 57, -19, -37, 35],
                [42, -58, 64, -37, -37, -76, 39, 11, -30, 34],
                [60, 19, -5, 68, 54, -81, 94, 71, -71, -12],
                [78, -100, 98, 32, -87, 51, 68, -31, -96, -47],
                [-47, 17, -74, 66, -18, 45, 57, 26, -71, 14],
            ],
            15,
            15,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxSumSubmatrix(t[0], t[1])
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
