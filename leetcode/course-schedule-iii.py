# https://leetcode.com/problems/course-schedule-iii/


import timeit
from heapq import heappop, heappush, heapreplace
from operator import itemgetter
from typing import List

# The two hints on the description are key to solving this problem:
#
# During iteration, say I want to add the current course, currentTotalTime being total time of
# all courses taken till now, but adding the current course might exceed my deadline or it doesn’t.
#
# 1. If it doesn’t, then I have added one new course. Increment the currentTotalTime with duration
# of current course.
#
# 2. If it exceeds deadline, I can swap current course with current courses that has biggest duration.
# * No harm done and I might have just reduced the currentTotalTime, right?
# * What preprocessing do I need to do on my course processing order so that this swap is always legal?
#
# I can first order the courses by their due time, then store durations in a max priority heap, if
# adding the current course would go over the current due date, I can check if the course with the
# longest duration, heap[0], has a longer duration, if yes, swap them.
#
# The swap is guaranteed to not put me over the deadline because the later course is guaranteed to
# have a later deadline, higher value of duration.
#
# Runtime: 741 ms, faster than 90.85% of Python3 online submissions for Course Schedule III.
# Memory Usage: 20.2 MB, less than 29.11 % of Python3 online submissions for Course Schedule III.


class Heap:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        t, heap = 0, []
        courses.sort(key=itemgetter(1))
        for dur, due in courses:
            if t + dur <= due:
                t += dur
                heappush(heap, -dur)
            elif heap and -heap[0] > dur:
                t += dur + heapreplace(heap, -dur)
        return len(heap)


# Use a heap to push and pop all durations.
#
# Runtime: 1233 ms, faster than 28.65% of Python3 online submissions for Course Schedule III.
# Memory Usage: 19.5 MB, less than 85.21 % of Python3 online submissions for Course Schedule III.


class PushPopAll:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        start = 0
        courses.sort(key=itemgetter(1))
        # for course in sorted(courses, key=itemgetter(1)):
        for course in courses:
            start += course[0]
            heappush(heap, -course[0])
            if start > course[1]:
                start += heappop(heap)
        return len(heap)


def test():
    executor = [
        {'executor': Heap, 'title': 'Heap', },
        {'executor': PushPopAll, 'title': 'PushPopAll', },
    ]
    tests = [
        [[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3],
        [[[1, 2]], 1],
        [[[3, 2], [4, 3]], 0],
        [[[1, 2], [2, 3]], 2],
        [[[5, 5], [4, 6], [2, 6]], 2],
        [[[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]], 4],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.scheduleCourse([*t[0]])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
