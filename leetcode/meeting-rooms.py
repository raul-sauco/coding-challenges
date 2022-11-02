# 252. Meeting Rooms
# 🟢 Easy
#
# https://leetcode.com/problems/meeting-rooms/
#
# Tags: Array - Sorting - Interval

import timeit
from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Interval({self.start},{self.end})"


# Sort the intervals, then iterate over them making sure that the start
# time of all intervals is the same or later than the end time of the
# previous interval.
#
# Time complexity: O(n*log(n)) - The sorting step has the highest cost.
# Space complexity: O(n) - sort() in Python can take up to n/2 we could
# implement our ows sorting to bring it down to O(1).
#
# Runtime: 162 ms, faster than 97.00% on LintCode.
# Memory Usage: 9.08 MB, less than 97.00%
class Sorting:
    def canAttend(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True


def test():
    executors = [Sorting]
    tests = [
        [[(5, 8), (9, 15)], True],
        [[(0, 8), (8, 10), (15, 20)], True],
        [[(0, 30), (5, 10), (15, 20)], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.canAttend(
                    [Interval(start, end) for start, end in t[0]]
                )
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
