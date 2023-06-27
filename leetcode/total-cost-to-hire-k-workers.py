# 2462. Total Cost to Hire K Workers
# 🟠 Medium
#
# https://leetcode.com/problems/total-cost-to-hire-k-workers/
#
# Tags: Array - Two Pointers - Heap (Priority Queue) - Simulation

import timeit
from collections import deque
from heapq import heappop, heappush
from typing import List


# Use two priority queues with c candidates each, pick the k candidates
# with the smallest cost form each of the queues.
#
# Time complexity: O(k*log(c)+n) - We push and pop into the heaps k +
# candidates items if there are enough in the input array, each push
# and each pop cost log(candidates). Creating the deque is O(n)
# Space complexity: O(c+n) - Each of the heaps stores candidates entries
# the deque has the same size as the input.
#
# Runtime 787 ms Beats 81.76%
# Memory 27 MB Beats 82.28%
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        deq = deque(costs)
        left, right = [], []
        for _ in range(candidates):
            if not deq:
                break
            heappush(left, deq.popleft())
            if not deq:
                break
            heappush(right, deq.pop())
        cost = 0
        for _ in range(k):
            if not left or (right and right[0] < left[0]):
                cost += heappop(right)
                if deq:
                    heappush(right, deq.pop())
            else:
                cost += heappop(left)
                if deq:
                    heappush(left, deq.popleft())
        return cost


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 4, 1], 3, 3, 4],
        [[17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4, 11],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.totalCost(t[0], t[1], t[2])
                exp = t[3]
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
