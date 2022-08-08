# 300. Longest Increasing Subsequence
# 🟠 Medium
#
# https://leetcode.com/problems/longest-increasing-subsequence/
#
# Tags: Array - Binary Search - Dynamic Programming

import timeit
from typing import List

# TODO add incremental solutions until we get to O(n*log(n))

# We can use an array to store partial results. On each position i, we
# will store the index of nums where we can find the last element of a
# sequence of length i. Then we iterate over all values of nums in O(n)
# and, for each, we search the dp array for the longest sequence we can
# find (the highest index of dp) that points to a value in nums that is
# smaller than the current value we are checking. Since the value is
# smaller, we know that we can build a sequence of length i + 1.
#
# Time complexity: O(n*log(n)) - We iterate over all values in nums and,
# for each, we do a binary search on dp in O(log(n))
# Space complexity: O(n) - dp has length n + 1.
#
# Runtime: 161 ms, faster than 75.57%
# Memory Usage: 14.2 MB, less than 83.70%
class BottomUpDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # An array with the index of the last element of a sequence of
        # len(i), i.e. dp[4] contains the index of the last element of
        # nums that forms a subsequence of length 4.
        dp = [None] * (len(nums) + 1)
        # Store the longest subsequence that we have seen.
        lis = 0
        for i in range(len(nums)):
            # Binary search for the smallest positive l ≤ lis such
            # that nums[dp[l]] > nums[i]
            lo = 1
            hi = lis + 1
            while lo < hi:
                mid = lo + ((hi - lo) // 2)  # lo <= mid < hi
                if nums[dp[mid]] >= nums[i]:
                    hi = mid
                else:  # if nums[dp[mid]] < nums[i]
                    lo = mid + 1
            # After searching, lo == hi is 1 greater than the length of
            # the longest prefix of nums[i]
            sequence_length = lo
            # After we determine the longest sequence that has this
            # number as its last component, store it in our dp array.
            dp[sequence_length] = i
            # We found a new longest sequence.
            if sequence_length > lis:
                lis = sequence_length
        # Return the longest sequence that we have seen.
        return lis


def test():
    executors = [BottomUpDP]
    tests = [
        [[10, 9, 2, 5, 3, 7, 101, 18], 4],
        [[0, 1, 0, 3, 2, 3], 4],
        [[7, 7, 7, 7, 7, 7, 7], 1],
        [[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.lengthOfLIS(t[0])
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
