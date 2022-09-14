# 26. Remove Duplicates from Sorted Array
# 🟢 Easy
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Tags: Array - Two Pointers

import timeit
from typing import List


# Use a read and write pointers, read each value and, when the values
# are unique, write them to the corresponding position.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - Constant space, if we don't consider input
# and output arrays.
class NonMutating:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Use two pointers, one to read and one to write.
        w = r = 0
        # Initialize a variable that registers the last number processed.
        last = float("-inf")
        while r < len(nums):
            # If this is the first occurrence of a number, we want to
            # save it to the result array.
            if nums[r] != last:
                # Mark this value as the last seen.
                last = nums[r]
                # Write the value to its position and update the
                # write pointer.
                nums[w] = nums[r]
                w += 1
            # Always update the write pointer.
            r += 1
        # Overwrite the rest of the values with None.
        for idx in range(w, len(nums)):
            nums[idx] = None
        return nums


# This solution is modified to work in the LeetCode tests, they ask for
# the array to be modified in place, and the last values can be
# anything, we do not need to set them to None.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - Constant space.
#
# Runtime: 154 ms, faster than 50.33%
# Memory Usage: 15.5 MB, less than 65.27%
#
# NOTE: This solution does not work locally, it is modified to work with
# the LeetCode tests, it modifies the input in place and returns the
# number of unique elements.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Use two pointers, one is the implicit read pointer of the
        # for loop, other is the explicit write pointer initialized to 0.
        w = 0
        # Initialize a variable that registers the last number processed.
        last = float("-inf")
        for val in nums:
            # If this is the first occurrence of a number, we want to
            # save it to the result array.
            if val != last:
                # Mark this value as the last seen.
                last = val
                # Write the value to its position and update the
                # write pointer.
                nums[w] = val
                w += 1
        return w


def test():
    executors = [NonMutating]
    tests = [
        [[1, 1, 2], [1, 2, None]],
        [
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            [0, 1, 2, 3, 4, None, None, None, None, None],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.removeDuplicates(t[0])
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
