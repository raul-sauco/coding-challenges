# 496. Next Greater Element I
# 🟢 Easy
#
# https://leetcode.com/problems/next-greater-element-i/
#
# Tags: Array - Hash Table - Stack - Monotonic Stack

import timeit
from typing import List


# Iterate over nums2 in reverse keeping track of the largest values that
# we have seen using a monotonic stack. For each value, we pop any
# smaller values of the stack then append it. We also use a hashmap to
# record which is the first greater element that we have seen after the
# current one, which will be the top of the stack. Once we have visited
# all elements of nums2, we iterate over nums1 using the dictionary to
# get the next greater value.
#
# Time complexity: O(n) - We visit once each element in both arrays.
# Each element also may get pushed and popped from the stack once.
# Space complexity: O(n) - The dictionary will grow to the same size as
# nums2, the stack may as well grow to that size.
#
# Runtime: 98 ms, faster than 62.24%
# Memory Usage: 14.2 MB, less than 56.75%
class Solution:
    def nextGreaterElement(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        # A dictionary of val: next greater found in nums2.
        next_greater = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            val = nums2[i]
            while stack and stack[-1] < val:
                stack.pop()
            next_greater[val] = stack[-1] if stack else -1
            stack.append(val)
        return [next_greater[x] for x in nums1]


def test():
    executors = [Solution]
    tests = [
        [[2, 4], [1, 2, 3, 4], [3, -1]],
        [[4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.nextGreaterElement(t[0], t[1])
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
