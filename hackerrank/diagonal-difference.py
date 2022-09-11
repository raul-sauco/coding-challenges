# Diagonal Difference
# 🟢 Easy
#
# https://www.hackerrank.com/challenges/diagonal-difference
#
# Tags: Array - Matrix

import timeit

# Iterate over the matrix rows computing the sum of the main and reverse
# diagonals at the same time.
#
# Time complexity: O(m) - Where m is the number of rows in the matrix.
# Space complexity: O(1) - Only constant space.
class Solution:
    def diagonalDifference(self, arr):
        a = b = 0
        for idx in range(len(arr)):
            # For each row, add to the main diagonal.
            a += arr[idx][idx]
            # And to the reverse diagonal.
            b += arr[idx][-idx - 1]
        return abs(a - b)


def test():
    executors = [Solution]
    tests = [
        [[[1, 2, 3], [4, 5, 6], [9, 8, 9]], 2],
        [[[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.diagonalDifference(t[0])
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
