# 1137. N-th Tribonacci Number
# 🟢 Easy
#
# https://leetcode.com/problems/n-th-tribonacci-number/
#
# Tags: Math - Dynamic Programming - Memoization

import timeit


# Use three variables initialized to the three initial tribonacci values,
# iterate over 3..n values computing the sum of the current three
# variables, discarding the lowest one and adding the sum as the third
# value. The result will be that sum at the last iteration.
#
# Time complexity: O(n) - The loop executes n-2 times.
# Space complexity: O(1) - Constant space used.
#
# Runtime 31 ms Beats 76.51%
# Memory 13.8 MB Beats 54.1%
class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        a, b, c = 0, 1, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c


def test():
    executors = [Solution]
    tests = [
        [0, 0],
        [1, 1],
        [2, 1],
        [3, 2],
        [25, 1389537],
        [37, 2082876103],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.tribonacci(t[0])
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
