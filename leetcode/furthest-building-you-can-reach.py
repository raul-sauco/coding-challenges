# https://leetcode.com/problems/furthest-building-you-can-reach/

from heapq import heappop, heappush, heapreplace
import timeit
from typing import List

# Solution using a heap
#
# Runtime: 828 ms, faster than 50.48% of Python3 online submissions for Furthest Building You Can Reach.
# Memory Usage: 28.6 MB, less than 16.41 % of Python3 online submissions for Furthest Building You Can Reach.


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) < 2:
            return 0
        heap = []
        for i in range(1, len(heights)):
            d = heights[i] - heights[i-1]
            if d > 0:
                # If we still have remaining ladders, use one
                if ladders > 0:
                    heappush(heap, d)
                    ladders -= 1
                else:
                    # No free ladders, check if we should have used one here
                    if heap and d > heap[0]:
                        gap = heapreplace(heap, d)
                    else:
                        gap = d

                    # Check if we have enough bricks to span the minimum gap
                    if gap > bricks:
                        return i-1
                    bricks -= gap

        return i


# Solution pushing into the heap each positive gap is about 15% slower.
#
# 1e5 calls
# Solution            0.55255   seconds
# BSolution           0.71058   seconds
class BSolution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1


def test():
    executor = [
        {'executor': Solution, 'title': 'Solution', },
        {'executor': BSolution, 'title': 'BSolution', },
    ]
    tests = [
        [[4, 2, 7, 6, 9, 14, 12], 5, 1, 4],
        [[4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7],
        [[14, 3, 19, 3], 17, 0, 3],
        [[1], 17, 20, 0],
        [[1, 20], 19, 0, 1],
        [[1, 20], 18, 0, 0],
        [[10, 9, 8, 7, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 1], 0, 0, 14],
        [[10, 9, 8, 7, 6, 6, 6, 6, 6, 6, 5, 4, 3, 4, 1], 0, 0, 12],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e5'))):
            for t in tests:
                sol = e['executor']()
                result = sol.furthestBuilding(t[0], t[1], t[2])
                assert result == t[3], f'{result} != {t[3]}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
