# 918. Maximum Sum Circular Subarray
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-sum-circular-subarray/
#
# Tags: Array - Divide and Conquer - Dynamic Programming - Queue
# - Monotonic Queue

import timeit
from typing import List


# The maximum sum if we can go over the end and use values at the
# beginning of the array will be either the classical maximum that we
# can obtain using Kadane's algorithm, if the maximum subarray does not
# overlap the going around point, or the sum of all values in the array
# minus the minimum subarray in the original input. We can compute both,
# and the sum of values in the array, using a single pass and Kadane's
# algorithm.
#
# Time complexity: O(n) - We visit each value in the input once.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 516 ms Beats 93.34%
# Memory 18.6 MB Beats 99.58%
class Kadanes:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = min_sum = current_max = current_min = total = nums[0]
        for num in nums[1:]:
            # Compute the maximum subarray using Kadane's.
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)
            # Use a reversed version of Kadane's to compute the minimum
            # subarray inside the input array.
            current_min = min(current_min + num, num)
            min_sum = min(current_min, min_sum)
            total += num
        # Return the best result between the max of a section of the
        # original array and removing the minimum array from the
        # original array.
        return max_sum if min_sum == total else max(total - min_sum, max_sum)


def test():
    executors = [Kadanes]
    tests = [
        [[5, -3, 5], 10],
        [[-3, -2, -3], -2],
        [[1, -2, 3, -2], 3],
        [[5, -3, -7, 5], 10],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxSubarraySumCircular(t[0])
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
