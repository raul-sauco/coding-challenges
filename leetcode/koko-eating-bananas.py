# 875. Koko Eating Bananas
# 🟠 Medium
#
# https://leetcode.com/problems/koko-eating-bananas/
#
# Tags: Array - Binary Search

import timeit
from typing import List


# It isn't evident, but this problem can be solved using binary search
# if we think of it in terms of: we are looking for a number between
# two others such that koko can finish all her bananas.
# We know that we need to eat, at least, 1 banana. The right
# boundary is the number of bananas in the biggest pile, because we
# know that we can finish the piles eating one per hour.
#
# Time complexity: O(p*log(b - p)) - b: max number of bananas in pile,
# p: number of piles.
# Space complexity: O(1)
#
# Runtime: 667 ms, faster than 57.73%
# Memory Usage: 15.6 MB, less than 24.04%
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Define a helper function that determines whether koko can
        # finish all the bananas at a given speed.
        def canFinish(k: int) -> bool:
            # Iterate through the piles subtracting, for each pile, the
            # amount of hours that koko will use to finish it up.
            remaining = h
            for p in piles:
                # Ceiling division, faster to use integer division than
                # remaining -= math.ceil(p / k)
                # https://stackoverflow.com/a/17511341/2557030
                remaining += p // -k
                # If we determine that koko cannot finish all the piles
                # at rate k, return false.
                if remaining < 0:
                    return False
            # Koko would be able to finish the piles at rate k.
            return True

        # Set the search boundaries.
        left, right = 0, max(piles)
        # We are looking for the lowest number that fulfills the
        # requirements, similar to First Bad Version.
        while right > left + 1:
            mid = (left + right) // 2
            if canFinish(mid):
                # It could be this value or a smaller one.
                right = mid
            else:
                # It could be this value or a bigger one.
                left = mid

        return right


def test():
    executors = [Solution]
    tests = [
        [[3], 10, 1],
        [[3, 6, 7, 11], 8, 4],
        [[30, 11, 23, 4, 20], 5, 30],
        [[30, 11, 23, 4, 20], 6, 23],
        [
            [
                332484035,
                524908576,
                855865114,
                632922376,
                222257295,
                690155293,
                112677673,
                679580077,
                337406589,
                290818316,
                877337160,
                901728858,
                679284947,
                688210097,
                692137887,
                718203285,
                629455728,
                941802184,
            ],
            823855818,
            14,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.minEatingSpeed(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
