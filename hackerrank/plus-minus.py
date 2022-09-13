# Plus Minus
# 🟢 Easy
#
# https://www.hackerrank.com/challenges/plus-minus/problem
#
# Tags: Array

import timeit


# Iterate over the array and return the fraction of values that are
# positive, negative and zero. Format to six decimal places.
#
# Time complexity: O(n)
# Space complexity; O(1)
class Solution:
    def plusMinus(self, arr):
        p = m = z = 0
        for num in arr:
            if num < 0:
                m += 1
            elif num == 0:
                z += 1
            else:
                p += 1
        return [round(x / len(arr), 6) for x in [p, m, z]]


def test():
    executors = [Solution]
    tests = [
        [[-4, 3, -9, 0, 4, 1], [0.500000, 0.333333, 0.166667]],
        [[1, 2, 3, -1, -2, -3, 0, 0], [0.375000, 0.375000, 0.250000]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.plusMinus(t[0])
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
