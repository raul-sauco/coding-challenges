# 605. Can Place Flowers
# 🟢 Easy
#
# https://leetcode.com/problems/can-place-flowers/
#
# Tags: Array - Greedy

import timeit
from typing import List


# Iterate over the indexes in flower bed, if the element at the index
# does not already have a pot itself, or it is neighbor to a pot, place
# one of the flowers, return true if we place them all or false if we
# run out of flower bed before placing all flowers.
#
# Time complexity: O(f) - We may iterate the entire flower bed.
# Space complexity: O(1) - We use constant extra space.
#
# Runtime 168 ms Beats 62.38%
# Memory 14.4 MB Beats 65.78%
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        i = 0
        while i < len(flowerbed):
            # If we can place at the current index.
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                n -= 1
                if n == 0:
                    return True
                # If we placed, skip the next index.
                i += 2
            else:
                i += 1
        return False


# Use an extra array to simulate placing flowers in the flower bed, this
# is just to avoid mutating the input array but increases the space
# complexity of the solution.
#
# Time complexity: O(f) - We visit each element of the input array.
# Space complexity: O(f) - We make a copy of the input array.
#
# Runtime 163 ms Beats 78.96%
# Memory 14.4 MB Beats 65.78%
class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = [0] + flowerbed + [0]
        count = 0
        for i in range(1, len(placed) - 1):
            if placed[i]:
                count += 1
                continue
            if not placed[i - 1] and not placed[i + 1]:
                placed[i] = 1
                n -= 1
                if not n:
                    return True
        return not n


def test():
    executors = [
        Solution,
        Solution2,
    ]
    tests = [
        [[1], 0, True],
        [[1, 0, 0, 0, 1], 1, True],
        [[1, 0, 0, 0, 1], 2, False],
        [[1, 0, 0, 0, 0, 1], 2, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.canPlaceFlowers(t[0], t[1])
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
