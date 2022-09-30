# 218. The Skyline Problem
# 🔴 Hard
#
# https://leetcode.com/problems/the-skyline-problem/
#
# Tags: Array - Divide and Conquer - Binary Indexed Tree - Segment Tree -
# Line Sweep - Heap (Priority Queue) - Ordered Set

import timeit
from heapq import heappop, heappush
from typing import List


# Iterate over the input buildings using a heap to store buildings that
# could affect the skyline sorted by height descending. Before adding
# the current building to the heap, pop any buildings which right ends
# are further left than the left side of the current building from the
# heap, checking how going past them would affect the skyline. Then push
# the current building into the heap and check if it would modify the
# current maximum height.
#
# Time complexity: O(n*log(n)) - We iterate over the buildings in O(n),
# but the main complexity comes from pushing and popping all of them
# in and out of the heap at O(log(n)) each.
# Space complexity: O(n) - The heap can grow to the same size as the
# input.
#
# Runtime: 180 ms, faster than 74.68%
# Memory Usage: 18.8 MB, less than 95.50%
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Use a list to add skyline points.
        skyline = []
        # Use a heap to keep buildings that we have seen.
        # A building is a tuple of (height, left_x, right_x)
        heap = []
        # Define a function that pops from the heap taking into account
        # writing height changes to the output.
        def popHead() -> None:
            height, _, r = heappop(heap)
            # If the next lower building in the heap has a right edge
            # to the left of the current one, pop it as well.
            while heap and heap[0][2] < r:
                heappop(heap)
            new_height = -heap[0][0] if heap else 0
            if not heap or height < heap[0][0]:
                # That was the last building or the next height is going
                # to be lower than the previous one when we go passed
                # this building, record this height change into the
                # skyline. Check if this height has the same right edge
                # as the last one seen. If yes, overwrite it.
                if r == skyline[-1][0]:
                    skyline[-1] = [r, new_height]
                # If the x value at which the heights change is new,
                # append it to the result skyline.
                else:
                    skyline.append([r, new_height])

        # Iterate over all the positions up to the right boundary.
        for l, r, h in buildings:
            # Pop expired elements from the heap.
            while heap and heap[0][2] < l:
                popHead()
            # Push this element to the heap.
            heappush(heap, (-h, l, r))
            # If this is the first building add it.
            if not skyline or skyline[-1][1] == 0:
                skyline.append([l, h])
                continue
            # If this building is taller.
            if -heap[0][0] > skyline[-1][1]:
                # If this building started at the same point as the
                # previous one, overwrite the previous height.
                if l == skyline[-1][0]:
                    skyline[-1] = [l, h]
                else:
                    skyline.append([heap[0][1], -heap[0][0]])
        # Process the heap leftover buildings.
        while heap:
            popHead()

        return skyline


def test():
    executors = [Solution]
    tests = [
        [
            [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
        ],
        [
            [[0, 2, 3], [2, 5, 3]],
            [[0, 3], [5, 0]],
        ],
        [
            [[1, 2, 5], [1, 5, 3], [1, 4, 7]],
            [[1, 7], [4, 3], [5, 0]],
        ],
        [
            [[1, 8, 5], [2, 8, 7], [4, 8, 11]],
            [[1, 5], [2, 7], [4, 11], [8, 0]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.getSkyline(t[0])
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
