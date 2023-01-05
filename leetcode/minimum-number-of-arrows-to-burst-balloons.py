# 452. Minimum Number of Arrows to Burst Balloons
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
#
# Tags: Array - Greedy - Sorting

import timeit
from typing import List


# Sort the balloons, then view them as intervals, each interval needs to
# be "hit" by, at least, one arrow. We can choose the first interval
# that has not been hit already and shot at its end point, then move to
# the next interval, if its start point is before/equal to the shot, it
# can be hit as well, we also need to check its end point and adjust
# the shot to make sure we also hit this new balloon shot = min(shot, end)
#
# Time complexity: O(n*log(n)) - The sorting step has the highest
# complexity, once sorted, we visit each balloon in the input once and
# do constant time operations with it.
# Space complexity: O(n) - Sorting in Python takes space.
#
# Runtime 1333 ms Beats 86.96%
# Memory 59.9 MB Beats 35.51%
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the intervals then greedily burst balloons.
        points.sort()
        # We are guaranteed to have, at least, one balloon, we need to
        # use one arrow to burst, greedily shot it at the end of the
        # interval trying to hit other balloons, we can move it back
        # later because the balloons are sorted.
        last_shot, arrows = points[0][1], 1
        # Iterate over the rest of the balloons finding the best shots
        # to burst them all.
        for start, end in points[1:]:
            # If this balloons start is before or the same as the last
            # shot, we can burst it with the same arrow.
            if start <= last_shot:
                # If the end of the balloon is before the last shot's
                # position, we need to move it back to make sure we hit
                # this balloon as well, we don't need to worry about the
                # start because balloons are sorted.
                if end < last_shot:
                    last_shot = end
            # If we could not hit this balloon using the previous arrow,
            # we will need to consume one more.
            else:
                last_shot = end
                arrows += 1
        return arrows


def test():
    executors = [Solution]
    tests = [
        [[[1, 5]], 1],
        [[[1, 5], [2, 5]], 1],
        [[[1, 2], [2, 5]], 1],
        [[[1, 2], [4, 5]], 2],
        [[[1, 2], [2, 3], [3, 4], [4, 5]], 2],
        [[[1, 2], [3, 4], [5, 6], [7, 8]], 4],
        [[[10, 16], [2, 8], [1, 6], [7, 12]], 2],
        [[[10, 16], [2, 8], [1, 6], [7, 12], [2, 4]], 2],
        [[[12, 16], [2, 7], [1, 6], [8, 11], [2, 4]], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findMinArrowShots(t[0])
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
