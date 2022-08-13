# 152. Maximum Product Subarray
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-product-subarray/
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List


# The brute force solution computes the product of all possible
# subarrays and returns the maximum found.
#
# Time complexity: O(n^2)
# Space complexity: O(1)
#
# This solution would probably fail with Time Limit Exceeded.
class BruteForce:
    def maxProduct(self, nums: List[int]) -> int:
        # We are guaranteed to have one element.
        max_found = nums[0]
        for i in range(len(nums)):
            prod = nums[i]
            for j in range(i + 1, len(nums)):
                prod *= nums[j]
                if prod > max_found:
                    max_found = prod
        return max_found


# The maximum product for an array containing either only positive
# integers, or an even number of negative integers, would be the entire
# array. If there are an uneven number of negative values, we have to
# find the maximum product to either the right or left of one of them.
# The special cases we have to take into account are:
#
# - A zero value, we can decide to take:
#   - The subarray to the left.
#   - The subarray to the right.
#   - The zero itself.
#
# - An uneven number of negative values, have to discard:
#   - The subarray left of the first negative value including it.
#   - The subarray right of the last negative value including it.
#
# We can calculate the prefix and suffix products and take the maximum
# between them. We need to take care of resetting the current product
# to a neutral value when we find a 0.
#
# Time complexity: O(n) - We visit each element twice.
# Space complexity: O(1) - We only store three variables.
#
# Runtime: 148 ms, faster than 35.59%
# Memory Usage: 14.4 MB, less than 79.17%
class PrefixSuffix:
    def maxProduct(self, nums: List[int]) -> int:
        best = float("-inf")
        prefix_prod = suffix_prod = 0
        # Iterate over the input to get the prefix sum.
        for i in range(len(nums)):
            if not prefix_prod:
                prefix_prod = nums[i]
            else:
                prefix_prod *= nums[i]
            if not suffix_prod:
                suffix_prod = nums[-i - 1]
            else:
                suffix_prod *= nums[-i - 1]
            best = max(best, prefix_prod, suffix_prod)
        return best


# We can use the same logic as in the previous solution but using extra
# memory to keep a reversed copy of the input array. We iterate
# over the elements of both and sum their values before getting the
# maximum of the sum.
#
# Time complexity: O(n)
# Space complexity: O(n) - The reversed array.
#
# Runtime: 144 ms, faster than 39.45%
# Memory Usage: 15.5 MB, less than 10.60%
class PrefixSuffixAlt:
    def maxProduct(self, nums: List[int]) -> int:
        nums_reversed = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            nums_reversed[i] *= nums_reversed[i - 1] or 1
        return max(nums + nums_reversed)


# Going one step further, we can make the observation that a negative
# value changes the sign of the product, if we had a negative product
# from the subarray up to this value, it would become a positive one.
# Now we see that we can iterate over the array keeping the maximum and
# minimum product that we can obtain from a subarray up to this point.
# We visit each value of the input, computing the maximum and minimum
# that we could obtain up to this point by:
#
# - The maximum is the maximum of:
#   - The product of the current value by the current maximum.
#     (handles positive values correctly)
#   - The product of the current value by the current minimum.
#     (handles negative values correctly)
#   - The value that we are visiting itself.
#     (handles correctly restarting the calculation after seeing a 0)
#
# - The minimum is the minimum of:
#   - The product of the current value by the current maximum.
#     (it would store a current maximum that was negated by the current
#      value and was converted to the maximum at a later point)
#   - The product of the current value by the current minimum.
#     (it handles small positive values)
#   - The value that we are visiting itself.
#     (handles correctly restarting the calculation after seeing a 0)
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - Three variables.
#
# Runtime: 107 ms, faster than 74.44%
# Memory Usage: 14.4 MB, less than 79.17%
class DP:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the result, we know we have at least one element.
        result = nums[0]
        # Initialize a current maximum and minimum to a value neutral
        # for the product. We could also use 0s because the logic
        # handles correctly 0s in the array.
        current_min, current_max = 1, 1  # 0, 0
        # Iterate over the elements of nums.
        for num in nums:
            # Compute the new maximum and minimum values taking into
            # account the sign of the value. Adding num to the max and
            # min functions arguments also takes care to reinitialize
            # the computation after finding a 0.
            current_max, current_min = max(
                num * current_max, num * current_min, num
            ), min(current_max * num, num * current_min, num)
            result = max(result, current_max)
        return result


def test():
    executors = [
        BruteForce,
        PrefixSuffix,
        PrefixSuffixAlt,
        DP,
    ]
    tests = [
        [[0], 0],
        [[-2, -1, -3], 3],
        [[0, -1, -2, -3], 6],
        [[-1, -2, -3], 6],
        [[-2, 0], 0],
        [[0, -1], 0],
        [[-2, 0, -1, -2], 2],
        [[2, 3, -2, 4], 6],
        [[2, 3, -2, 4, 3], 12],
        [[2, 3, -2, 4, -3], 144],
        [[2, 3, -2, 4, 0, 2, 3, -2, 4, -3], 144],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1000):
            for n, t in enumerate(tests):
                sol = executor()
                # One of the solutions mutates the input.
                result = sol.maxProduct([*t[0]])
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
