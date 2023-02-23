# 502. IPO
# 🔴 Hard
#
# https://leetcode.com/problems/ipo/
#
# Tags: Array - Greedy - Sorting - Heap (Priority Queue)

import timeit
from heapq import heappop, heappush
from typing import List


# We want to greedily pick the job that gives us the maximum gain out of
# the jobs that are available to us. We can use a heap to keep a list of
# jobs sorted in reversed order by capital and a heap with the top
# element being the one that gives us the maximum profit, after we
# complete each job we update our current capital and iterate over the
# jobs adding any available jobs to the heap, then pick the top job from
# the heap in O(log(h)).
#
# Time complexity: O(n*log(n)) - Sorting n jobs has a O(n*log(n))
# complexity, then we iterate k times on which we pop elements from the
# sorted list in O(1) and append them to the heap in O(log(h)) where h
# is the current size of the heap and has an upper bound of n. Then we
# pop from the heap in O(log(h)), it would seem that the complexity is
# then O(k*n*log(n)) but, since any of the n jobs will be popped from the
# list and added to the heap a maximum of 1 time, we know that the limit
# of O(log(h)) insertions is n, since h is also bound to n, the time
# complexity of both sections of the algorithm is the same, O(n*log(n)).
# Space complexity: O(n) - Both the sorted list and the heap can grow to
# a size of n.
#
# Runtime 1023 ms Beats 74.65%
# Memory 38.7 MB Beats 82.34%
class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        # Create a list of jobs reverse sorted by capital.
        sorted_jobs = sorted(
            [(capital[i], profits[i]) for i in range(len(profits))],
            reverse=True,
        )
        heap, cap = [], w
        # Pick as many jobs as we can.
        for _ in range(k):
            # Update the heap with all newly available jobs.
            while sorted_jobs and sorted_jobs[-1][0] <= cap:
                _, p = sorted_jobs.pop()
                heappush(heap, -p)
            # Pick the top job or break if no jobs are available.
            if not heap:
                break
            cap -= heappop(heap)
        return cap


def test():
    executors = [Solution]
    tests = [
        [1, 0, [1, 2, 3], [1, 1, 2], 0],
        [2, 0, [1, 2, 3], [0, 1, 1], 4],
        [3, 0, [1, 2, 3], [0, 1, 2], 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findMaximizedCapital(t[0], t[1], t[2], t[3])
                exp = t[4]
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
