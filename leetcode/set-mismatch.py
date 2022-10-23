# 645. Set Mismatch
# 🟢 Easy
#
# https://leetcode.com/problems/set-mismatch/
#
# Tags: Array - Hash Table - Bit Manipulation - Sorting

import timeit
from typing import List

# 1e4 calls
# » Math                0.01733   seconds
# » UseSet              0.02906   seconds
# » InPlaceMark         0.04286   seconds

# We can use a set of the expected numbers, then iterate over the input
# removing the values we encounter from the set, if we find a value that
# is not in the set, is because we have removed it already, and that is
# the duplicated value, the value we have left in the set after we
# iterate over the entire input is the missing value.
#
# Time complexity: O(n) - We iterate over the input once.
# Space complexity: O(n) - The set is the same size as the input.
#
# Runtime: 633 ms, faster than 13.77%
# Memory Usage: 15.9 MB, less than 23.96%
class UseSet:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated = None
        # Create a set with all numbers we are expecting to see.
        expected = {i for i in range(1, len(nums) + 1)}
        for num in nums:
            if num in expected:
                expected.remove(num)
            else:
                repeated = num
        return [repeated, expected.pop()]


# Avoid using extra space using the values found as indexes and updating
# the values at that index to be negative. When we find a value that is
# already negative, that is the duplicate value. Iterate once more over
# the input to find the index of the only value that is positive, that
# is the missing value.
#
# Time complexity: O(n) - We iterate twice over the input.
# Space complexity: O(1) - Only constant space used.
#
# Runtime: 286 ms, faster than 75.93%
# Memory Usage: 15.3 MB, less than 84.98%
class InPlaceMark:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated, missing = None, None
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                repeated = num
            else:
                nums[num - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break
        return [repeated, missing]


# We can also compute the result using several properties of the integer
# series 1..n
# https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_⋯
#
# Time complexity; O(n) - We still iterate over all the values twice.
# Space complexity: O(n) - We still use a set of size n.
#
# Runtime: 458 ms, faster than 46.36%
# Memory Usage: 16 MB, less than 14.59%
class Math:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # This value represents what the sum should be for the set, the
        # missing number will be the difference between the sum of
        # unique values that we have and this sum.
        sum_1_to_n = len(nums) * (len(nums) + 1) // 2
        # The sum of unique values in the input.
        sum_unique = sum(set(nums))
        # The sum of actual values in the input, the duplicate number
        # will be the difference between this value and the sum of
        # unique values.
        sum_input = sum(nums)
        return [sum_input - sum_unique, sum_1_to_n - sum_unique]


def test():
    executors = [
        Math,
        UseSet,
        InPlaceMark,
    ]
    tests = [
        [[1, 1], [1, 2]],
        [[2, 2], [2, 1]],
        [[1, 2, 2, 4], [2, 3]],
        [
            [13, 10, 3, 8, 5, 6, 7, 17, 9, 1, 4, 12, 9, 14, 15, 16, 2, 18],
            [9, 11],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                # Make a copy, the in-place solution mutates the array.
                result = sol.findErrorNums(t[0].copy())
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
