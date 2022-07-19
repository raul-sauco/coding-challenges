# https://leetcode.com/problems/pascals-triangle/

# Tags: Array - Dynamic Programming

import timeit
from typing import List


# Create the result matrix and then, starting at the third row, fill the values for each row based on the values
# found on the previous row.
#
# Time complexity: O(n^2) - We visit each element twice, when we create the empty matrix and when we calculate
# its value. The number of elements has a quadratic relation to the value of the input n and a linear O(n) relation
# to the output.
# Space complexity; O(n^2) - Same as above. Quadratic relation with the value of the input and linear with the size
# of the output.
#
# Runtime: 50 ms, faster than 43.34% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.9 MB, less than 66.48% of Python3 online submissions for Pascal's Triangle.
class CreateUpdate:
    def generate(self, numRows: int) -> List[List[int]]:
        # Create the result matrix prefilled with ones. This solves edge cases when numRows < 2
        matrix = [[1] * (x + 1) for x in range(numRows)]
        # Starting at the 3rd row, fill in the values for all rows
        for row_idx in range(2, numRows):
            # Generate row sums avoiding the first and last element
            for col_idx in range(1, row_idx):
                # pos = top_left + top_right when center-aligned
                matrix[row_idx][col_idx] = matrix[row_idx - 1][col_idx - 1] + matrix[row_idx - 1][col_idx]

        return matrix


# Similar idea, and O complexity, but slower because append needs to grow the matrix, using O(n) time,
# each time that it doubles in size. Between grow operations, append is O(1).
#
# Runtime: 63 ms, faster than 12.86% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 14 MB, less than 17.88% of Python3 online submissions for Pascal's Triangle.
class Append:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        matrix = [[1], [1, 1]]
        if numRows == 2:
            return matrix

        for row_idx in range(2, numRows):
            matrix.append(
                [1]
                + [matrix[row_idx - 1][col_idx - 1] + matrix[row_idx - 1][col_idx] for col_idx in range(1, row_idx)]
                + [1]
            )

        return matrix


def test():
    executors = [CreateUpdate, Append]
    tests = [
        [
            5,
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
            ],
        ],
        [1, [[1]]],
        [2, [[1], [1, 1]]],
        [3, [[1], [1, 1], [1, 2, 1]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.generate(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
