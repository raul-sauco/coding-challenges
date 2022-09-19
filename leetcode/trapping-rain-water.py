# 42. Trapping Rain Water
# 🔴 Hard
#
# https://leetcode.com/problems/trapping-rain-water/
#
# Tags: Array - Two Pointers - Dynamic Programming - Stack - Monotonic Stack

import timeit
from typing import List

# 1e4 calls
# » TwoPointers         0.04256   seconds
# » MonotonicStack      0.08529   seconds

# If we get to the realization that the maximum height collected between
# two values will be determined by the lower of the two heights,
# independently of the value of the higher one, we can come up with a
# greedy O(n) solution to this problem. We use both a pointer and a
# max_height variable from each end. At each step, we update the pointer
# that is on the side of the lower of the two max heights, that
# guarantees that we know the amount of water that can be held at that
# particular point. If the inner heights from that point are smaller,
# then the two current max will determine the height of the water, if
# we find a taller height, then, we still know that the max at the
# current position is equal to the closer maximum because that one would
# be one of the extremities of this "tank" and would mark the water
# height independent of how much taller the other side is.
#
# Time complexity: O(n) - We visit each position of the list once.
# Space complexity: O(1) - We use 5 variables independently of the size
# of the input.
#
# Runtime: 120 ms, faster than 97.96%
# Memory Usage: 16 MB, less than 81.24%
class TwoPointers:
    def trap(self, height: List[int]) -> int:
        # Initialize two pointers to the ends of the array.
        left_idx, right_idx = 0, len(height) - 1
        # Initialize the current maximum height seen on both the left
        # and right hand side of the array.
        trapped, max_left, max_right = 0, height[0], height[-1]
        # Keep iterating while the pointers are not next to each other.
        while right_idx > left_idx + 1:
            # Move the pointer that is on the side of the lower max
            # height, if they are both the same, it does not matter
            # which pointer we update.
            if max_left >= max_right:
                # The left max is higher, update the right pointer.
                right_idx -= 1
                # If the new height is taller than the current max right
                # then we cannot collect any water at this point and
                # we want to update the max to be this new height.
                if height[right_idx] > max_right:
                    max_right = height[right_idx]
                # Else, if the new height is lower than the current max
                # right, we know that we will be able to collect water
                # there, one unit wide and the difference between the
                # current height and the water level in height.
                elif height[right_idx] < max_right:
                    trapped += max_right - height[right_idx]
                # We ignore the case when the max height and the current
                # height are the same, we cannot either collect water
                # or update the max value.
            else:
                # The right max is higher, update the left pointer.
                left_idx += 1
                # If the new height is taller than the current max left
                # then we cannot collect any water at this point and
                # we want to update the max to be this new height.
                if height[left_idx] > max_left:
                    max_left = height[left_idx]
                # Else, if the new height is lower than the current max
                # left, we know that we will be able to collect water
                # there, one unit wide and the difference between the
                # current height and the water level in height.
                elif height[left_idx] < max_left:
                    trapped += max_left - height[left_idx]
                # We ignore the case when the max height and the current
                # height are the same, we cannot either collect water
                # or update the max value.
        # Return the amount of trapped water.
        return trapped


# Use a monotonic stack to keep the index of heights that we have seen
# from the latest max height on, iterate over all the heights starting
# on the left, by popping any height smaller than the current from the
# stack and calculating the amount of water trapped for that height,
# we can move on with the calculations, if later we find an area
# comprised between two higher heights, we add that "top" portion of
# trapped water to the result.
#
# Time complexity: O(n) - We visit each height a maximum of two times,
# on the main loop and later if we pop it from the stack.
# Space complexity: O(n) - The stack may grow to the same size as the
# input.
#
# Runtime: 133 ms, faster than 81.46%
# Memory Usage: 15.8 MB, less than 77.48%
class MonotonicStack:
    def trap(self, height: List[int]) -> int:
        # Store the amount of trapped water.
        trapped = 0
        # The monotonic stack with the indices of the latest tall
        # heights seen, in non-increasing order.
        stack = []
        # Iterate over all the heights from left to right.
        for i, h in enumerate(height):
            # While the current height is taller than the last and
            # smallest height in the stack, pop it and check if any
            # water is being trapped between the previous height and the
            # current one.
            while stack and h > height[stack[-1]]:
                # The last height in the stack is smaller than the
                # current one, pop it and use it as the "column" on top
                # of which the collected water sits.
                column = stack.pop()
                # If we still have any heights in the stack after the
                # last pop, we have a "column" check the amount of
                # water trapped on top of that column.
                if stack:
                    # The width of the trapped portion goes from the
                    # index of the height that we are visiting to the
                    # height that is trapping the water on the left,
                    # i.e. left = 1, right = 3 => w = 3-1-1 => 1
                    trapped_width = i - stack[-1] - 1
                    # The height of the trapped area equals the
                    # difference from the top of the "column" below the
                    # trapped water to the point at which the water
                    # would start to flow out, which is the smallest of
                    # the left and right height. This greedy approach
                    # works because if there was a higher height, we
                    # would add that unprocessed area in a later step.
                    trapped_height = min(h, height[stack[-1]]) - height[column]
                    # The amount of trapped water on that section equals
                    # the area with the computed width and height.
                    trapped += trapped_height * trapped_width
            # Append this height to the stack, any smaller heights have
            # been popped already.
            stack.append(i)
        # Return the amount of trapped water.
        return trapped


def test():
    executors = [
        TwoPointers,
        MonotonicStack,
    ]
    tests = [
        [[4, 2, 0, 3, 2, 5], 9],
        [[1, 1, 1, 1, 1, 1], 0],
        [[6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1], 0],
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
        [[6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 7], 40],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.trap(t[0])
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
