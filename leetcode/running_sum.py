# https://leetcode.com/problems/running-sum-of-1d-array/

import timeit
from typing import List

from helpers import BColors


# Runtime: 95 ms, faster than 6.24% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.1 MB, less than 25.39 % of Python3 online submissions for Running Sum of 1d Array.
class ExtraVariable:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            nums[i] = sum
        return nums


# Runtime: 97 ms, faster than 5.37% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 13.9 MB, less than 92.56 % of Python3 online submissions for Running Sum of 1d Array.
class InPlace:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


def test():
    executor = [
        {'executor': ExtraVariable, 'title': 'ExtraVariable', },
        {'executor': InPlace, 'title': 'InPlace', },
    ]
    tests = [
        [[1, 2, 3, 4], [1, 3, 6, 10]],
        [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5]],
        [[3, 1, 2, 10, 1], [3, 4, 6, 16, 17]],
        [[1, 1, 8, -90, 1], [1, 2, 10, -80, -79]],
        [[], []],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.runningSum([*t[0]])
                expected = t[1]
                assert result == expected, f'{result} != {expected} for {t[0]} using {e["title"]} solution'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m » {result}\033[0m")


test()
