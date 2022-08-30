# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
#
# Tags: Array - Greedy - Sorting

import timeit
from typing import List


# Find the biggest horizontal and vertical slice sizes and multiply them
# to get the biggest area.
#
# Time complexity: O(n*log(n) + m*log(m)) - Where n is the number of
# horizontal cuts and m is the number of vertical cuts. The sorting step
# has the biggest complexity, if the input was sorted, it would be O(n).
# Space complexity: O(1) - We use constant space.
#
# Runtime: 343 ms, faster than 91.34%
# Memory Usage: 26.7 MB, less than 94.03%
class MaxSlices:
    def maxArea(
        self,
        h: int,
        w: int,
        horizontalCuts: List[int],
        verticalCuts: List[int],
    ) -> int:
        # Sorting the cutting arrays makes calculating the distance
        # between all cuts in linear time possible. O(nlog(n) + mlog(m)).
        horizontalCuts.sort()
        verticalCuts.sort()
        # Append the width and height to the end of the cuts arrays
        # because we are interested in the length of sections between
        # the cuts, we want to start at 0 and go to the height/width.
        horizontalCuts.append(h)
        verticalCuts.append(w)
        # Store the current maximum slice lengths found so far.
        max_vertical, max_horizontal = 0, 0
        # Initialize the left value at 0.
        previous_cut = 0
        # Iterate over all horizontal cuts in O(n) to find the longest
        # remaining horizontal section after cuts.
        for cut in horizontalCuts:
            max_horizontal = max(max_horizontal, cut - previous_cut)
            previous_cut = cut
        # Iterate over all vertical cuts in O(m) to find the longest
        # remaining vertical section after cuts.
        previous_cut = 0
        for cut in verticalCuts:
            max_vertical = max(max_vertical, cut - previous_cut)
            previous_cut = cut
        # The maximum area after cuts will be formed by the intersection
        # of the biggest horizontal and vertical sections. Return their
        # product modulo 10^9 + 7.
        return (max_vertical * max_horizontal) % 1000000007


# TODO add a O(n+m) time solution using bucket sort and the pigeon hole
# principle, similar to 164. Maximum Gap (Hard).


def test():
    executors = [MaxSlices]
    tests = [
        [5, 4, [1, 2, 4], [1, 3], 4],
        [5, 4, [3, 1], [1], 6],
        [5, 4, [3], [3], 9],
        [1000000000, 1000000000, [2], [2], 81],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxArea(t[0], t[1], t[2], t[3])
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
