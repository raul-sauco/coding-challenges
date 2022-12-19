# Zero Sum Subarray
# 🟠 Medium
#
# https://www.algoexpert.io/questions/zero-sum-subarray
#
# Tags: Array

import timeit
from typing import List


# For the array to contain a zero sum subarray, it either needs to sum
# zero, contain a zero, or have two indexes i, j on which the sum of
# values 0..i, 0..j are equal. We can iterate over the array computing
# accumulated sums up to that point, using a hash set to store them, if
# we ever see a sum that we have seen already, we can return True.
#
# Time complexity: O(n) - We iterate over the array once.
# Space complexity: O(n) - The set can grow to the size of the input.
class Solution:
    def zeroSumSubarray(self, nums: List[int]) -> bool:
        total, sums = 0, set([0])
        for num in nums:
            total += num
            if num == 0 or total in sums:
                return True
            sums.add(total)
        return False


def test():
    executors = [Solution]
    tests = [
        [[], False],
        [[1], False],
        [[-2, 2], True],
        [[-2, 4, 0], True],
        [[-2, 2, 2, -2], True],
        [[-5, -5, 2, 3, -2], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.zeroSumSubarray(t[0])
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
