# 35. Search Insert Position
# 🟢 Easy
#
# https://leetcode.com/problems/search-insert-position/
#
# Tags: Array - Binary Search

import timeit
from typing import List


# A binary search problem with the added challenge that the value may
# or may not exist in the given array, we can use a classic binary
# search algorithm and a conditional in the return, if the value under
# the pointer is equal or greater than the target value, return that
# index, but if the value is lesser than the target, return the next
# index to represent that we need to insert after that position.
#
# Time complexity: O(n*log(n)) - Each iteration reduces the search
# space by half.
# Space complexity: O(1) - Constant extra memory is used.
#
# Runtime 47 ms Beats 88.69%
# Memory 14.7 MB Beats 73.66%
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2  # l +  (r-l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l if nums[l] >= target else l + 1


def test():
    executors = [Solution]
    tests = [
        [[4], 3, 0],
        [[4], 5, 1],
        [[-1], -1, 0],
        [[1, 3, 5, 6], 5, 2],
        [[1, 3, 5, 6], 2, 1],
        [[1, 3, 5, 6], 7, 4],
        [[2, 3, 5, 6], 1, 0],
        [[-10, -3, 5, 8], 7, 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.searchInsert(t[0], t[1])
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
