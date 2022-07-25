# 34. Find First and Last Position of Element in Sorted Array
# 🟠 Medium
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Tags: Array - Binary Search

import timeit
from itertools import takewhile
from typing import List


# Similar to LeetCode 278. First Bad Version, but here we have to find the first and last occurrence of the
# given number, we can do it by running two simultaneous binary searches, one for the start and one for the end.
#
# Time complexity: O(log(n)) - We split the input by half in each iteration.
# Space complexity: O(1) - We only store 6 pointers in memory.
#
# Runtime: 140 ms, faster than 40.86% of Python3 online submissions for Find First and Last Position of Element in
# Sorted Array.
# Memory Usage: 15.4 MB, less than 50.23% of Python3 online submissions for Find First and Last Position of Element
# in Sorted Array.
class BinarySearch:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if not nums:
            return result

        # Four pointers, we are effectively doing two binary searches simultaneously.
        ll, lr, rl, rr = 0, len(nums) - 1, 0, len(nums) - 1
        # Edge case when the start, and/or end of the list match the target.
        if nums[ll] == target:
            result[0] = ll
        if nums[rr] == target:
            result[1] = rr
        while result[0] == -1 or result[1] == -1:
            if result[0] == -1:
                lm = ll + ((lr - ll) // 2)
                if nums[lm] < target:
                    # If the value at index lm on nums is < target. The first value could be to the right, move
                    # the left pointer.
                    ll = lm
                else:
                    # If the value at index lm is equal or greater than the target, the first match could be this
                    # position, or one to the left, move the right pointer.
                    lr = lm

                if lr - ll < 2:
                    # We have run out of positions to check.
                    if nums[lr] == target:
                        result[0] = lr
                    else:
                        # We have failed, return [-1, -1]
                        return result

            if result[1] == -1:
                rm = rl + ((rr - rl) // 2)
                if nums[rm] > target:
                    # If the value at index lm on nums is > target. The last match could be to the left, move
                    # the right pointer.
                    rr = rm
                else:
                    # If the value at index lm is equal or less than the target, the first match could be this
                    # position, or one to the right, move the left pointer.
                    rl = rm

                if rr - rl < 2:
                    # We have run out of positions to check.
                    if nums[rl] == target:
                        result[1] = rl
                    else:
                        # We have failed, return [-1, -1]
                        return result

        return result


# Use List.index() to find the leftmost match, then iterate over the elements, using takewhile, until one of them
# does not match the target, and return that position - 1 as right.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - We use generator functions, no extra memory used.
#
# Runtime: 135 ms, faster than 45.66% of Python3 online submissions for Find First and Last Position of Element
# in Sorted Array.
# Memory Usage: 15.3 MB, less than 93.21% of Python3 online submissions for Find First and Last Position of
# Element in Sorted Array.
class BuiltInFn:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            right = left = nums.index(target)
            for _ in takewhile(lambda idx: nums[idx] == target, range(left, len(nums))):
                right += 1
            return [left, right - 1]
        except ValueError:
            return [-1, -1]


def test():
    executors = [BinarySearch, BuiltInFn]
    tests = [
        [[1], 0, [-1, -1]],
        [[5, 7, 7, 8, 8, 10], 8, [3, 4]],
        [[5, 7, 7, 8, 8, 10], 6, [-1, -1]],
        [[], 0, [-1, -1]],
        [[13], 13, [0, 0]],
        [[13, 13], 13, [0, 1]],
        [[8, 8, 8, 8, 8, 8, 8, 8], 0, [-1, -1]],
        [[8, 8, 8, 8, 8, 8, 8, 8], 8, [0, 7]],
        [[8, 8, 8, 8, 8, 8, 8, 8, 9, 10, 12], 8, [0, 7]],
        [[4, 5, 6, 8, 8, 8, 8, 8, 8, 8, 8, 9, 10, 12], 8, [3, 10]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.searchRange(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
