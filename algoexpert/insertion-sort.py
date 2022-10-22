# Insertion Sort
# 🟢 Easy
#
# https://www.algoexpert.io/questions/insertion-sort
#
# Tags: Sorting

import timeit
from typing import List


# The problem asks us to implement this naive sorting algorithm.
#
# Time complexity: O(n^2) - Nested loops that iterate over n elements.
# Space complexity; O(1) - Only extra constant space.
class Naive:
    def insertionSort(self, array: List[int]) -> List[int]:
        # Start sorting from index i to the end.
        for i in range(1, len(array)):
            # Check value pairs starting at the last on the sorted
            # section and moving back to the first two.
            for j in range(i, 0, -1):
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
        return array


def test():
    executors = [
        Naive,
    ]
    tests = [
        [[1], [1]],
        [[1, 2], [1, 2]],
        [[8, 5, 2, 9, 5, 6, 3], [2, 3, 5, 5, 6, 8, 9]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.insertionSort(t[0])
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
