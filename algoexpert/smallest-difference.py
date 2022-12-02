# Smallest Difference
# 🟠 Medium
#
# https://www.algoexpert.io/questions/smallest-difference
#
# Tags: Array - Sorting

import timeit


# Start by sorting the arrays then comparing pairs of integers along the
# sorted order, we will move forward the pointer to the smaller element
# hopping to make the difference smaller.
#
# Time complexity: O(m*log(m) + n*log(n)) - Where m and n are the sizes
# of the input arrays.
# Space complexity: O(m+n): - Sorting in python takes extra memory.
class Solution:
    def smallestDifference(self, arrayOne, arrayTwo):
        arrayOne.sort()
        arrayTwo.sort()
        res, d = [None, None], float("inf")
        i = j = 0
        while i < len(arrayOne) and j < len(arrayTwo):
            current = abs(arrayOne[i] - arrayTwo[j])
            if current < d:
                res = [arrayOne[i], arrayTwo[j]]
                d = current
            if arrayOne[i] <= arrayTwo[j]:
                i += 1
            else:
                j += 1
        return res


def test():
    executors = [Solution]
    tests = [
        [[-1, 5, 10, 20, 3], [26, 134, 135, 15, 17], [20, 17]],
        [[-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17], [28, 26]],
        [[10, 0, 20, 25, 2000], [1005, 1006, 1014, 1032, 1031], [2000, 1032]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.smallestDifference(t[0], t[1])
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
