# 2187. Minimum Time to Complete Trips
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-time-to-complete-trips/
#
# Tags: Array - Binary Search

import timeit
from typing import List


# Use binary search to take guesses on the time that it can be needed
# for the n buses to complete k number of trips.
#
# Time complexity: O(n*log(k*t)) - Where n is the number of buses,
# k is the total number of trips to be completed and t is the time
# that the fastest bus needs to complete one trip.
# Space complexity: O(1) - Only pointers used, unless the list
# comprehension takes memory, in that case O(n) but it could be improved
# to O(1) using sum directly instead of the list comprehension.
#
# Runtime 1679 ms Beats 99%
# Memory 28.3 MB Beats 96.75%
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # The minimum and maximum possible time to complete k trips.
        l, r = 0, totalTrips * min(time)
        # Binary search the answer.
        while l < r:
            guess = (l + r) // 2
            # Can the buses complete k trips in guess amount of time?
            if sum([guess // req for req in time]) >= totalTrips:
                # Can we do it faster?
                r = guess
            else:
                # We definitely need more time
                l = guess + 1
        return l


def test():
    executors = [Solution]
    tests = [
        [[2], 1, 2],
        [[1, 2, 3], 5, 3],
    ]

    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimumTime(t[0], t[1])
                exp = t[2]
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
