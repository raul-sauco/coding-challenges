# 1011. Capacity To Ship Packages Within D Days
# 🟠 Medium
#
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
#
# Tags: Array - Binary Search

import timeit
from typing import List


# Use binary search to determine the minimum size of ship that lets us
# ship all the weights in the given amount of time. The binary search
# uses an auxiliary function to determine whether shipping is feasible
# given a ship size.
#
# Time complexity: O(n*log(n)) - Linear time over the number of weights
# to determine whether a ship size is suitable and log(n) over the
# ship sizes, bounded by the max weight on the bottom and the total
# weights on top, which makes it equivalent to n.
# Space complexity: O(1) - Constant extra space used.
#
# Runtime 521 ms Beats 60.62%
# Memory 17 MB Beats 78.6%
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The smallest and biggest size ship
        l, r = max(weights), sum(weights)
        # Define a function that computes whether we can ship the given
        # weights in the given number of days with the given ship size.
        def canShip(ship_size: int) -> bool:
            # Number of days used to ship all weights.
            shipping_days = 0
            # Remaining capacity in the current ship.
            remaining_capacity = 0
            # Iterate over the weights.
            for weight in weights:
                if remaining_capacity < weight:
                    shipping_days += 1
                    remaining_capacity = ship_size
                remaining_capacity -= weight
                if shipping_days > days:
                    return False
            return True

        while l < r:
            mid = (l + r) // 2
            # If we can ship using a ship of this size, we want to move
            # the right pointer to this spot, we cannot move it to mid-1
            # because we are not guaranteed that we can ship using that
            # value.
            if canShip(mid):
                r = mid
            # If we cannot ship using a ship of that size, we know that
            # we need to use, at least, a ship one unit greater.
            else:
                l = mid + 1
        # l is the smallest ship size that we can use.
        return l


# Use binary search to determine the minimum size of ship that lets us
# ship all the weights in the given amount of time. This solution is
# equivalent to the previous one except for inlining the function that
# checks whether we can ship given a ship size.
#
# Time complexity: O(n*log(n)) - Linear time over the number of weights
# to determine whether a ship size is suitable and log(n) over the
# ship sizes, bounded by the max weight on the bottom and the total
# weights on top, which makes it equivalent to n.
# Space complexity: O(1) - Constant extra space used.
#
# Runtime 508 ms Beats 67.61%
# Memory 17 MB Beats 97.85%
class Inline:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The smallest and biggest size ship
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            ships, remaining_capacity = 0, 0
            for weight in weights:
                # If we can't put this weight in the current ship,
                # consume one extra ship and reset the remaining capacity.
                if remaining_capacity < weight:
                    ships += 1
                    remaining_capacity = mid
                remaining_capacity -= weight
                # If we need more days than are available.
                if ships > days:
                    l = mid + 1
                    break
            else:
                # If we could ship all weights with the given ship size.
                r = mid
        # l is the smallest ship size that we can use.
        return l


def test():
    executors = [
        Solution,
        Inline,
    ]
    tests = [
        [[1, 2, 3, 1, 1], 4, 3],
        [[3, 2, 2, 4, 1, 4], 3, 6],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.shipWithinDays(t[0], t[1])
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
