# https://leetcode.com/problems/binary-search/


import timeit
from typing import List

# The loop solution is the most efficient on LeetCode.
# Using the built-in method index is the most efficient locally.
#
# Index               0.01493   seconds
# Loop                0.02365   seconds
# Recursive           0.04586   seconds


# Use a loop to do binary search.
#
# Runtime: 249 ms, faster than 94.42% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 71.46 % of Python3 online submissions for Binary Search.
class Loop:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid-1
            if nums[mid] < target:
                start = mid+1
        return -1


# Use the built-in index method
#
#

# Use the built-in index method.
#
# Runtime: 343 ms, faster than 49.28% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 71.46 % of Python3 online submissions for Binary Search.


class Index:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except (Exception):
            return -1


# Use a recursive call to implement binary search.
#
# Runtime: 355 ms, faster than 45.00% of Python3 online submissions for Binary Search.
# Memory Usage: 22.9 MB, less than 21.93 % of Python3 online submissions for Binary Search.
class Recursive:
    def search(self, nums: List[int], target: int) -> int:
        def s(start: int, end: int) -> int:
            if start > end:
                return -1
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return s(mid+1, end)
            if nums[mid] > target:
                return s(start, mid-1)
            return -1
        return s(0, len(nums)-1)


def test():
    executor = [
        {'executor': Index, 'title': 'Index', },
        {'executor': Loop, 'title': 'Loop', },
        {'executor': Recursive, 'title': 'Recursive', },
    ]
    tests = [
        [[], 2, -1],
        [[5], 5, 0],
        [[-4, -2, 0, 1], 2, -1],
        [[-1, 0, 3, 5, 9, 12], 9, 4],
        [[-1, 0, 3, 5, 9, 12], 2, -1],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.search([*t[0]], t[1])
                expected = t[2]
                assert result == expected, f'{result} != {expected} for {t[0]}:{t[1]} using {e["title"]} solution'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
