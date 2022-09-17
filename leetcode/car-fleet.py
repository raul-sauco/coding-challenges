# 853. Car Fleet
# 🟠 Medium
#
# https://leetcode.com/problems/car-fleet/
#
# Tags: Array - Stack - Sorting - Monotonic Stack

import timeit
from typing import List


# We can use a greedy approach because the cars cannot overtake each
# other. Start processing cars starting from the one closest to the
# target, keep track of how many time units it takes to get to the
# target, any cars that take strictly more time than the previous fleet
# to arrive at the target will create its own fleet.
#
# Time complexity: O(n*log(n)) - Sorting the cars by position has the
# highest complexity, then we can process them in O(n).
# Space complexity: O(n) - Sorted uses time sort with O(n), zip uses O(n)
# as well.
#
# Runtime: 922 ms, faster than 98.61%
# Memory Usage: 36.1 MB, less than 58.17%
class Solution:
    def carFleet(
        self, target: int, position: List[int], speed: List[int]
    ) -> int:
        # Initialize the number of fleets seen.
        fleets = 0
        # Initialize the last arrival time seen.
        last = float("-inf")
        # Sort the cars based on their position
        for p, s in sorted(zip(position, speed), reverse=True):
            # Compute the eta for this car if it had no cars in front.
            eta = (target - p) / s
            # If this car's eta is strictly higher than the previous car
            # that we saw, it will create its own fleet.
            if eta > last:
                fleets += 1
                last = eta
            # Else, this car will run into some car ahead of it and
            # fleet-up.
        return fleets


def test():
    executors = [Solution]
    tests = [
        [10, [3], [3], 1],
        [100, [0, 2, 4], [4, 2, 1], 1],
        [12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.carFleet(t[0], t[1], t[2])
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
