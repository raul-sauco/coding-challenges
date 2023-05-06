# 1498. Number of Subsequences That Satisfy the Given Sum Condition
# 🟠 Medium
#
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
#
# Tags: Array - Two Pointers - Binary Search - Sorting

import timeit
from bisect import bisect_right
from typing import List


# Sort the input array, then we can iterate over the numbers, starting
# at the lowest, and binary search the highest value that we can use in
# combination with the lower l. The number of valid combinations is the
# number of subsequences that we can build with sn[l] as the min and
# none or any of the other values between l and r as the maximum.
#
# Time complexity: O(log(n) * n) - We sort the input elements, which
# already takes O(log(n)*n), then we also try all elements as the lower
# boundary l and, for each, binary search in log(n) the maximum r that
# we can use.
# Space complexity: O(n) - The sorted array takes extra n memory.
#
# Runtime 9342 ms Beats 24.29%
# Memory 29.1 MB Beats 8.18%
class BinarySearch:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Sort nums to use binary search later.
        sn = sorted(nums)
        res, mod, r = 0, 1_000_000_007, len(nums)
        for l, num in enumerate(sn):
            r = bisect_right(sn, target - num, lo=l, hi=r)
            # If the insert position would be to the right of l.
            if l < r:
                res += 2 ** (r - l - 1)
                res %= mod
            else:
                break
        return res


# Sort the input array, then we can iterate over the numbers, starting
# at the lowest, and binary search the highest value that we can use in
# combination with the lower l. The number of valid combinations is the
# number of subsequences that we can build with sn[l] as the min and
# none or any of the other values between l and r as the maximum.
#
# Time complexity: O(log(n) * n) - Sorting still takes the same time,
# but once we have a sorted array, the rest of the algorithm now works
# in O(n), we can accomplish the same using binary search and passing
# l as the low bound and r as the high bound.
# Space complexity: O(n) - The sorted array takes extra n memory.
#
# Runtime 7907 ms Beats 53.45%
# Memory 29 MB Beats 11.51%
class TwoPointers:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res, r = 0, len(nums) - 1
        for l in range(len(nums)):
            while nums[l] + nums[r] > target and l <= r:
                r -= 1
            if l <= r:
                res += 2 ** (r - l)
            else:
                break
        return res % 1_000_000_007


def test():
    executors = [
        BinarySearch,
        TwoPointers,
    ]
    tests = [
        [[3, 5, 6, 7], 9, 4],
        [[3, 3, 6, 8], 10, 6],
        [[2, 3, 3, 4, 6, 7], 12, 61],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numSubseq(t[0], t[1])
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
