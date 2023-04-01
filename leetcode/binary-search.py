# 704. Binary Search
# 🟢 Easy
#
# https://leetcode.com/problems/binary-search/
#
# Tags: Array - Binary Search


import timeit
from typing import List

# The iterative solution is the most efficient on LeetCode, using the
# built-in method index is the most efficient locally.
#
# BuiltIn             0.01493   seconds
# Iterative           0.02365   seconds
# Recursive           0.04586   seconds


# Use a left and right pointer, at each iteration compute the mid-point
# between them, when the value at that mid index is greater than the
# target, we know that the target will be to the left if it found in the
# array, when the value is lesser, it will be found to the right.
#
# Time complexity: O(log(n)) - Each iteration discards half of the
# search space.
# Space complexity: O(1) - We use constant space.
#
# Runtime 235 ms Beats 94.42%
# Memory 15.4 MB Beats 96.81%
class Iterative:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1


# Use the built-in index method wrapped in a try-catch block, if the
# method does not find the target, it will throw an exception, catch it
# and return -1.
#
# Time complexity: O(log(n)) - Each iteration discards half of the
# search space.
# Space complexity: O(1) - We use constant space.
#
# Runtime: 343 ms Beats 49.28%
# Memory 15.5 MB Beats 71.46%
class BuiltIn:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except (Exception):
            return -1


# Use a recursive call to implement binary search.
#
# Time complexity: O(log(n)) - Each iteration discards half of the
# search space.
# Space complexity: O(log(n)) - The height of the call stack will grow
# by one with each call to the recursive method.
#
# Runtime 355 ms Beats 45.00%
# Memory 22.9 MB Beats 21.93%
class Recursive:
    def search(self, nums: List[int], target: int) -> int:
        def s(lo: int, hi: int) -> int:
            if lo > hi:
                return -1
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return s(mid + 1, hi)
            if nums[mid] > target:
                return s(lo, mid - 1)
            return -1

        return s(0, len(nums) - 1)


def test():
    executors = [
        Iterative,
        BuiltIn,
        Recursive,
    ]
    tests = [
        [[5], 5, 0],
        [[-4, -2, 0, 1], 2, -1],
        [[-1, 0, 3, 5, 9, 12], 9, 4],
        [[-1, 0, 3, 5, 9, 12], 2, -1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.search(t[0], t[1])
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
