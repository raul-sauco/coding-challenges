# 223. Rectangle Area
# 🟠 Medium
#
# https://leetcode.com/problems/rectangle-area/
#
# Tags: Math - Geometry

import timeit


# Compute the overlaps, if any, on the x and y axis and multiply them to
# get the size of the overlapping area.
#
# Time complexity: O(1)
# Space complexity: O(1)
#
# Runtime: 44 ms, faster than 99.38%
# Memory Usage: 13.9 MB, less than 71.27%
class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        # Compute the size of each rectangle.
        size_a = (ax2 - ax1) * (ay2 - ay1)
        size_b = (bx2 - bx1) * (by2 - by1)
        # If any of them has size 0, the resulting size is the other.
        # Compute the overlap on the x axis.
        x = max(min(ax2, bx2) - max(ax1, bx1), 0)
        # Compute the overlap on the y axis
        y = max(min(ay2, by2) - max(ay1, by1), 0)
        overlap = x * y
        # Return the size of both rectangles minus the size of the
        # overlap if any.
        return size_a + size_b - overlap


def test():
    executors = [Solution]
    tests = [
        [-2, -2, 2, 2, 3, 3, 4, 4, 17],
        [0, 0, 0, 0, -1, -1, 1, 1, 4],
        [-3, 0, 3, 4, 0, -1, 9, 2, 45],
        [-2, -2, 2, 2, -2, -2, 2, 2, 16],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.computeArea(
                    t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7]
                )
                exp = t[8]
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
