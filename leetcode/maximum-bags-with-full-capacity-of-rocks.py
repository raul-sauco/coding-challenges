# 2279. Maximum Bags With Full Capacity of Rocks
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
#
# Tags: Array - Greedy - Sorting

import timeit
from heapq import heapify, heappop
from typing import List

# This is a template that can be used as the starting point of a
# solution with minimal changes.


# We need to compute each bag's remaining space and then start adding
# rocks to the bags that have the least amount of remaining space,
# because we are trying to maximize the number of bags that we fill.
# One way to do that is to compute the remaining space and use a heap to
# store it, then start popping from the heap and subtracting the
# amount of rocks that we need to use to fill each bag from the amount
# of bags that we have remaining. Stop once we don't have enough rocks
# to fill the next bag or we have filled all the bags.
#
# Time complexity: O(n*log(n)) - We pop n elements from the heap at
# a log(n) cost.
# Space complexity: O(n) - The remaining capacity array.
#
# Runtime: 944 ms Beats 93.9%
# Memory: 22.2 MB Beats 49.34%
class UseHeap:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        remaining_space = [capacity[i] - rocks[i] for i in range(len(rocks))]
        heapify(remaining_space)
        remaining_rocks, maxed_out_bags = additionalRocks, 0
        while (
            remaining_space
            and (current := heappop(remaining_space)) <= remaining_rocks
        ):
            remaining_rocks -= current
            maxed_out_bags += 1
        return maxed_out_bags


# Time complexity: O(n*log(n)) - We sort the capacity array of n items.
# Space complexity: O(n) - The remaining capacity array.
#
# Runtime: 944 ms Beats 93.9%
# Memory: 22.4 MB Beats 32.89%
class UseSortedArray:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        rem, i = sorted([capacity[i] - rocks[i] for i in range(len(rocks))]), 0
        while i < len(rocks) and rem[i] <= additionalRocks:
            additionalRocks -= rem[i]
            i += 1
        return i


def test():
    executors = [
        UseHeap,
        UseSortedArray,
    ]
    tests = [
        [[10, 2, 2], [2, 2, 0], 100, 3],
        [[2, 3, 4, 5], [1, 2, 4, 4], 2, 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maximumBags(t[0], t[1], t[2])
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
