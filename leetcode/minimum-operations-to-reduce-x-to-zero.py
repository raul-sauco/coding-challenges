# 1658. Minimum Operations to Reduce X to Zero
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
#
# Tags: Array - Hash Table - Binary Search - Sliding Window - Prefix

import timeit
from typing import List


# Use two pointers to compute the maximum length subarray that has a sum
# equal to the total elements in the array minus x.
#
# Time complexity: O(n) - We visit each element of the array and do
# constant time work for each.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 981 ms Beats 59.41%
# Memory 30.90 MB Beats 35.75%
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        longest, target, left, current_sum = -1, sum(nums) - x, 0, 0
        for right in range(len(nums)):
            current_sum += nums[right]
            if current_sum == target:
                longest = max(longest, 1 + right - left)
            while current_sum >= target and left < len(nums):
                current_sum -= nums[left]
                left += 1
                if current_sum == target:
                    longest = max(longest, 1 + right - left)

        return -1 if longest == -1 else len(nums) - longest


class Naive:
    def minOperations(self, nums: List[int], x: int) -> int:
        res = len(nums) + 1
        left_sum = 0
        calculations = 0
        for end in range(len(nums), 0, -1):
            if end < len(nums):
                # Add the left element value to the sum.
                left_sum += nums[end]
                if left_sum == x:
                    # If the sum of the left elements to this point
                    # matches, we cannot get a better solution later.
                    steps = len(nums) - end
                    res = min(res, steps)
                    break
                if left_sum > x:
                    # If the left sum is already greater than the
                    # number, we can't calculate a solution.
                    break

            # Now calculate sums starting from the right.
            i = 0
            # Start with whatever value we have taken from the right,
            # it will be 0 for the first iteration.
            sum = left_sum
            while i < end and sum < x:
                calculations += 1
                sum += nums[i]
                i += 1
                steps = i + (len(nums) - end)
                # If we have a match, compare the number of steps with
                # the current best.
                if sum == x:
                    res = min(res, steps)
                elif sum > x:
                    break

        return res if res < len(nums) + 1 else -1


def test():
    executors = [
        Solution,
        Naive,
    ]
    tests = [
        [[1], 1, 1],
        [[5], 5, 1],
        [[1], 3, -1],
        [[1, 1, 4, 2, 3], 5, 2],
        [[5, 6, 7, 8, 9], 4, -1],
        [[5, 6, 7, 8, 9], 35, 5],
        [[5, 6, 7, 8, 9], 30, 4],
        [[3, 2, 20, 1, 1, 3], 10, 5],
        [[3, 1, 1, 20, 1, 2, 1, 3], 27, 5],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 16, 15],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minOperations(t[0], t[1])
                exp = t[2]
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
