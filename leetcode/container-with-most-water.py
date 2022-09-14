# 11. Container With Most Water
# 🟠 Medium
#
# https://leetcode.com/problems/container-with-most-water/
#
# Tags: Array - Two Pointers - Greedy

import timeit
from typing import List


# Use a two pointer approach, start at both ends and shrink the window
# from the smaller height, keeping track of the biggest container seen.
#
# Time complexity: O(n) - We visit each height once.
# Space complexity: O(1) - Constant space.
#
# Runtime: 1098 ms, faster than 56.31%
# Memory Usage: 27.5 MB, less than 12.16%
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # No base case 2 <= len(height)
        # Keep track of the biggest container seen.
        greatest = 0
        # Initialize two pointers.
        l, r = 0, len(height) - 1
        # Keep iterating while we have window left between the pointers.
        while l < r:
            # Compare the current area with the max found.
            greatest = max(greatest, (r - l) * min(height[l], height[r]))
            # Shrink from the smaller height in.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        # Return the max area found.
        return greatest


def test():
    executors = [Solution]
    tests = [
        [[1, 1], 1],
        [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 12],
        [[1, 3, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1], 15],
        [[1, 1, 1, 1, 1, 1, 2, 1, 1, 8, 1, 8, 1], 16],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxArea(t[0])
                exp = t[1]
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
