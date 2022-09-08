# 6. Zigzag Conversion
# 🟠 Medium
#
# https://leetcode.com/problems/zigzag-conversion/
#
# Tags: String

import timeit
from itertools import zip_longest


# Follow the steps of the problem exactly as they are given, easy to
# visualize solution but not very performant.
#
# Compute the direction we are going, down or up, and calculate the
# position of the character in the matrix based on the constraints given.
# When going down, character will be placed below the last one, when
# going up, character will be placed on the position diagonally right
# and up from the last one.
#
# Time complexity: O(n) - we iterate over the number of elements in the
# matrix 3 times, to create the matrix, to put each character in its
# position in the matrix, and to create the result string.
# Space complexity: O(n*m) - the matrix grows proportionally to both the
# size of the string and the number of rows.
#
# The space complexity could be optimized calculating the number of
# columns needed after half of the elements go in the same column and
# the other half in consecutive columns.
#
# Runtime: 336 ms, faster than 10.15%
# Memory Usage: 21.2 MB, less than 5.04%
class Matrix:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        matrix = [[""] * len(s) for _ in range(numRows)]
        go_up = False
        col, row = 0, 0
        for c in s:
            matrix[row][col] = c
            if go_up:
                # While moving up, increase the column and row count
                col += 1
                row -= 1
                if row == 0:
                    go_up = False
            else:
                # When moving down, do not increase the column count,
                # just check if we reached the bottom
                row += 1
                if row == numRows - 1:
                    go_up = True

        # Merge the results one row at a time.
        return "".join(["".join(row) for row in matrix])

        # List comprehension is equivalent to:
        # result = ""
        # for row in matrix:
        #     result += "".join(row)
        # return result


# This solution improves on the above one realizing that we don't really
# use the col position of the elements, we only care to know which row,
# and after which character, they are on. Instead of using a matrix, we
# can save time and space by using an array of strings as the matrix and
# appending each character to the corresponding row-string.
#
# Time complexity: O(n) - We go over each character in the string once.
# Space complexity: O(n) - We store all characters in the string in the
# rows array
#
# Runtime: 117 ms, faster than 30.80%
# Memory Usage: 13.9 MB, less than 96.00%
class Rows:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        # Iterate over the characters of s appending them to the
        # corresponding row.
        rows = ["" for _ in range(numRows)]
        i, down = 0, True
        for c in s:
            rows[i] += c
            if down:
                i += 1
                if i == numRows - 1:
                    down = False
            else:
                i -= 1
                if i == 0:
                    down = True

        return "".join(rows)


# Using native functions, in this case zip_longest is probably not what
# an interviewer would be looking for, or even expect, but it is nice to
# be aware that it is a possibility, and that it tends to be more
# performant.
#
# Time complexity: O(n)
# Space complexity: O(n)
#
# Runtime: 70 ms, faster than 81.44%
# Memory Usage: 13.8 MB, less than 96.00%
class Zip:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        n = numRows - 1
        step = n * 2
        res = s[::step]
        for i in range(1, n):
            for v, w in zip_longest(
                s[i::step], s[step - i :: step], fillvalue=""
            ):
                res += v + w
        return res + s[n::step]


def test():
    executors = [Matrix, Rows, Zip]
    tests = [
        ["AB", 1, "AB"],
        ["ABC", 1, "ABC"],
        ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
        ["PAYPALISHIRING", 4, "PINALSIGYAHRPI"],
        ["A", 1, "A"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.convert(t[0], t[1])
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
