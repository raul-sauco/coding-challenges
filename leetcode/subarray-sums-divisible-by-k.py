# 974. Subarray Sums Divisible by K
# 🟠 Medium
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/
#
# Tags: Array - Hash Table - Prefix Sum

import timeit
from typing import List


# The brute force solution explores every pair of start and end indexes
class BruteForce:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count, n = 0, len(nums)
        for i in range(n):
            current = 0
            for j in range(i, n):
                current += nums[j]
                if current % k == 0:
                    count += 1
        return count


# Create an array with the count of times we have obtained a certain
# remainder in the input array up to that point when we have computed
# prefix_sum % k, the subarray between two equal results will always be
# divisible by k.
#
# Time complexity: O(n+k) - We visit each element of the input array and
# do O(1) operations. We also iterate over k elements to create the
# count array.
# Space complexity: O(k) - We use an array of size k of extra memory.
#
# Runtime 286 ms Beats 97.88%
# Memory 18.9 MB Beats 63.55%
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = prefix = 0
        # A count of times that we have seen prefix_sum % k == i.
        count = [1] + [0] * k
        for num in nums:
            # The modulus of the prefix sum up to this index and k.
            prefix = (prefix + num) % k
            # If we have seen the same modulus result before, the sum of
            # the subarray between the current index and any of these
            # indexes will be divisible by k.
            res += count[prefix]
            # Record the current remainder.
            count[prefix] += 1
        return res


def test():
    executors = [
        BruteForce,
        Solution,
    ]
    tests = [
        [[5], 9, 0],
        [[4, 5, 0, -2, -3, 1], 5, 7],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.subarraysDivByK(t[0], t[1])
                exp = t[2]
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
