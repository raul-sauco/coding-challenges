# https://leetcode.com/problems/merge-intervals/

# Tags: Array - Sorting

import timeit
from typing import List

# Sort the list and iterate over the sorted list merging adjacent overlapping intervals.
#
# Time complexity: O(n*log(n)) from the sorting, the merging takes place in O(n)
# Space complexity: If the sorting is done in place O(log(n)) otherwise O(n) for the sorting data structure.
#
# Runtime: 152 ms, faster than 93.78% of Python3 online submissions for Merge Intervals.
# Memory Usage: 18.9 MB, less than 25.29% of Python3 online submissions for Merge Intervals.
class Iterative:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # The problem does not guarantee that the intervals are sorted
        intervals.sort()
        result = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                result[-1] = [result[-1][0], max(result[-1][1], end)]
            else:
                result.append([start, end])

        return result


def test():
    executors = [Iterative]
    tests = [
        [
            [[8, 10], [1, 3], [15, 18], [2, 6]],
            [[1, 6], [8, 10], [15, 18]],
        ],
        [
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
        ],
        [
            [[1, 4], [4, 5]],
            [[1, 5]],
        ],
        [
            [[1, 4], [2, 3]],
            [[1, 4]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.merge(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
