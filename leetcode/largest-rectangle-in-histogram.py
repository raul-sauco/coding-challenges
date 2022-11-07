# 84. Largest Rectangle in Histogram
# 🔴 Hard
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/
#
# Tags: Array - Stack - Monotonic Stack

import timeit
from typing import List

# 10e3 calls.
# » Naive               0.02904   seconds
# » MonotonicStack      0.01783   seconds
# » DivideAndConquer    0.08459   seconds

# Use a min monotonic stack where each entry is a tuple (height, index).
# While correct, this implementation fails to pass the tests because it
# computes the rectangle between all the heights in the stack and a
# newly added height each time one is added. The next solution shows how
# we can avoid doing this O(n^2) work.
#
# Time complexity: O(n^2) - In the worst case, we keep pushing new
# heights into the stack without popping any, at O(n) per push.
# Space complexity: O(n) - We store all heights in the stack.
#
# Fails with Time Limit Exceeded.
class Naive:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        # Store the largest rectangle seen so far.
        res = 0
        # Initialize the stack with the height 0 just left of the
        # first index.
        stack = [(0, -1)]
        for idx, height in enumerate(heights):
            # Avoid adding this element as long as the next element has
            # the same height and it is not the last one. Pass LC 96.
            if idx < len(heights) - 1 and heights[idx + 1] == height:
                continue
            # Pop any heights greater than or equal to the current one.
            while stack and stack[-1][0] >= height:
                stack.pop()
            stack.append((height, idx))
            # Calculate the area of all rectangles that we can build
            # using the newly added height.
            for i in range(len(stack) - 1):
                # Area = base * h
                # The base for this height goes all the way from this
                # index to the current index.
                base = idx - stack[i][1]
                # The height is the height of the next lowest histogram
                # column.
                h = stack[i + 1][0]
                area = base * h
                if area > res:
                    res = area

        return res


# Use a monotonic non-decreasing stack. Add boundary 0s to the start and
# end of the heights array, to symbolize that rectangles cannot be
# extended to include this positions. The left 0 boundary also
# guarantees that the stack will never be empty, letting us avoid having
# to check in each iteration of the inner loop. Iterate over the heights
# array, when we see a height smaller than the top of the stack, we pop
# it and calculate the rectangle that can be obtained between the
# popped height and the first smaller height to its left. We keep the
# largest area found to return as the result of the function.
#
# Time complexity: O(n) - We iterate once over the input array, each
# height can be, at most, pushed into and popped from the stack once,
# and we calculate an area every time we pop from the stack, that is a
# maximum of n area calculations.
# Space complexity: O(n) - The stack can grow to the same size as the
# input.
#
# Runtime: 2061 ms, faster than 66.19%
# Memory Usage: 27.1 MB, less than 99.30%
class MonotonicStack:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add two boundaries to the heights array. Initialize the stack
        # to contain the left 0 height to avoid having to check for
        # an empty stack at each iteration. Initialize the max at 0.
        heights, stack, res = [0] + heights + [0], [0], 0
        for i in range(1, len(heights)):
            # Shortcut to avoid computing each rectangle in a set of
            # bars of the same height, it will only compute the max.
            if heights[i] == heights[stack[-1]]:
                stack[-1] = i
                continue
            # Keep the stack non-decreasing by popping any greater
            # elements before appending.
            while heights[i] < heights[stack[-1]]:
                # Use any indexes popped from the stack to compute the
                # area of the rectangle that could be obtained between
                # that height and the next smaller height to its left.
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res


# Use a divide-and-conquer strategy, the max area of each section will
# be the max area of the bars left of the middle, the bars right of the
# middle, or the section that contains the middle bar.
#
# Time complexity: O(n*log(n)) - At each step the algorithm divides the
# input into two halves and also calculates the result of using the
# middle heights with O(n), the division can happen O(log(n)) times.
# Space complexity: O(log(n)) - The call stack can grow to a height of
# log(n), each call holds a reference to the input array and some
# pointers, all of them constant space.
#
# Runtime: 9960 ms, faster than 5.1%
# Memory Usage: 27.6 MB, less than 87.99%
class DivideAndConquer:
    def maxCombinedArea(
        self, heights: List[int], l: int, mid: int, r: int
    ) -> int:
        # Expand from the middle in O(1) to find the max area containing
        # the two central bars heights[mid] and heights[mid + 1]
        i, j, area = mid, mid + 1, 0
        h = min(heights[i], heights[j])
        while i >= l and j <= r:
            h = min(h, min(heights[i], heights[j]))
            area = max(area, (j - i + 1) * h)
            # If one side has reached the boundary, expand on the other
            # side only.
            if i == l:
                j += 1
            elif j == r:
                i -= 1
            # If both sides still have room to expand, do it on the side
            # that has a bigger height.
            else:
                if heights[i - 1] > heights[j + 1]:
                    i -= 1
                else:
                    j += 1
        return area

    # Worker function that computes the max area between two points.
    def maxArea(self, heights: List[int], l: int, r: int) -> int:
        # The area of a single bar is its height.
        if l == r:
            return heights[l]
        mid = l + (r - l) // 2
        # Divide and conquer, the max area is either left, right or
        # contains mid.
        return max(
            self.maxArea(heights, l, mid),  # Left.
            self.maxArea(heights, mid + 1, r),  # Right.
            self.maxCombinedArea(heights, l, mid, r),  # Overlapping mid.
        )

    # Main function, exposes a public API expected by consumers.
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # For tests that contain only one value. LC 92 is 10e5 8793
        if len(set(heights)) == 1:
            return len(heights) * heights[0]
        # Call the worker function with the entire input array.
        return self.maxArea(heights, 0, len(heights) - 1)


# DivideAndConquer solution inspired on the Java version here:
# https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/
# 28910/simple-divide-and-conquer-ac-solution-without-segment-tree/


def test():
    executors = [
        Naive,
        MonotonicStack,
        DivideAndConquer,
    ]
    tests = [
        [[0], 0],
        [[0, 0], 0],
        [[2, 4], 4],
        [[2, 1, 5, 6, 2, 3], 10],
        [[0, 0, 0, 2, 4, 5, 0, 0, 0, 7, 0], 8],
        [
            [3, 1, 6, 4, 3, 6, 6, 2, 7, 1, 1, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5, 4],
            28,
        ],
        [
            [3, 2, 6, 4, 3, 6, 6, 2, 7, 2, 2, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5, 4],
            44,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.largestRectangleArea(t[0])
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
