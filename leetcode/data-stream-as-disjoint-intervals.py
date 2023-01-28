# 352. Data Stream as Disjoint Intervals
# 🔴 Hard
#
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/
#
# Tags: Binary Search - Design - Ordered Set

import timeit
from typing import List


# Use bucket sorting and union find to create discrete groups, then
# sort the start of the discrete groups and return them as the result,
# if allowed to use sorted collections, we could use a sorted
# dictionary and return its values.
#
# Runtime 171 ms Beats 73.58%
# Memory 19 MB Beats 75.92%
class SummaryRanges:
    # O(10^4) time and space.
    def __init__(self):
        self.capacity = 10**4
        # A dictionary of group parent to the group interval.
        self.intervals = {}
        # An array of parents. None represents a value that we have not
        # seen yet.
        self.parents = [None for _ in range(self.capacity + 1)]

    # O(1) time and space.
    def union(self, a: int, b: int):
        pa, pb = self.findParent(a), self.findParent(b)
        # The representative needs to be the smaller value.
        if pa > pb:
            pa, pb = pb, pa
        # Merge interval b under a.
        self.intervals[pa] = (self.intervals[pa][0], self.intervals[pb][1])
        # Delete interval b.
        del self.intervals[pb]
        # Merge the disjoint sets.
        self.parents[pb] = pa

    # Amortized O(1) time and O(1) space, the array was created already.
    def findParent(self, a: int) -> int:
        if self.parents[a] != a:
            self.parents[a] = self.findParent(self.parents[a])
        return self.parents[a]

    # Amortized O(1) time because of the union and O(1) space, because
    # the array was created already and we only update a value.
    def addNum(self, value: int) -> None:
        # If the value had been seen, do nothing.
        if self.parents[value] is not None:
            return
        # Mark the value as seen.
        self.parents[value] = value
        # Create an interval with only one member.
        self.intervals[value] = (value, value)
        # Check if we have seen the value immediately after this one.
        if value + 1 <= self.capacity and self.parents[value + 1] is not None:
            self.union(value, value + 1)
        # Check if we have seen the value immediately before this one.
        if value - 1 >= 0 and self.parents[value - 1] is not None:
            self.union(value - 1, value)

    # O(k*log(k)) - Where k is the number of intervals, this number
    # will become smaller when it gets closer to the capacity because
    # as the number of values grows intervals will start to merge. Worts
    # case we can have 5*10^3 unique intervals, after that point adding
    # a value in guaranteed to result in a merge and decrease the number
    # of intervals.
    def getIntervals(self) -> List[List[int]]:
        return sorted(self.intervals.values())


# If we knew that there were many more insertions than reads, we can
# optimize the addNums method. The test cases in LeetCode seem to favor
# solutions that optimize reads instead, so this solution is not very
# performant.
#
# Runtime 4808 ms Beats 5.2%
# Memory 19 MB Beats 43.48%
class ArrayValues:
    def __init__(self):
        # O(10^4)
        self.capacity = 10**4
        # An array of values seen.
        self.seen = [False for _ in range(self.capacity + 1)]

    # O(1)
    def addNum(self, value: int) -> None:
        self.seen[value] = True

    # O(n) - We iterate over the entire array of size 10^4.
    def getIntervals(self) -> List[List[int]]:
        res = []
        for i, val in enumerate(self.seen):
            if val is True:
                if len(res) == 0 or not self.seen[i - 1]:
                    res.append([i, i])
                else:
                    res[-1][1] = i
        return res


def test():
    executors = [
        # SummaryRanges,
        ArrayValues,
    ]
    tests = [
        [
            [
                "SummaryRanges",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
                "addNum",
                "getIntervals",
            ],
            [[], [1], [], [3], [], [7], [], [2], [], [6], []],
            [
                None,
                None,
                [[1, 1]],
                None,
                [[1, 1], [3, 3]],
                None,
                [[1, 1], [3, 3], [7, 7]],
                None,
                [[1, 3], [7, 7]],
                None,
                [[1, 3], [6, 7]],
            ],
        ]
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    if call == "addNum":
                        result = getattr(sol, call)(t[1][i][0])
                    else:
                        # result = list(map(list, getattr(sol, call)()))
                        result = getattr(sol, call)()
                    exp = t[2][i]
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
