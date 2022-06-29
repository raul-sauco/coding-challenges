# https://leetcode.com/problems/trapping-rain-water/

import timeit
from typing import List


# Use a pointer and a max_height from each end and add the maximum water that can
# be collected at each step.
#
# Runtime: 147 ms, faster than 71.76% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 15.9 MB, less than 77.48 % of Python3 online submissions for Trapping Rain Water.
class LinearFromBothEnds:
    def trap(self, height: List[int]) -> int:
        left_idx, right_idx = 0, len(height)-1
        trapped, max_left, max_right = 0, height[0], height[-1]
        while right_idx > left_idx+1:
            if max_left >= max_right:
                right_idx -= 1
                if height[right_idx] > max_right:
                    max_right = height[right_idx]
                elif height[right_idx] < max_right:
                    trapped += max_right - height[right_idx]
            else:
                left_idx += 1
                if height[left_idx] > max_left:
                    max_left = height[left_idx]
                elif height[left_idx] < max_left:
                    trapped += max_left - height[left_idx]

        return trapped


# This should run slower, but in leetcode it seems to run a little faster
#
# Runtime: 133 ms, faster than 81.46% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 15.8 MB, less than 77.48 % of Python3 online submissions for Trapping Rain Water.
class UsingStack:
    def trap(self, height):
        trapped = 0
        stack = []
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                deal = stack.pop()
                if stack:
                    w = i-stack[-1]-1
                    trapped += (min(h, height[stack[-1]]) - height[deal]) * w
            stack.append(i)
        return trapped


def test():
    executor = [
        {'executor': LinearFromBothEnds, 'title': 'LinearFromBothEnds', },
        {'executor': UsingStack, 'title': 'UsingStack', },
    ]
    tests = [
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
        [[4, 2, 0, 3, 2, 5], 9],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.trap(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected} for {t[0]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
