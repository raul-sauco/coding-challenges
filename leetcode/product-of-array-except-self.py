# https://leetcode.com/problems/product-of-array-except-self/

# Tags: Array - Prefix Sum

import timeit
from itertools import accumulate
from operator import mul
from typing import List


# Calculate the prefix and suffix products, for each item i, the multiplication of the prefix to i-1 + suffix to i+1
# is the product of all the elements except itself.
#
# Time complexity: O(n) - we visit each element 3 times
# Space complexity: O(n) - we store three arrays of size n
#
# Runtime: 497 ms, faster than 10.06% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 22.4 MB, less than 17.96% of Python3 online submissions for Product of Array Except Self.
class PrefixSuffix:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Using a lambda
        # prefixes = [*accumulate(nums, lambda a, b: a * b)]
        # suffixes = [*accumulate(nums[::-1], lambda a, b: a * b)][::-1]

        # Using assignments https://peps.python.org/pep-0572/
        # p, s = 1, 1
        # prefixes = [(p := p * n) for n in nums]
        # suffixes = [(s := s * n) for n in nums[::-1]][::-1]

        # Using accumulate and mul
        prefixes = list(accumulate(nums, mul))
        suffixes = list(accumulate(nums[::-1], mul))[::-1]
        return [
            (prefixes[i - 1] if i > 0 else 1) * (suffixes[i + 1] if i < len(nums) - 1 else 1) for i in range(len(nums))
        ]


# Using two variables for the prefix and suffix products, we can calculate the result in one pass using only the
# result array for space.
#
# We iterate over a range [0..len(nums)], for each step, we update the current prefix and suffix products and the
# values of result at result[i] and result[-i], when we complete the loop, we have visited each position twice,
# multiplying the value at that position by both the prefix product up to the previous item and the suffix product
# up to the following item.
#
# Time complexity; O(n) - we iterate over the elements of nums once, visiting two elements on each step
# Space complexity: O(1) - the description tells us to not consider the result array in the space complexity
#
# Runtime: 255 ms, faster than 84.79% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.2 MB, less than 43.25% of Python3 online submissions for Product of Array Except Self.
class SpaceOptimized:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result, prefix_product, suffix_product = [1] * len(nums), 1, 1
        for idx in range(len(nums)):
            # Multiply the current position with the prefix prod of the previous position
            result[idx] *= prefix_product
            # Update the current prefix product with the value of nums at index idx
            prefix_product *= nums[idx]

            # Multiply the -idx position with the current suffix product for values to its right
            result[-1 - idx] *= suffix_product
            # Update the current suffix product to include the value of nums at index -idx
            suffix_product *= nums[-1 - idx]

        return result


def test():
    executors = [PrefixSuffix, SpaceOptimized]
    tests = [
        [
            [1, 2, 3, 4],
            [24, 12, 8, 6],
        ],
        [
            [-1, 1, 0, -3, 3],
            [0, 0, 9, 0, 0],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.productExceptSelf(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
