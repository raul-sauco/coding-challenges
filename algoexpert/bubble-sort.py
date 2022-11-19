# Bubble Sort
# 🟢 Easy
#
# https://www.algoexpert.io/questions/bubble-sort
#
# Tags: Sorting

import timeit


# Iterate over the array elements swapping adjacent elements that are
# not in sorted order. Keep a flag that detects whether we have done
# any swaps, keep iterating over the entire array as long as we swap any
# elements in the previous loop.
#
# Time complexity: O(n^2) - We may end up iterating n times over the
# entire array. Best time O(n).
# Space complexity: O(1)
class Solution:
    def bubbleSort(self, array):
        done = False
        while not done:
            done = True
            for i in range(1, len(array)):
                if array[i] < array[i - 1]:
                    array[i], array[i - 1] = array[i - 1], array[i]
                    done = False
        return array


def test():
    executors = [Solution]
    tests = [
        [[8, 5, 2, 9, 5, 6, 3], [2, 3, 5, 5, 6, 8, 9]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.bubbleSort(t[0])
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
