# 33. Search in Rotated Sorted Array
# 🟠 Medium
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# Tags: Array - Binary Search

import timeit
from typing import List


# First check if the array is actually rotated, if rotated, use Binary
# search to find the point at which the array is rotated, check which
# section could contain the target, then binary search that section.
#
# Time complexity: O(log(n)) - 2 binary searches with O(log(n)) each.
# Space complexity: O(1)
#
# Runtime: 70 ms, faster than 41.42%
# Memory Usage: 14.3 MB, less than 56.29%
class FindPivot:
    def search(self, nums: List[int], target: int) -> int:
        # For small inputs, do linear search.
        if len(nums) < 10:
            for i, num in enumerate(nums):
                if num == target:
                    return i
            return -1
        # If the array is rotated
        if nums[0] > nums[-1]:
            # Search the index of the last element before the rotated
            # elements.
            left, right = 0, len(nums) - 1
            while right > left + 1:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < nums[0]:
                    right = mid - 1
                else:
                    left = mid
            # The first element of the original array is to the right
            # of left/right, check wether the target could be in the
            # head or the tail and set the boundaries for the binary
            # search.
            if target < nums[0]:
                left, right = right + 1, len(nums) - 1
            elif target > nums[0]:
                left, right = 0, right
            else:
                return 0 if nums[0] == target else -1
        # The array is not rotated, do binary search on nums.
        else:
            left, right = 0, len(nums) - 1

        # Binary search the section of the array that could contain the
        # target.
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1


# Do binary search on the rotated array but consider the value of idx 0
# when considering how to update the pointers.
#
# Time complexity: O(log(n)) - We are doing binary search directly on
# the input.
# Space complexity: O(1)
#
# Runtime: 81 ms, faster than 19.64%
# Memory Usage: 14.1 MB, less than 91.15%
class CheckSection:
    def search(self, nums: List[int], target: int) -> int:
        # No edge cases to consider if we check left <= right.
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # Check if mid is target.
            if nums[mid] == target:
                return mid

            # If the section between left and mid does not overlap the
            # intersection of the array.
            if nums[left] <= nums[mid]:
                # Take care of the case where the intersection could be
                # to the right of mid.
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # The intersection is not between left and mid, it could be
            # to the left of left or to the right of mid.
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


def test():
    executors = [
        FindPivot,
        CheckSection,
    ]
    tests = [
        [[3, 1], 0, -1],
        [[3, 1], 1, 1],
        [[4, 5, 6, 7, 0, 1, 2], 6, 2],
        [[40, 50, 60, 70, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 4],
        [[40, 50, 60, 70, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 11],
        [[40, 50, 60, 70, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 13],
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0],
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3],
        [[4, 5, 6, 7, 0, 1, 2], 0, 4],
        [[4, 5, 6, 7, 0, 1, 2], 3, -1],
        [[1], 0, -1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.search(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
