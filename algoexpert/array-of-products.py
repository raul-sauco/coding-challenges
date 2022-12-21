# Array Of Products
# 🟢 Easy
#
# https://www.algoexpert.io/questions/array-of-products
#
# Tags: Array - Recursion

import timeit


# Compute the products of the front of the array and the back of the
# array up to all indexes, the result of the product of array except for
# self is the product of the prefixes array up to i-1 times the
# postfixes array from i+1 to the end of the array.
#
# Time complexity: O(n) - We iterate over the array three times, all of
# them in O(n).
# Space complexity: O(n) - The pre and post arrays are the same size as
# the input.
class Solution:
    def arrayOfProducts(self, array):
        # Array of products up to an index i and from i to the end.
        pre, post = [None] * len(array), [None] * len(array)
        pre[0], post[-1] = array[0], array[-1]
        for i in range(1, len(array)):
            pre[i] = pre[i - 1] * array[i]
        for i in range(len(array) - 2, -1, -1):
            post[i] = post[i + 1] * array[i]
        # Return the product of the array up to i-1 * the array from
        # i+1 to the end.
        return [
            (pre[i - 1] if i > 0 else 1)
            * (post[i + 1] if i < len(array) - 1 else 1)
            for i in range(len(array))
        ]


def test():
    executors = [Solution]
    tests = [
        [[-1, -1, -1], [1, 1, 1]],
        [[0, 0, 0, 0], [0, 0, 0, 0]],
        [[5, 1, 4, 2], [8, 40, 10, 20]],
        [[1, 8, 6, 2, 4], [384, 48, 64, 192, 96]],
        [[-5, 2, -4, 14, -6], [672, -1680, 840, -240, 560]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.arrayOfProducts(t[0])
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
