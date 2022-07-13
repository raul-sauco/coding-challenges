# https://leetcode.com/problems/last-stone-weight/

# Tags: Array - Heap (Priority Queue)

import timeit
from heapq import heapify, heappop, heappush, heapreplace
from typing import List


# Use a heap to access the two biggest elements and subtract the smallest from the biggest.
# If the result is greater than 0, push it into the heap.
#
# Time complexity: O(n*log(n)) each time we push into the heap costs O(log(n)) and we may push and pop each item
# Space complexity: O(n) we have a heap of size n
#
# Runtime: 57 ms, faster than 28.34% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 61.83% of Python3 online submissions for Last Stone Weight.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        stones = [-x for x in stones]
        heapify(stones)

        while len(stones) > 1:
            result = heappop(stones) - heappop(stones)
            if result < 0:
                heappush(stones, result)

        return -1 * stones[0] if stones else 0


def test():
    executors = [Solution]
    tests = [
        [[2, 7, 4, 1, 8, 1], 1],
        [[1], 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.lastStoneWeight(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
