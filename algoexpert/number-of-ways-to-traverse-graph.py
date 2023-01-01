# Number Of Ways To Traverse Graph
# 🟠 Medium
#
# https://www.algoexpert.io/questions/number-of-ways-to-traverse-graph
#
# Tags: Graph - Dynamic Programming - Math

import timeit
from math import factorial


# We can look at this problem as computing the ways to arrange m "R" and
# n "D" in a string of length n+m, where m is the width of the graph and
# n is its height, at each position we can choose to go either right or
# down until we have consumed all the moves. When we look at the problem
# that way, it is easy to see that it can be expressed as a classic
# combination problem; the problem of traveling a graph of w: 4, h: 3,
# from its top-left corner to its bottom-right corner only moving down
# or right at each step, is the problem of choosing where to place two
# "D"s in a string of 3 "R"s and 2 "D"s, which is C(5,2) (C(5,3)).
#
# https://betterexplained.com/articles/easy-permutations-and-combinations/
#
# Time complexity: O(log(n)) - the factorial function is calculated as:
#
# > factorial(n) is written in the form 2**k * m, with m odd.  k and m
# > are computed separately, and then combined using a left shift.
#
# Python3 factorial implementation and comments:
# https://hg.python.org/cpython/file/d42f264f291e/Modules/mathmodule.c#l1218
#
# Space complexity: O(1) - But the result of factorial grows at a O(n!)
class Math:
    def numberOfWaysToTraverseGraph(self, width: int, height: int) -> int:
        a, b = width - 1, height - 1
        return factorial(a + b) // (factorial(a) * factorial(b))


# Bottom-up DP. We initialize a row of size m with all values being
# equal to 1. This represents the possible ways to reach the destination
# from these positions. Then we iterate over the remaining rows of the
# matrix updating the possible ways to reach the destination from the
# given position.
#
# For each position, the possible ways to reach the destination are the
# sum of the position above plus the position to its left.
#
# Time complexity: O(m*n) - We do one calculation for each position of
# the matrix mxn.
# Space complexity: O(n) - We store an array of size n in memory.
class DP:
    def numberOfWaysToTraverseGraph(self, width: int, height: int) -> int:
        paths = [1] * height
        for _ in range(width - 1):
            for i in range(height):
                # The first col is always 1 because we can only move
                # down from this position to reach the target.
                if i > 0:
                    # The number of ways to reach the target from here
                    # are the sum of the ways to reach the target
                    # from the position to the right and the position
                    # below (inverted on the code for clarity).
                    paths[i] += paths[i - 1]

        return paths[-1]


def test():
    executors = [
        Math,
        DP,
    ]
    tests = [
        [1, 1, 1],
        [2, 1, 1],
        [3, 2, 3],
        [2, 3, 3],
        [4, 3, 10],
        [3, 7, 28],
        [5, 9, 495],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numberOfWaysToTraverseGraph(t[0], t[1])
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
