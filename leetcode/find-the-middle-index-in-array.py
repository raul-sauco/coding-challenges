# https://leetcode.com/problems/find-the-middle-index-in-array/

# Note: This question is the same as
# 724: https://leetcode.com/problems/find-pivot-index/

import timeit
from typing import List

# Runtime: 78 ms, faster than 19.67% of Python3 online submissions for Find the Middle Index in Array.
# Memory Usage: 13.9 MB, less than 58.31 % of Python3 online submissions for Find the Middle Index in Array.


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        for i, n in enumerate(nums):
            right -= n
            if right == left:
                return i
            left += n
        return -1


def test():
    executor = [
        {'executor': Solution, 'title': 'Solution', },
    ]
    tests = [
        [[1, 7, 3, 6, 5, 6], 3],
        [[1, 2, 3], -1],
        [[2, 1, -1], 0],
        [[2, 3, -1, 8, 4], 3],
        [[1, -1, 4], 2],
        [[2, 5], -1],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.findMiddleIndex([*t[0]])
                expected = t[1]
                assert result == expected, f'{result} != {expected} for {t[0]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
