# 153. Find Minimum in Rotated Sorted Array
# 🟠 Medium
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Tags: Array - Binary Search

import timeit
from typing import List


# A naive solution would iterate over all the input and return the
# minimum found.
#
# Time complexity: O(n)
# Space complexity: O(1)
#
# Surprisingly, this passes the tests.
# Runtime: 96 ms, faster than 5.38%
# Memory Usage: 14.3 MB, less than 23.54%
class Naive:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


# If we had a sorted array, the answer would be to trivially return the
# leftmost element. Since the array is rotated, we have a point in the
# array, it could be 0, where we could split the array into two sorted
# arrays, if we find that point, the minimum will be the leftmost
# element of the right section. We can improve on the previous solution
# using binary search to find that point.
#
# Time complexity: O(log(n)) - Each iteration we eliminate half of the
# remaining elements.
# Space complexity: O(1) - We only use pointers. Constant space.
#
# Runtime: 48 ms, faster than 84.63%
# Memory Usage: 14 MB, less than 96.01%
class BinarySearch:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            # If the entire section we are looking at is sorted, the
            # minimum is the leftmost element.
            if nums[l] < nums[r]:
                return nums[l]
            # Otherwise, look at the middle element.
            mid = (r + l) // 2
            # Mid is in the rotated portion of the array move the right
            # pointer.
            if nums[mid] < nums[l]:
                r = mid
            # Mid is in the non rotated section of the array.
            else:
                l = mid
        # If we have only two elements left, return the min.
        return min(nums[l], nums[r])


def test():
    executors = [
        Naive,
        BinarySearch,
    ]
    tests = [
        [[4], 4],
        [[4, 5], 4],
        [[1, 2, 3, 4, 5], 1],
        [[6, 7, 8, 1, 2, 3, 4, 5], 1],
        [[3, 4, 5, 1, 2], 1],
        [[4, 5, 6, 7, 0, 1, 2], 0],
        [[11, 13, 15, 17], 11],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findMin(t[0])
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
