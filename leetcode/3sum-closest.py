# 16. 3Sum Closest
# 🟠 Medium
#
# https://leetcode.com/problems/3sum-closest/
#
# Tags: Array - Two Pointers - Sorting

import timeit
from typing import List


# Sort the input, fix one element starting from the left and use
# two pointers encircling the remaining window to calculate possible
# sums. When the current sum is bigger than target, shrink the window
# from the right, when smaller, shrink it from the left, this allows us
# to find the best 3sum with each element in O(n).
#
# Time complexity: O(n^2) - For each element, we find the best 3sum that
# contains it in linear time.
# Space complexity: O(1) - We keep one sum and 3 pointers in memory.
#
# Runtime: 7216 ms, faster than 40.63%
# Memory Usage: 14 MB, less than 88.54%
class LoopAndTwoPointers:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # If we only have 3 elements, return the input.
        if len(nums) < 4:
            return sum(nums)
        # Sort the input to be able to use a two pointer approach.
        nums.sort()
        # We are guaranteed to have at least 3 elements.
        closest = sum(nums[:3])
        # The outer loop iterates over all the values except the last
        # two, these are covered by the left and right pointer.
        for idx in range(len(nums) - 2):
            # Use a left and right pointer to calculate possible 3 sums.
            # Initialize the pointers to the biggest possible window.
            left, right = idx + 1, len(nums) - 1
            # Check sums while we haven't checked them all.
            while left < right:
                current = nums[idx] + nums[right] + nums[left]
                # If the current sum is greater than the target, find a
                # smaller sum by moving left the right pointer.
                if current > target:
                    right -= 1
                # If the current sum is less than the target, find a
                # larger sum by moving right the left pointer.
                elif current < target:
                    left += 1
                # If the target equals the sum, return the values, this
                # is the only match.
                else:
                    return current
                # Check all possible sums against the best.
                if abs(current - target) < abs(closest - target):
                    closest = current

        return closest


# We can extend the previous solution to come up with a generic
# solution that finds the sum of k elements that comes closer to target.
#
# Time complexity: O(n^2) - For each element, we find the best 3sum that
# contains it in linear time.
# Space complexity: O(n) - We keep the reversed input and use list
# comprehension to calculate the result, linear space.
class KSum:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.kSumClosest(nums, target, 3)

    def kSumClosest(self, nums: List[int], target: int, k: int) -> int:
        n = len(nums)
        if k == n:
            return sum(nums[:k])

        current = sum(nums[:k])
        if current >= target:
            return current

        current = sum(nums[-k:])
        if current <= target:
            return current

        if k == 1:
            return min(
                [(x, abs(target - x)) for x in nums],
                key=lambda tuple: tuple[1],
            )[0]

        closest = sum(nums[:k])
        for i in range(n - k + 1):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            current = (
                self.kSumClosest(nums[i + 1 :], target - nums[i], k - 1)
                + nums[i]
            )
            if abs(target - current) < abs(target - closest):
                if current != target:
                    closest = current
                else:
                    return target

        return closest


def test():
    executors = [
        LoopAndTwoPointers,
        KSum,
    ]
    tests = [
        [[-1, 2, 1, -4], 1, 2],
        [[0, 0, 0], 1, 0],
        [[1, 1, 1, 1], 0, 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.threeSumClosest(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
