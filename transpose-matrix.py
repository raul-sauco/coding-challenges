# https://leetcode.com/problems/transpose-matrix/

from typing import List

from helpers import BColors


class Solution:
    # 4.3 seconds
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        # The result will have n rows and m columns
        result = [[None for _ in range(m)] for _ in range(n)]
        # Initialize the X coordinate once
        # x = 0
        for x, row in enumerate(matrix):
            # Initialize the Y coordinate for each row
            # y = 0
            for y, elem in enumerate(row):
                # Reverse the coordinates of the element
                # Swap the coordinates to insert the element
                result[y][x] = elem
                y += 1
            x += 1

        return result

    # 3.1 seconds
    def transposeWithRange(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]

        return ans

    # 1.324 seconds
    def transposeWithZip(self, matrix: List[List[int]]) -> List[List[int]]:
        # we need to explicitly cast as zip returns tuples
        return list(map(list, zip(*matrix)))

    # 2.9 seconds
    def transposeWithListComprehension(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[y][x] for y in range(len(matrix))] for x in range(len(matrix[0]))]


def test():
    sol = Solution()
    assert sol.transposeWithZip([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert sol.transposeWithZip([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4], [2, 5], [3, 6]]
    # print(f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')


for _ in range(int(1e+6)):
    test()
