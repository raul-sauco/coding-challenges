# 973. K Closest Points to Origin
# 🟠 Medium
#
# https://leetcode.com/problems/k-closest-points-to-origin/
#
# Tags: Array - Math - Divide and Conquer - Geometry - Sorting -
# Heap (Priority Queue) - Quickselect

import timeit
from heapq import heappush, heappushpop
from typing import List


# Use a min heap to store the k elements closest to the origin. We can
# push or push and pop an element to the heap in O(log(k)).
#
# Time complexity: O(n*log(k)) - Pushing n elements into the heap at
# log(k) cost each, we could improve this checking if k is greater than
# n/2, in that case we could heapify the input in O(n) then pop n-k
# elements in O(log(k)), that would improve the complexity to
# O(min(k, n-k)*log(k))
# Space complexity: O(k) - The size of the heap.
#
# Runtime: 1756 ms, faster than 31.3%
# Memory Usage: 20.4 MB, less than 61.68%
class Heap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a heap to store the k closest points to the origin.
        heap = []
        # Iterate over the input points.
        for x, y in points:
            # Calculate the square of the distance to the origin
            dis = x * x + y * y
            # Push or push-and-pop to the heap preserving size k.
            if len(heap) < k:
                heappush(heap, (-dis, x, y))
            else:
                heappushpop(heap, (-dis, x, y))
        # Cast the heap elements to a list keeping only the second and
        # third values in each. Order is not important.
        return [[x, y] for d, x, y in list(heap)]


def test():
    executors = [Heap]
    tests = [
        [[[1, 3], [-2, 2]], 1, [[-2, 2]]],
        [[[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(10000):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.kClosest(t[0], t[1])
                exp = t[2]
                # The order is not important
                result.sort()
                exp.sort()
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
