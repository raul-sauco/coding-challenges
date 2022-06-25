# https://leetcode.com/problems/non-decreasing-array/

import timeit
from typing import List

# The recursive solution is faster on LeetCode but not locally.
#
# Iterative           0.04479   seconds
# Recursive           0.10398   seconds


# Use a recursive call and store in the state if we have already used the one wildcard allowed.
#
# Runtime: 280 ms, faster than 47.35% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 17.1 MB, less than 5.92 % of Python3 online submissions for Non-decreasing Array.


class Recursive:
    def checkPossibility(self, nums: List[int]) -> bool:
        def checkSequence(seq: List[int], w: bool):
            for i in range(len(seq)-1):
                if seq[i+1] < seq[i]:
                    if w:
                        if i == len(nums) - 2:
                            return w
                        if i == 0 or seq[i-1] <= seq[i+1]:
                            # The current number is too big for the sequence
                            return checkSequence(seq[i+1:], False)
                        if seq[i] <= seq[i+2]:
                            # The next number is too small for the sequence
                            seq[i+1] = seq[i]
                            return checkSequence(seq[i+1:], False)
                    return False
            return True
        return checkSequence(nums, True)


# Use a for loop and a boolean to store the one wildcard.
#
# Runtime: 303 ms, faster than 37.80% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 15.3 MB, less than 49.84 % of Python3 online submissions for Non-decreasing Array.
class Iterative:
    def checkPossibility(self, nums: List[int]) -> bool:
        w = True   # One wildcard
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if not w:
                    return False
                w = False
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        return True


def test():
    executor = [
        {'executor': Iterative, 'title': 'Iterative', },
        {'executor': Recursive, 'title': 'Recursive', },
    ]
    tests = [
        [[5, 7, 1, 8], True],
        [[5, 7, 8, 1], True],
        [[3, 4, 2, 3], False],
        [[-1, 4, 2, 3], True],
        [[4], True],
        [[0, -1], True],
        [[4, 2, 3], True],
        [[4, 2, 1], False],
        [[-1000, 1000, -2], True],
        [[-1000, 1000, -2, -3], False],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.checkPossibility([*t[0]])
                expected = t[1]
                assert result == expected, f'{result} != {expected} for {t[0]} using {e["title"]} solution'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
