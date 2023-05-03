# 2215. Find the Difference of Two Arrays
# 🟢 Easy
#
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
#
# Tags: Array - Hash Table

import timeit
from typing import List


# What they are really asking for is a tuple with set set differences of
# a-b and b-a, but in a list format, we can return just that.
#
# Time complexity: O(n) - We iterate all the elements multiple times.
# Space complexity: O(n) - We are creating sets of the same size as the
# input.
#
# Runtime 182 ms Beats 61.53%
# Memory 16.8 MB Beats 9.53%
class Solution:
    def findDifference(
        self, nums1: List[int], nums2: List[int]
    ) -> List[List[int]]:
        a, b = set(nums1), set(nums2)
        return [list(a - b), list(b - a)]


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3, 3], [1, 1, 2, 2], [[3], []]],
        [[1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findDifference(t[0], t[1])
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
