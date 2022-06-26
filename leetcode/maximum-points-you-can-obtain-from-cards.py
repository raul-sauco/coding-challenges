# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


import timeit
from typing import List

# Create a sliding window of size k and find the window with the minimum sum inside cardPoints.
# The maximum sum we can obtain will be the total sum of the cards minus the sum of the minimum
# sliding window found.
#
# Runtime: 439 ms, faster than 93.92% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
# Memory Usage: 27 MB, less than 95.20 % of Python3 online submissions for Maximum Points You Can Obtain from Cards.


class RightToLeft:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_points = sum(cardPoints)
        remove = len(cardPoints) - k
        if remove == 0:
            return total_points
        current = sum(cardPoints[:remove])
        m = current
        l, r = 0, remove - 1
        while r < len(cardPoints)-1:
            r += 1
            current = current + cardPoints[r] - cardPoints[l]
            l += 1
            # m = min(current, m)
            if current < m:
                m = current
        return total_points - m


# Use negative indexes to simplify the code
class LeftToRight:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        l, r = 0, k
        c = a = sum(cardPoints[l:r])
        while r > 0:
            l -= 1
            r -= 1
            c = c + cardPoints[l] - cardPoints[r]
            if c > a:
                a = c
        return a


def test():
    executor = [
        {'executor': RightToLeft, 'title': 'RightToLeft', },
        {'executor': LeftToRight, 'title': 'LeftToRight', },
    ]
    tests = [
        [[1, 2, 3, 4, 5, 6, 1], 3, 12],
        [[2, 2, 2], 2, 4],
        [[9, 7, 7, 9, 7, 7, 9], 7, 55],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.maxScore([*t[0]], t[1])
                expected = t[2]
                assert result == expected, f'{result} != {expected} for {t[0]}:{t[1]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
