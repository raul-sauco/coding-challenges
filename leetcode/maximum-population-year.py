# 1854. Maximum Population Year
# 🟢 Easy
#
# https://leetcode.com/problems/maximum-population-year/
#
# Tags: Array - Counting

import timeit
from heapq import heappop, heappush
from typing import List


# Use line-sweep, sort the logs by birth year then iterate over them
# pushing the death year into a heap. Pop all deaths up to the current
# year, the population is the number of values in the heap.
#
# Time complexity: O(n*log(n)) - Both sorting and pushing and popping
# from the heap.
# Space complexity: O(n) - The heap takes extra n memory.
#
# Runtime 38 ms Beats 95.38%
# Memory 16.16 MB Beats 93.63%
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        res = (0, 0)
        logs.sort()
        heap = []
        for birth, death in logs:
            while heap and heap[0] <= birth:
                heappop(heap)
            heappush(heap, death)
            if len(heap) > res[0]:
                res = (len(heap), birth)

        return res[1]


def test():
    executors = [Solution]
    tests = [
        [[[1993, 1999], [2000, 2010]], 1993],
        [[[1950, 1961], [1960, 1971], [1970, 1981]], 1960],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maximumPopulation(t[0])
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
