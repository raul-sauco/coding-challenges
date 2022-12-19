# Find Three Largest Numbers
# 🟢 Easy
#
# https://www.algoexpert.io/questions/find-three-largest-numbers
#
# Tags: Array - Recursive

import timeit


# Store the three largest numbers in an array, initialize them with
# -inf, when we see a value that is greater than the minimum in the
# result, update it, then shift the minimum with its next greater
# neighbor until the new value is in its corresponding position in the
# sorted result.
#
# Time complexity; O(n) - We visit each value once and perform O(1)
# operations for each.
# Space complexity: O(1) - Constant extra memory.
class Solution:
    def findThreeLargestNumbers(self, array):
        res = [float("-inf")] * 3
        for num in array:
            if num > res[0]:
                res[0] = num
                for i in range(2):
                    if res[i] > res[i + 1]:
                        res[i], res[i + 1] = res[i + 1], res[i]
        return res


def test():
    executors = [Solution]
    tests = [
        [[55, 7, 8], [7, 8, 55]],
        [[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7], [18, 141, 541]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findThreeLargestNumbers(t[0])
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
