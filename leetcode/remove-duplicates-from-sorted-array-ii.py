# 80. Remove Duplicates from Sorted Array II
# 🟠 Medium
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
#
# Tags: Array - Two Pointers

import timeit
from typing import List


# Remove duplicates leaving one or two instances of every unique value.
# Iterate over the input keeping the count of times we have seen the
# last value, when the count is under one, write the value under the
# read pointer on the position indicated by the write pointer, when we
# have seen the value under the read pointer twice already, move the
# read pointer forward without moving the write pointer.
#
# Time complexity: O(n) - We visit each value in the input once.
# Space complexity: O(1) - We use constant memory.
#
# Runtime: 60 ms, faster than 88.76%
# Memory Usage: 13.8 MB, less than 74.73%
class TwoPointers:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = count = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[w - 1]:
                nums[w], count = nums[r], 1
                w += 1
            elif count < 2:
                count += 1
                nums[w] = nums[r]
                w += 1
        return w


def test():
    executors = [
        TwoPointers,
    ]
    tests = [
        [[1, 1, 1, 2, 2, 3], 5],
        [[0, 0, 1, 1, 1, 1, 2, 3, 3], 7],
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
