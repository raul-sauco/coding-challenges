# Merge Overlapping Intervals
# 🟠 Medium
#
# https://www.algoexpert.io/questions/merge-overlapping-intervals
#
# Tags: Array - Intervals

import timeit
from typing import List


# Sort the intervals by start and then iterate over them, before adding
# an interval to the result, we check if it overlaps with the last one
# already in the result, if it does, we update the end time of the last
# interval in the result to be the max of its own end time and the end
# time of the current interval.
#
# Time complexity: O(n*log(n)) - For the sorting, once sorted, checking
# the intervals can be done in O(n).
# Space complexity: O(n) - Sorting takes space in Python. The result set
# can also be of the same size as the input, but I would not consider it
# on the space complexity calculation.
class Solution:
    def mergeOverlappingIntervals(self, intervals: List[int]) -> List[int]:
        if not intervals:
            return intervals
        # Sort the intervals by start time.
        intervals.sort()
        res = [intervals[0]]
        # Iterate over the rest of the intervals.
        for start, end in intervals[1:]:
            # If the current interval overlaps the last one on the
            # result, compute the end point of the overlapping interval.
            if start <= res[-1][1]:
                res[-1] = [res[-1][0], max(end, res[-1][1])]
            else:
                res.append([start, end])
        return res


def test():
    executors = [Solution]
    tests = [
        [[[1, 4]], [[1, 4]]],
        [[[-5, -4], [-4, -3], [-3, -2], [-2, -1], [-1, 0]], [[-5, 0]]],
        [[[6, 8], [4, 0], [3, 5], [4, 7], [9, 10], [1, 40]], [[1, 40]]],
        [
            [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]],
            [[1, 2], [3, 8], [9, 10]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.mergeOverlappingIntervals(t[0])
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
