# Binary Search
# 🟢 Easy
#
# https://www.algoexpert.io/questions/binary-search
#
# Tags: Search - Binary Search - Array

import timeit


# Implement a binary search algorithm, conceptually easy but the details
# are tricky, the best is to memorize details of one way that works and
# start with that, then modify if the particulars of the problem require
# it, to fit.
#
# Time complexity: O(log(n)) - Each iteration removes half the remaining
# search space.
# Space complexity: O(1) - Constant extra memory used.
class Solution:
    def binarySearch(self, array, target):
        l, r = 0, len(array) - 1
        while l < r:
            mid = (l + r) // 2
            if array[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if array[l] == target else -1


def test():
    executors = [Solution]
    tests = [
        [[1, 5, 23, 111], 35, -1],
        [[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33, 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.binarySearch(t[0], t[1])
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
