# https://leetcode.com/problems/unique-paths/

# Tags: Math - Dynamic Programming - Combinatorics

import timeit
from functools import reduce
from math import factorial

# 1e3 calls:
# » DP                  0.74211   seconds
# » Math                0.00483   seconds
# » Reduce              0.015     seconds

# Bottom-up DP. We initialize a row of size m with all values being equal to 1. This represents the possible ways
# reach the destination from these positions. Then we iterate over the remaining rows of the matrix updating the
# possible ways to reach the destination from the given position.
#
# For each position, the possible ways to reach the destination are the sum of the position above plus the position
# to its left.
#
# Time complexity: O(m*n) - we do one calculation for each position of the matrix mxn.
# Space complexity: O(n) - we store an array of size n in memory.
#
# Runtime: 42 ms, faster than 69.04% of Python3 online submissions for Unique Paths.
# Memory Usage: 14 MB, less than 32.87% of Python3 online submissions for Unique Paths.
class DP:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [1] * n
        for _ in range(m - 1):
            for i in range(n):
                # The first col is always 1 because we can only move down from this position to reach the target.
                if i > 0:
                    # The number of ways to reach the target from here are the sum of the ways to reach the target
                    # from the position to the right and the position below (inverted on the code for clarity).
                    paths[i] += paths[i - 1]

        return paths[-1]


# What the problem asks for is simply the number of ways we can combine a certain amount of 2 values,
# for example, if we call the down move 0 and the right move 1, the first example can be re-written to be:
# How many different ways can we combine 3 0s and 7 1s?
# That is a combination that can be calculated as C(10, 3)
#
# https://betterexplained.com/articles/easy-permutations-and-combinations/
#
# Time complexity: O(log(n)) - the factorial function is calculated as:
#
# > factorial(n) is written in the form 2**k * m, with m odd.  k and m are
# > computed separately, and then combined using a left shift.
#
# Python3 factorial implementation and comments:
# https://hg.python.org/cpython/file/d42f264f291e/Modules/mathmodule.c#l1218
#
# Space complexity: O(1) - But the result of factorial grows at a O(n!) rate, even limited by a size of n, m <= 100,
# the factorial of 200 is > 1e350 which is probably more space than needed for the 100 slot list used on the DP.
#
# The results running this code in LeetCode are a bit surprising, for me at least, I expected the code to run fast
# but use a lot of memory, but the result is the oppossite.
#
# Runtime: 71 ms, faster than 7.38% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.7 MB, less than 97.78% of Python3 online submissions for Unique Paths.
class Math:
    def uniquePaths(self, m: int, n: int) -> int:
        down = m - 1
        right = n - 1
        return factorial(down + right) // (factorial(down) * factorial(right))


# We can use functools.reduce to have python do the calculations in C, this method has the same O complexity but
# is more efficient.
#
# Time complexity: O(m*n) - we do one calculation for each position of the matrix mxn.
# Space complexity: O(m*n) - the memory used by reduce and the lambda will grow linearly with the size of the matrix.
#
# Runtime: 41 ms, faster than 71.79% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 73.29% of Python3 online submissions for Unique Paths.
class Reduce:
    def uniquePaths(self, m: int, n: int) -> int:
        if 1 in [n, m]:
            return 1
        return reduce(lambda x, y: x * y, range(n, n + m - 1)) // reduce(lambda x, y: x * y, range(1, m))


def test():
    executors = [DP, Math, Reduce]
    tests = [
        [1, 1, 1],
        [
            100,
            100,
            22750883079422934966181954039568885395604168260154104734000,
        ],
        [3, 7, 28],
        [3, 2, 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.uniquePaths(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
