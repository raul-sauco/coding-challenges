# 867. Transpose Matrix
# 🟢 Easy
#
# https://leetcode.com/problems/transpose-matrix/
#
# Tags: Array - Matrix - Simulation


import timeit
from typing import List

# 10e5 calls:
# » TransposeEnumerate  0.02779   seconds
# » TransposeWithRange  0.02162   seconds
# » ListComprehension   0.02229   seconds
# » TransposeWithZip    0.00919   seconds

# Iterate over all the matrix cells assigning their value to the
# transposed cell in a result matrix.
#
# Time complexity: O(m*n) - We visit each element of the matrix once.
# Space complexity: O(1) - Constant space if we don't consider the input
# or output matrices.
#
# Runtime: 141 ms, faster than 19.88%
# Memory Usage: 14.7 MB, less than 56.41%
class TransposeEnumerate:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # The result will have n rows and m columns.
        result = [[None for _ in range(m)] for _ in range(n)]
        # Iterate over all matrix positions.
        for x, row in enumerate(matrix):
            for y, elem in enumerate(row):
                # Swap the coordinates to insert the element.
                result[y][x] = elem
        return result


# Similar to the previous solution but avoid using enumerate and instead
# use row and column index to access and assign the elements.
# Iterate over all the matrix cells assigning their value to the
# transposed cell in a result matrix.
#
# Time complexity: O(m*n) - We visit each element of the matrix once.
# Space complexity: O(1) - Constant space if we don't consider the input
# or output matrices.
#
# Runtime: 73 ms, faster than 96.52%
# Memory Usage: 14.8 MB, less than 56.41%
class TransposeWithRange:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        num_rows, num_cols = len(matrix), len(matrix[0])
        # Do not overwrite the input matrix.
        result = [[None] * num_rows for _ in range(num_cols)]
        # Iterate over all matrix positions.
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                # Swap the coordinates to insert the element.
                result[col_idx][row_idx] = matrix[row_idx][col_idx]
        return result


# Similar to the previous solution but nesting the iterative logic
# inside list comprehension.
#
# Time complexity: O(m*n) - We visit each element of the matrix once.
# Space complexity: O(1) - Constant space if we don't consider the input
# or output matrices.
#
# Runtime: 83 ms, faster than 84.48%
# Memory Usage: 14.8 MB, less than 56.41%
class ListComprehension:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [
            [matrix[y][x] for y in range(len(matrix))]
            for x in range(len(matrix[0]))
        ]


# If we unpack the matrix and use zip, we have logic similar to the
# previous solutions but get the advantage of the built-in functions
# being C code.
#
# Time complexity: O(m*n) - We visit each element of the matrix once.
# Space complexity: O(1) - Constant space if we don't consider the input
# or output matrices.
#
# Runtime: 70 ms, faster than 98.49%
# Memory Usage: 14.7 MB, less than 93.57%
class TransposeWithZip:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # we need to explicitly cast as zip returns tuples
        return list(map(list, zip(*matrix)))


def test():
    executors = [
        TransposeEnumerate,
        TransposeWithRange,
        ListComprehension,
        TransposeWithZip,
    ]
    tests = [
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        ],
        [
            [[1, 2, 3], [4, 5, 6]],
            [[1, 4], [2, 5], [3, 6]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.transpose(t[0])
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
