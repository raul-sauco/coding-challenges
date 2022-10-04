# 268. Missing Number
# 🟢 Easy
#
# https://leetcode.com/problems/missing-number/
#
# Tags: Array - Hash Table - Math - Binary Search - Bit Manipulation
# - Sorting

import timeit
from typing import List

# 10e5 calls
# » Set                 0.01628   seconds
# » O1WithIndexes       0.01233   seconds


# Create a set that contains all the values that should be in the range,
# then iterate over the input removing values we see from the set, the
# only remaining value will be the missing value. This is the easy
# naive solution that I would suggest first in an interview.
#
# Time complexity: O(n) - To iterate over the elements.
# Space complexity: O(n) - For the set.
#
# Runtime: 376 ms, faster than 19.67%
# Memory Usage: 15.9 MB, less than 6.62%
class Set:
    def missingNumber(self, nums: List[int]) -> int:
        s = {i for i in range(len(nums) + 1)}
        for num in nums:
            s.remove(num)
        return s.pop()


# Iterate over the input adding index values and subtracting input
# values to and from a result. Once we add/subtract all values, the
# result == missing number.
#
# Time complexity: O(n)
# Space complexity: O(1)
#
# Runtime: 139 ms, faster than 94.32%
# Memory Usage: 15.1 MB, less than 98.59%
class O1WithIndexes:
    def missingNumber(self, nums: List[int]) -> int:
        # There is one less element than value, the missing element.
        res = len(nums)
        # Iterate over the numbers from 0 to the length of the list, add
        # the index and subtract the value of nums at that index.
        for i in range(len(nums)):
            # Add the value of the index, subtract the value of the
            # element at i.
            res += i - nums[i]
        # The sum of indexes minus values is equal to the missing value.
        return res


def test():
    executors = [
        Set,
        O1WithIndexes,
    ]
    tests = [
        [[1], 0],
        [[3, 0, 1], 2],
        [[0, 1], 2],
        [[9, 6, 4, 2, 3, 5, 7, 0, 1], 8],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.missingNumber(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
