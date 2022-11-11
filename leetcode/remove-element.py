# 27. Remove Element
# 🟢 Easy
#
# https://leetcode.com/problems/remove-element/
#
# Tags: Array - Two Pointers

import timeit
from typing import List


# Modify the input in place to remove any occurrence of val, return
# number of remaining values and place them at the start of the input
# array. Use a read pointer to read all the values, use a left write
# pointer to write any value that does not match the input element.
#
# Time complexity: O(n) - We visit each array position twice.
# Space complexity: O(1) - Only two pointers are kept in memory.
#
# Runtime: 67 ms, faster than 39.29%
# Memory Usage: 13.8 MB, less than 62.90%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        w = 0
        for num in nums:
            if num != val:
                nums[w] = num
                w += 1
        for i in range(w, len(nums)):
            nums[i] = None
        return w


def test():
    _ = None
    executors = [Solution]
    tests = [
        [[3, 2, 2, 3], 2, [3, 3, _, _], 2],
        [[0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4, _, _, _], 5],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.removeElement(t[0], t[1])
                exp = t[3]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
                assert t[0] == t[2], (
                    f"\033[93m» {t[0]} <> {t[2]}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
