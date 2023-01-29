# Quickselect
# 🔴 Hard
#
# https://www.algoexpert.io/questions/quickselect
#
# Tags: Searching

import timeit
from random import randint
from typing import List


# Implement the quickselect algorithm.
#
# Time complexity: Best/Average: O(n), Worst O(n^2)
# Space complexity: O(1) - Pointers and a loop, only 1 call to partition
# is on the stack at one given time.
class Solution:
    def quickselect(self, array: List[int], k: int) -> int:
        def partition(l, r, p) -> int:
            # Move the pivot to the right end.
            array[p], array[r] = array[r], array[p]
            st = l
            for i in range(l, r):
                if array[i] < array[r]:
                    array[st], array[i] = array[i], array[st]
                    st += 1
            array[st], array[r] = array[r], array[st]
            return st

        l, r = 0, len(array) - 1
        while l < r:
            # Choose a random pivot between the boundaries inclusive.
            pivot = randint(l, r)
            pivot = partition(l, r, pivot)
            if k - 1 == pivot:
                return array[k - 1]
            if k - 1 < pivot:
                r = pivot - 1
            else:
                l = pivot
        return array[l]


def test():
    executors = [Solution]
    tests = [
        [[4], 1, 4],
        [[43, 24, 37], 2, 37],
        [[8, 5, 2, 9, 7, 6, 3], 3, 5],
        [[8, 3, 2, 5, 1, 7, 4, 6], 4, 4],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.quickselect(t[0], t[1])
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
