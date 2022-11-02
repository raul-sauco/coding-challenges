# 253. Meeting Rooms II
# 🟠 Medium
#
# https://leetcode.com/problems/meeting-rooms-ii/
# https://www.lintcode.com/problem/919/
#
# Tags: Array - Sorting - Greedy - Interval

import timeit
from typing import List

# 10e4 calls.
# » Recursive           0.01482   seconds
# » Iterative           0.00999   seconds
# » Greedy              0.01017   seconds

# Definition of Interval:
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Interval({self.start},{self.end})"


# Iterate over the intervals placing all intervals that we can into one
# meeting room and the ones that we can't into an array of non
# compatible meetings. Recursively call minMeetingRooms with that array
# and return the result of the recursive call plus 1 for the current
# meeting room.
#
# Time complexity: O(n^2) - If all meetings are incompatible, we will
# check each pair of meetings for compatibility.
# Space complexity: O(n) - The data structures and the call stack all
# can reach size n where n is the number of intervals.
#
# Runtime: 82 ms, faster than 61.60% on LintCode.
# Memory Usage: 6.07 MB, less than 61.60%
class Recursive:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        # Find all intervals that cannot use this meeting room.
        non_compat = []
        last = None
        for interval in intervals:
            if not last:
                last = interval
                continue
            if interval.start < last.end:
                non_compat.append(interval)
            else:
                last = interval
        return 1 + self.minMeetingRooms(non_compat)


# Similar idea to the previous solution. We place intervals into rooms
# as long as there is no overlap, when we find overlap we create a new
# room. For each interval, we iterate over the rooms until we find one
# that does not contain overlapping intervals, if none is found, we
# create a new room for the interval.
#
# Time complexity: O(n^2) - For each interval, we may iterate over all
# the rooms which can have the same length as the intervals.
# Space complexity: O(n) - The rooms array will have i rooms and an
# average of j meetings per room where i * j == number of intervals.
#
# Runtime: 101 ms, faster than 56.40% on LintCode.
# Memory Usage: 9.08 MB, less than 56.40%
class Iterative:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        intervals.sort(key=lambda interval: interval.start)
        for interval in intervals:
            placed = False
            # Try to find this interval a room out of the existing ones.
            for room in rooms:
                # If this meeting can take place in this room.
                if interval.start >= room[-1].end:
                    room.append(interval)
                    placed = True
                    break
            # If there are no rooms or this interval could not use any
            # of the existing rooms, create a new room.
            if not placed:
                rooms.append([interval])
        return len(rooms)


# We can use a greedy algorithm to solve this problem. Sort start and
# end times into their own arrays, use two pointers to visit the next
# "event" on the timeline, be it a start or end, by choosing the
# smaller element under either of the pointers, when we choose a start,
# we increase the count of meetings that are simultaneously taking
# place at that moment by one, when we choose and end, we decrease the
# same count also by one. The result is the highest count of
# simultaneous meetings that we see.
#
# Time complexity: O(n) - We visit each interval twice at most, one when
# we see its start value, and maybe one more when we see its end value.
# Space complexity: O(n) - The start and end array both have n items.
#
# Runtime: 102 ms, faster than 36.80% on LintCode.
# Memory Usage: 6.05 MB, less than 36.80%
class Greedy:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Store all the start and end times into two sorted arrays.
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        # Keep a pointer to the current element in each of the arrays.
        # Keep the count of simultaneous meetings.
        s_idx = e_idx = simultaneous = res = 0
        while s_idx < len(intervals):
            if starts[s_idx] < ends[e_idx]:
                simultaneous += 1
                s_idx += 1
            else:
                simultaneous -= 1
                e_idx += 1
            if simultaneous > res:
                res = simultaneous
        return res


def test():
    executors = [
        Recursive,
        Iterative,
        Greedy,
    ]
    tests = [
        [[(2, 7)], 1],
        [[(0, 8), (8, 10), (15, 20)], 1],
        [[(0, 30), (5, 10), (15, 20)], 2],
        [
            [
                (65, 424),
                (351, 507),
                (314, 807),
                (387, 722),
                (19, 797),
                (259, 722),
                (165, 221),
                (136, 897),
            ],
            7,
        ],
        [
            [
                (65, 424),
                (351, 507),
                (314, 807),
                (387, 722),
                (19, 797),
                (259, 722),
                (165, 221),
                (136, 897),
                (100, 259),
            ],
            7,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minMeetingRooms(
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
