# Nth-Fibonacci
# 🟢 Easy
#
# https://www.algoexpert.io/questions/nth-fibonacci
#
# Tags: Dynamic Programming

import timeit


# Compute the Fibonacci number for n-1.
#
# Time complexity: O(n) - Where n is the value of the input, we do one
# O(1) operation for each value between 0 to n.
# Space complexity: O(1) - Constant memory.
class Solution:
    def getNthFib(self, n):
        if n == 1:
            return 0
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b


def test():
    executors = [Solution]
    tests = [
        [1, 0],
        [2, 1],
        [3, 1],
        [4, 2],
        [9, 21],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.getNthFib(t[0])
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
