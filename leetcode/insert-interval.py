# https://leetcode.com/problems/insert-interval/

# Tags: Array

import timeit
from typing import List


# First check if we need to insert before all intervals
# Then iterate over the elements of intervals and for each element check if we need to insert before or merge
# Once we are done, check if we need to insert after the whole array
#
# Time complexity: O(n) we check all elements once
# Space complexity: O(n) we use a list to build the result set
#
# Runtime: 159 ms, faster than 17.84% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.2 MB, less than 92.25% of Python3 online submissions for Insert Interval.
class IterativeOneArray:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        result = []
        insert_start, insert_end = newInterval

        # Check if we need to insert before all elements
        if insert_end < intervals[0][0]:
            result.append(newInterval)

        for start, end in intervals:
            # Check if we need to insert between the previous element and the current element without merging
            if result and result[-1][1] < insert_start and insert_end < start:
                result.append(newInterval)
            # Check if we don't need to do anything
            if end < insert_start or start > insert_end:
                # Just insert this value
                result.append([start, end])
            # We need to merge
            else:
                # Merge the insert element with this element
                merged_start = min(start, insert_start)
                merged_end = max(end, insert_end)

                # Check if we need to merge with the previous element
                if result and result[-1][1] >= merged_start:
                    result[-1] = [result[-1][0], max(merged_end, result[-1][1])]
                # If result is empty, or the previous element's end is strictly before the merged start, just insert this element
                else:
                    result.append([merged_start, merged_end])

        # Check if we need to insert after all elements
        if result[-1][1] < insert_start:
            result.append(newInterval)

        return result


# Iterate over the elements but use newInterval to create the merged interval instead of using multiple conditionals.
#
# Time complexity: O(n) we check all elements once
# Space complexity: O(n) we use a list to build the result set
#
# Runtime: 87 ms, faster than 89.89% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.4 MB, less than 53.14% of Python3 online submissions for Insert Interval.
class IterUpdateInsert:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, int in enumerate(intervals):

            # If we can insert newInterval before the current interval, do it and return the result
            if newInterval[1] < int[0]:
                res.append(newInterval)
                return res + intervals[i:]

            # If the end of the current interval does not overlap the insert interval, append the current interval
            elif newInterval[0] > int[1]:
                res.append(int)

            # If there is overlap, start building the insert interval by merging the original one with the overlapping ones
            # but do not insert it yet
            else:
                newInterval = [min(newInterval[0], int[0]), max(newInterval[1], int[1])]

        # If the code gets here, newInterval could not fit before an existing interval and has not been inserted yet
        res.append(newInterval)
        return res


def test():
    executors = [IterativeOneArray, IterUpdateInsert]
    tests = [
        [[[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]],
        [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]],
        [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [2, 3], [[1, 5], [6, 7], [8, 10], [12, 16]]],
        [[], [1, 2], [[1, 2]]],
        [[[1, 5]], [6, 8], [[1, 5], [6, 8]]],
        [[[6, 8]], [1, 5], [[1, 5], [6, 8]]],
        [[[0, 4], [6, 8]], [1, 5], [[0, 5], [6, 8]]],
        [[[3, 5], [12, 15]], [6, 6], [[3, 5], [6, 6], [12, 15]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e4"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.insert(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
