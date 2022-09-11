# 1383. Maximum Performance of a Team
# 🔴 Hard
#
# https://leetcode.com/problems/maximum-performance-of-a-team/
#
# Tags: Array - Greedy - Sorting - Heap (Priority Queue)

import timeit
from heapq import heappop, heappush, heappushpop
from typing import List

# Question hints:
#
# Keep track of the engineers by their efficiency in decreasing order.
# Starting from one engineer, to build a team, it suffices to bring K-1
# more engineers who have higher efficiencies as well as high speeds.
#
# Choose at most k different engineers out of the n engineers to form a
# team with the maximum performance.
#
# The performance of a team is the sum of their engineers' speeds
# multiplied by the minimum efficiency among their engineers.

# Sort the engineers on descending order of efficiency O(n*log(n)), then
# start iterating over the sorted engineers, keeping a heap of size k
# with the highest k or less speeds that we have seen up to this point.
# For each engineer that we see, calculate the result of adding this
# engineer to the team. We can do that comparing its speed to the top of
# the heap, if necessary, push and pop from it a smaller value and
# adjust the running sum as needed. We multiply the running sum by the
# current engineer's efficiency, which is guaranteed to be the smallest
# efficiency value seen so far, even though there may be other equal
# values that have been used already. This way, for each engineer seen,
# we can calculate the result of using it on the team in O(log(k)), then
# we compare this value to the best that we have seen so far and keep
# the best.
#
# Time complexity: O(n*log(n)) - Sorting the array, there is also the
# extra complexity of iterating over the engineers computing the result
# of adding them to the team, but that cost O(n*log(k)) is superseded by
# the cost of sorting.
# Space complexity: O(n) - The sorting takes place in memory, there is
# also O(k) for the heap, but that is also superseded by the sorting
# iterator.
#
# Runtime: 406 ms, faster than 94.94%
# Memory Usage: 29.6 MB, less than 95.36%
class SortAndHeap:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        MOD = 1000000007  # 10**9 + 7
        # Initialize the best result seen and the cumulative sum of
        # efficiencies, since we are using only positive values, we can
        # initialize them to 0.
        res = cumulative_speed_sum = 0
        # Use a heap to be able to store, and update, the highest up to
        # k engineer speed values seen. This is the greedy part of the
        # algorithm, since the engineers are sorted from highest to
        # lowest efficiency, there will never be an advantage to taking
        # less than the maximum number of speeds that we are allowed to
        # take, max(visited, k)
        heap = []
        # Iterate over the engineers sorted by descending efficiency.
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            # Initialize the loop variables.
            popped_speed = 0
            pushed = False
            # If the heap is not full just push into the heap.
            if len(heap) < k:
                heappush(heap, s)
                pushed = True
            # Else, if the  speed of this engineer is better than the
            # worst currently in the heap.
            elif s > heap[0]:
                popped_speed = heappushpop(heap, s)
                pushed = True
            # If we have updated the heap, compute the result of the
            # update.
            if pushed:
                # Add the new engineer's speed and remove the one popped
                # from the heap, 0 if no value was popped.
                cumulative_speed_sum += s - popped_speed
                # Compute the result of adding this engineer to the
                # team, since engineers are sorted, this efficiency is
                # the lowest value seen, we need to use it, the heap
                # provides the optimal combination of engineer speeds.
                performance = cumulative_speed_sum * e
                # Use a nested conditional instead of max
                if performance > res:
                    res = performance

        return res % MOD


def test():
    executors = [SortAndHeap]
    tests = [
        [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60],
        [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3, 68],
        [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4, 72],
        [6, [2, 10, 13, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 69],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxPerformance(t[0], t[1], t[2], t[3])
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
