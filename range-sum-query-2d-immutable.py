# https://leetcode.com/problems/range-sum-query-2d-immutable/


from typing import List

from helpers import BColors


class NumMatrix:
    # The naive approach would be to assign the matrix and calculate the result
    # on each call to the sumRegion. O1 space but On2 time. This fails on LeetCode.
    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     sum = 0
    #     for row in range(row1, row2+1):
    #         for col in range(col1, col2+1):
    #             sum += self.matrix[row][col]
    #     return sum

    def __init__(self, matrix: List[List[int]]):
        # Exit if no matrix passed in as input
        if matrix == None or not matrix or matrix[0] == None or not matrix[0]:
            return
        self.sums = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row_idx, row in enumerate(matrix):
            row_sum = 0
            for col_idx, col in enumerate(row):
                row_sum += col
                self.sums[row_idx][col_idx] = row_sum if row_idx == 0 else row_sum + \
                    self.sums[row_idx-1][col_idx]
        # print(self.sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Start with the total at the bottom-right edge of the selected area
        result = self.sums[row2][col2]
        # print(f'total at end point is {result}')
        # If the start row is not the first one, subtract the sum at (row1-1,col2)
        if row1 > 0:
            result -= self.sums[row1-1][col2]
            # print(f'subtracting {self.sums[row1-1][col2]}')
        # If the start col is not the first one, subtract the sum at (row2, col1-1)
        if col1 > 0:
            result -= self.sums[row2][col1-1]
            # print(f'subtracting {self.sums[row2][col1-1]}')
        # If both the start column and the start row are not the first one, we
        # have subtracted that area twice, we have to re-add its value
        if row1 > 0 and col1 > 0:
            result += self.sums[row1-1][col1-1]
            # print(f'adding {self.sums[row1-1][col1-1]}')
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
input = [
    [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ],
    [2, 1, 4, 3],
    [1, 1, 2, 2],
    [1, 2, 2, 4],
]
numMatrix = NumMatrix(input[0])
result_1 = numMatrix.sumRegion(*input[1])
assert result_1 == 8, f'{result_1} is not 8'
assert numMatrix.sumRegion(
    *input[2]) == 11, f'{numMatrix.sumRegion(*input[2])} is not 11'
assert numMatrix.sumRegion(
    *input[3]) == 12, f'{numMatrix.sumRegion(*input[3])} is not 12'

print(
    f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')
