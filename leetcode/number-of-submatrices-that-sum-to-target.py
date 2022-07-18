# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

# Tags: Array - Hash Table - Matrix - Prefix Sum

import timeit
from typing import List


# TODO Non-working solution TLE!
class Solution:

    # Create a matrix of prefix sums
    def calculatePrefixSum(self, matrix: List[int]) -> List[int]:
        sums = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        if matrix == None or not matrix or matrix[0] == None or not matrix[0]:
            return sums
        for row in range(len(matrix)):
            row_sum = 0
            for col in range(len(matrix[row])):
                row_sum += matrix[row][col]
                sums[row][col] = row_sum if row == 0 else row_sum + sums[row - 1][col]
        return sums

    # Function to calculate the sum of a region given its four corner positions
    def sumRegion(self, top: int, left: int, bottom: int, right: int) -> int:
        # Start with the total at the bottom-right edge of the selected area
        result = self.sums[bottom][right]
        # If the start row is not the first one, subtract the sum at (row1-1,col2)
        if top > 0:
            result -= self.sums[top - 1][right]
        # If the start col is not the first one, subtract the sum at (row2, col1-1)
        if left > 0:
            result -= self.sums[bottom][left - 1]
        # If both the start column and the start row are not the first one, we
        # have subtracted that area twice, we have to re-add its value
        if top > 0 and left > 0:
            result += self.sums[top - 1][left - 1]
        return result

    def findResultsInRows(self, top: int, bottom: int, target: int) -> int:
        left, right, results = 0, 0, 0
        for left in range(len(self.sums[0])):
            for right in range(left, len(self.sums[0])):
                s = self.sumRegion(top, left, bottom, right)
                if s == target:
                    results += 1

        return results

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        self.sums = self.calculatePrefixSum(matrix)
        result = 0
        # Iterate over every possible combination of 2 rows
        for top in range(len(matrix)):
            for bottom in range(top, len(matrix)):
                result += self.findResultsInRows(top, bottom, target)

        return result


def test():
    executors = [Solution]
    tests = [
        [[[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0, 4],
        [[[1, -1], [-1, 1]], 0, 5],
        [[[904]], 0, 0],
        [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], 1000, 0],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.numSubmatrixSumTarget(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()


# Bonus / TODO optimize the code only looping through submatrices that could generate the target sum

# Calculate the number of matches in the submatrix formed by the rows between top and bottom
# This is a neat idea to decide when we can skip calculations looking at the difference between target and current sum
# but it needs to get fixed to work when the submatrix has negative values, store sum_neg and sum_pos
# def findResultsInRows(self, top: int, bottom: int, target: int) -> int:
#     left, right, results = 0, 0, 0
#     while left < len(self.sums[top]):
#         s = self.sumRegion(top, left, bottom, right)

#         if s < target or s == target:
#             # Sum is too small or equal to the target, move right if possible
#             if s == target:
#                 results += 1
#             # Right pointer is at the end and the sum is already too small
#             if right == len(self.sums[top]) - 1:
#                 break
#             right += 1
#         else:
#             # sum is currently bigger than target
#             left += 1
#             right = max(right, left)  # Prevent the left pointer overtaking the right one

#     return results
