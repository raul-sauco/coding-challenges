# 15. 3Sum
# 🟠 Medium
#
# https://leetcode.com/problems/3sum/
#
# Tags: Array - Two Pointers - Sorting

import timeit
from typing import List


# We can sort the input to start. If we fix the left-most element i and
# use a two-pointer approach to increase or decrease the sum of three
# elements that contains i, we can find the sum of three elements that
# contains i and equals 0, if any, in O(n) time.
#
# Time complexity: O(n^2) - We iterate over every element of the input
# and search the 3sum that contains it in O(n).
# Space complexity: O(1) - If we don't consider the input or output.
#
# Runtime: 976 ms, faster than 76.71%
# Memory Usage: 17.3 MB, less than 91.68%
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input. O(n*log(n)).
        nums.sort()
        # The problem requires that there are no duplicates, the easiest
        # way to guarantee this is to use a set of triplet tuples.
        result = set()
        # Iterate over the input.
        for i in range(len(nums) - 2):
            # Once the value under i is positive, we will not be able to
            # get the 3 sum because the values to the right are all
            # greater or equal.
            if nums[i] > 0:
                break
            # Do not recalculate sums with the same i value.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Fix the element at i and use two pointers to search the
            # 3 sum that equals 0.
            # Initialize the pointers at the maximum possible window.
            left, right = i + 1, len(nums) - 1
            # Adjust while we haven't run out of elements.
            while left < right:
                # Create a tuple with the values currently under the
                # three pointers.
                current = (nums[i], nums[left], nums[right])
                # Compute the current sum of the 3 values.
                sum3 = sum(current)
                if sum3 == 0:
                    # Add to the result set.
                    result.add(current)
                    # Adjust both pointers.
                    left += 1
                    right -= 1
                elif sum3 < 0:
                    # We have to increase the 3sum.
                    left += 1
                else:
                    # We need to decrease the 3sum.
                    right -= 1
        # Return the results.
        return result


def test():
    executors = [Solution]
    tests = [
        # The problem description shows a list of lists, but it accepts
        # a set of tuples.
        [[-1, 0, 1, 2, -1, -4], {(-1, -1, 2), (-1, 0, 1)}],
        [[0, 1, 1], set()],
        [[0, 0, 0], {(0, 0, 0)}],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.threeSum(t[0])
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
