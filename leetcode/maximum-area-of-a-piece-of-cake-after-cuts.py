# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

import timeit
from typing import List

# Intuition; find the biggest horizontal and vertical slice sizes and multiply them to get the biggest area.
#
# Runtime: 343 ms, faster than 91.34% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
# Memory Usage: 26.7 MB, less than 94.03 % of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        max_vertical, max_horizontal = 0, 0
        previous_cut = 0
        for cut in horizontalCuts:
            max_horizontal = max(max_horizontal, cut - previous_cut)
            previous_cut = cut
        previous_cut = 0
        for cut in verticalCuts:
            max_vertical = max(max_vertical, cut - previous_cut)
            previous_cut = cut
        return (max_vertical * max_horizontal) % 1000000007


def test():
    executor = [
        {'executor': Solution, 'title': 'Solution', },
    ]
    tests = [
        [5, 4, [1, 2, 4], [1, 3], 4],
        [5, 4, [3, 1], [1], 6],
        [5, 4, [3], [3], 9],
        [1000000000, 1000000000, [2], [2], 81],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = e['executor']()
                result = sol.maxArea(t[0], t[1], t[2], t[3])
                expected = t[4]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
