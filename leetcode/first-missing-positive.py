# 41. First Missing Positive
# 🔴 Hard
#
# https://leetcode.com/problems/first-missing-positive/
#
# Tags: Array - Hash Table

import timeit
from typing import List


# Use the pigeon hole principle with the array positions as the holes.
# We visit each position on the array, if we find a positive integer
# that would fit a "hole", that is, one of the array positions between
# 0 and len(arr), we swap it with the value there, we keep doing this
# until the current index has a value that does not belong in any of
# the holes, or the destination hole already has its correct value, then
# we move to the next hole. Once we iterate over the entire array, we
# know that holes that have their corresponding value in the array will
# be filled with the correct value, we iterate over the array from the
# start, the index of the first hole that contains the wrong pigeon is
# the first missing positive.
#
# Time complexity: O(n) - Since on each operation we are placing, at
# least, one of the values in its correct pigeon hole, we will do that
# operation at most n-1 times, then we will skip these correct positions
# in the outer loop, even with the nested for-while loop on the first
# pass, the complexity remains O(n)
# Space complexity: O(1) - Constant space.
#
# Runtime: 770 ms, faster than 40.67%
# Memory Usage: 27.2 MB, less than 82.84%
class PigeonHoling:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Place values i in the 1..len(nums)-1 at the nums[i-1]
        # index, ignore other values.
        for i in range(len(nums)):
            # Keep swapping the value while this position has a value
            # that could be placed in a hole. Skip if the hole already
            while (
                nums[i] > 0
                and nums[i] <= len(nums)
                and nums[i] != i + 1
                and nums[i] != nums[nums[i] - 1]
            ):
                # Store the destination index in a variable.
                dest_idx = nums[i] - 1
                # Swap this value with the value at nums[nums[i]-1]
                nums[i], nums[dest_idx] = nums[dest_idx], nums[i]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        # Iterate over the modified array to find the first missing positive.
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                break
            i += 1
        return i + 1


def test():
    executors = [PigeonHoling]
    tests = [
        [[1, 1], 2],
        [[1, 2, 0], 3],
        [[3, 4, -1, 1], 2],
        [[7, 8, 9, 11, 12], 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.firstMissingPositive(t[0])
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
