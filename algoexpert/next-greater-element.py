# Next Greater Element
# 🟠 Medium
#
# https://www.algoexpert.io/questions/next-greater-element
#
# Tags: Array - Stack - Monotonic Stack

import timeit
from typing import List


# Find the index of the greatest element, from that index, visit all
# elements in the circular array from right to left computing their next
# greater element.
#
# Time complexity: O(n) - We visit each element twice.
# Space complexity: O(n) - The monotonic stack could grow to the same
# size as the input.
class Solution:
    def nextGreaterElement(self, array: List[int]) -> List[int]:
        if not array:
            return []
        # Find the index of the greatest element furthest right.
        max_idx = 0
        for i in range(1, len(array)):
            if array[i] >= array[max_idx]:
                max_idx = i
        stack, res = [], [None] * len(array)
        # Visit all elements right to left.
        for i in range(max_idx, max_idx - len(array) - 1, -1):
            # Preserve the strictly decreasing stack tone.
            while stack and stack[-1] <= array[i]:
                stack.pop()
            # The top of the stack is the next greater element.
            res[i] = -1 if not stack else stack[-1]
            # The current element is now the smallest element from the
            # left.
            stack.append(array[i])
        return res


def test():
    executors = [Solution]
    tests = [
        [[], []],
        [[3], [-1]],
        [[3, 1], [-1, 3]],
        [[6, 4, 5, 7, 2, 1, 3], [7, 5, 7, -1, 3, 3, 6]],
        [[2, 5, -3, -4, 6, 7, 2], [5, 6, 6, 6, 7, -1, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.nextGreaterElement(t[0])
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
