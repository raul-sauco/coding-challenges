# Product Sum
# 🟢 Easy
#
# https://www.algoexpert.io/questions/product-sum
#
# Tags: Array - Recursion

import timeit


# Process integers and recursively call the function to process lists,
# then multiply the result by the depth of the nested array, 1 for the
# top level array.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(n) - The call stack will grow to the depth of the
# most deeply nested list, which could be the same as the input.
class Solution:
    def productSum(self, array, depth=1):
        res = 0
        for elem in array:
            if isinstance(elem, list):
                res += self.productSum(elem, depth + 1)
            else:
                res += elem
        return res * depth


def test():
    executors = [Solution]
    tests = [
        [[], 0],
        [[0], 0],
        [[7], 7],
        [[[[[[5]]]]], 600],
        [[[1, 2], 3, [4, 5]], 27],
        [[5, 2, [7, -1], 3, [6, [-13, 8], 4]], 12],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.productSum(t[0])
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
