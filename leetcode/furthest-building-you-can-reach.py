# 1642. Furthest Building You Can Reach
# 🟠 Medium
#
# https://leetcode.com/problems/furthest-building-you-can-reach/
#
# Tags: Array - Greedy - Heap (Priority Queue)

import timeit
from heapq import heappop, heappush, heapreplace
from typing import List


# Iterate over the input, greedily use ladders saving the gap sizes we
# bridge using ladders in a heap, once we run out of ladders, every time
# we see a positive height gain, compare with the top of the heap, if
# the top of the heap is smaller, pretend we used bricks to save that
# gap and we still have one ladder to bridge the current one, until we
# run out of bricks.
#
# Time complexity: O(n*log(n)) - We visit each element in the input, for
# each, we may push and pop from the heap in O(log(n))
# Space complexity: O(l) - The heap can have as many entries as the
# number of ladders.
#
# Runtime 441 ms Beats 30.55%
# Memory 30.92 MB Beats 92.76%
class MinHeapSolution:
    def furthestBuilding(
        self, heights: List[int], bricks: int, ladders: int
    ) -> int:
        if len(heights) < 2:
            return 0
        heap = []
        for i in range(1, len(heights)):
            d = heights[i] - heights[i - 1]
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
                        return i - 1
                    bricks -= gap

        return i


# Similar to the previous solution but "use bricks" for each gap we
# encounter until we run out of bricks, saving them all in a max heap.
# Once we encounter a gap that we cannot bridge using bricks, substitute
# the greatest gap found so far for a ladder, keep doing that until we
# are out of ladders and we don't have enough bricks to bridge the next
# gap or we get to the end.
#
# Time complexity: O(n*log(n)) - We visit each element in the input,
# for each, we may push and pop from the heap in O(log(n))
# Space complexity: O(n) - The heap can have as many entries as the
# elements in the input.
#
# Runtime 415 ms Beats 82.83%
# Memory 31.15 MB Beats 57.95%
class MaxHeapSolution:
    def furthestBuilding(
        self, heights: List[int], bricks: int, ladders: int
    ) -> int:
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
    executors = [
        MinHeapSolution,
        MaxHeapSolution,
    ]
    tests = [
        [[1], 17, 20, 0],
        [[1, 20], 19, 0, 1],
        [[1, 20], 18, 0, 0],
        [[14, 3, 19, 3], 17, 0, 3],
        [[4, 2, 7, 6, 9, 14, 12], 5, 1, 4],
        [[4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7],
        [[10, 9, 8, 7, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 1], 0, 0, 14],
        [[10, 9, 8, 7, 6, 6, 6, 6, 6, 6, 5, 4, 3, 4, 1], 0, 0, 12],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.methodCall(t[0])
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
