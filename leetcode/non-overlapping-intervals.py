# 435. Non-overlapping Intervals
# 🟠 Medium
#
# https://leetcode.com/problems/non-overlapping-intervals/
#
# Tags: Array - Dynamic Programming - Greedy - Sorting

import timeit
from typing import List


# Sort the intervals by start ascending and end descending order.
# Iterate over the sorted intervals keeping the last "used" interval
# stored in a variable, for each interval, we check if it overlaps the
# last interval we kept, if it does, we remove the one out of the two
# that ends later, to minimize collisions with later intervals.
#
# Time complexity: O(n*log(n)) - For the sorting. Then O(n) to check
# for overlapping intervals.
# Space complexity: O(n) - Sorting in python takes up to O(n/2) memory.
#
# Runtime: 2265 ms, faster than 72.50%
# Memory Usage: 52.7 MB, less than 59.13%
class Greedy:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by start time then reversed end time.
        intervals.sort(key=lambda i: (i[0], -i[1]))
        last = None
        res = 0
        for interval in intervals:
            if not last:
                last = interval
                continue
            # If this interval overlaps the last one we kept.
            if interval[0] < last[1]:
                res += 1
                # If this interval ends before last, remove last.
                if interval[1] < last[1]:
                    last = interval
            # Keep this interval.
            else:
                last = interval
        return res


def test():
    executors = [Greedy]
    tests = [
        [[[1, 2], [2, 3]], 0],
        [[[1, 2], [1, 2], [1, 2]], 2],
        [[[1, 2], [2, 3], [3, 4], [1, 3]], 1],
        [[[3, 5], [2, 3], [0, 2], [1, 4], [1, 3]], 2],
        [[[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.eraseOverlapIntervals(t[0])
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
