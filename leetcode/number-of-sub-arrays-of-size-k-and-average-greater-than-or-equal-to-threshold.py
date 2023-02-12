# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# 🟠 Medium
#
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
#
# Tags: Array - Sliding Window

import timeit
from typing import List


# For the average to be greater than or equal to the threshold, the sum
# of values needs to be equal to or greater than threshold * k when the
# size of the subarray is k. That lets us compute the solution in linear
# time.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - We use constant extra space.
#
# Runtime 595 ms Beats 96.16%
# Memory 26.7 ms Beats 97.96%
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k > len(arr):
            return 0
        count, t = 0, threshold * k
        window_sum = sum(arr[:k])
        if window_sum >= t:
            count += 1
        for r in range(k, len(arr)):
            window_sum += arr[r] - arr[r - k]
            if window_sum >= t:
                count += 1
        return count


def test():
    executors = [Solution]
    tests = [
        [[20, 20], 3, 4, 0],
        [[2, 2, 2, 2, 5, 5, 5, 8], 3, 4, 3],
        [[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5, 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numOfSubarrays(t[0], t[1], t[2])
                exp = t[3]
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
