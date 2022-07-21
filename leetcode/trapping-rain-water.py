# https://leetcode.com/problems/trapping-rain-water/

# Tags: Array - Two Pointers - Dynamic Programming - Stack - Monotonic Stack

import timeit
from typing import List


# Use a pointer and a max_height from each end and add the maximum water that can
# be collected at each step.
#
# Time complexity: O(n) - we visit each position of the list once.
# Space complexity: O(1) - we use 5 variables independently of the size of the input.
#
# Runtime: 147 ms, faster than 71.76% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 15.9 MB, less than 77.48 % of Python3 online submissions for Trapping Rain Water.
class LinearFromBothEnds:
    def trap(self, height: List[int]) -> int:
        left_idx, right_idx = 0, len(height) - 1
        trapped, max_left, max_right = 0, height[0], height[-1]
        while right_idx > left_idx + 1:
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
                    w = i - stack[-1] - 1
                    trapped += (min(h, height[stack[-1]]) - height[deal]) * w
            stack.append(i)
        return trapped


def test():
    executors = [LinearFromBothEnds, UsingStack]
    tests = [
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
        [[4, 2, 0, 3, 2, 5], 9],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.trap(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
