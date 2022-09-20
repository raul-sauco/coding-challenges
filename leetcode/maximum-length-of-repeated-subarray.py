# 718. Maximum Length of Repeated Subarray
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
#
# Tags: Array - Binary Search - Dynamic Programming - Sliding Window -
# Rolling Hash - Hash Function

import timeit
from collections import defaultdict
from typing import List

# 1 call.
# » BruteForce          0.00755   seconds
# » DP                  0.00051   seconds
# » OptimizedDP         0.00042   seconds
# » BSandRH             0.00023   seconds
# » SlidingWindow       0.00017   seconds

# The brute force approach iterates over all the elements in one array
# and, for each, checks the longest substring that can be formed with
# each element of the other array.
#
# Time complexity: O(n^2*m^2) - For each position, we may end up
# iterating over all the positions in both arrays.
# Space complexity: O(1) - Only constant space is used.
#
# This solution would fail with Time Limit Exceeded.
class BruteForce:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize the max length seen to 0.
        res = 0
        # Iterate over all the indices in nums1.
        for i in range(len(nums1)):
            # Iterate over all the indices in nums2.
            for j in range(len(nums2)):
                # Initialize the k pointer that moves forward in both
                # input arrays.
                k = 0
                while (
                    i + k < len(nums1)
                    and j + k < len(nums2)
                    and nums1[i + k] == nums2[j + k]
                ):
                    # This position is a match, move to the next one.
                    k += 1
                    # k is zero indexed, the number of matches is k+1
                    # update the result after moving the pointer.
                    res = max(res, k)
        return res


# We can avoid recalculating the number of matched characters for each
# possible offset and position of the two input arrays by storing them
# into a matrix. Each position of the matrix records the number of
# matching characters that we have if we use its row and column as the
# indexes in the input arrays and work backwards. For example, if
# dp[3][4] = 2, that means that if we start an nums1[2] and nums2[4] and
# compare the values backwards, we will have two equal values, the next
# will not be equal. If we store this data in a matrix, when we want to
# compute the number of matches that we will have at [4][5], we only
# need to check if the values at these indexes are equal, if they are,
# we add 1 to the value found at dp[3][4].
#
# Time complexity: O(n*m) - Where n and m are the size of the input
# arrays. We iterate over one array, for each value, we iterate over all
# the values of the other array.
# Space complexity: O(n*m) - The matrix that stores temporary results
# has a size n*m where n and m are the size of the input arrays.
#
# This solution failed with Time Limit Exceeded.
class DP:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Store the longest repeated substring seen.
        res = 0
        # Use a matrix to store temporary results.
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        # Start iterating from 1 makes indexing easier.
        # Iterating over values of i,j and checking if the values under
        # the pointers match, if the values match, we know that we have
        # a match 1 value longer than what we had before we added the
        # last two values.
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                # If the values under the pointers match, add 1 to the
                # match before we added this two characters.
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # Check if this is the longest match we have seen.
                    res = max(res, dp[i][j])
        return res


# We can optimize the space utilization of the previous solution if we
# realize that at any point we will only need to access values for the
# previous value of i, that lets us discard all other values in the
# matrix.
#
# Time complexity: O(n*m) - Where n and m are the size of the input
# arrays. We iterate over one array, for each value, we iterate over all
# the values of the other array.
# Space complexity: O(min(m,n)) - The array that stores temporary results
# has a size min(m,n) where m and n are the size of the input arrays.
#
# Runtime: 9046 ms, faster than 8.26%
# Memory Usage: 14 MB, less than 88.72%
class OptimizedDP:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Make sure that we use the length of the shortest dimension
        # for the dp array.
        if len(nums1) < len(nums2):
            return self.findLength(nums2, nums1)
        # Store the longest repeated substring seen.
        res = 0
        # Use two arrays to store temporary results.
        dp, prev = [0] * (len(nums2) + 1), [0] * (len(nums2) + 1)
        # Start iterating from 1 makes indexing easier.
        # Iterating over values of i,j and checking if the values under
        # the pointers match, if the values match, we know that we have
        # a match 1 value longer than what we had before we added the
        # last two values.
        for i in range(1, len(nums1) + 1):
            prev = dp
            dp = [0] * (len(nums2) + 1)
            for j in range(1, len(nums2) + 1):
                # If the values under the pointers match, add 1 to the
                # match before we added this two characters.
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev[j - 1] + 1
                    # Check if this is the longest match we have seen.
                    res = max(res, dp[j])
        return res


# TODO study the solution below.

# Binary search the longest match using a rolling hash to check for
# matches. This solution comes from the LeetCode official solutions.
#
# Time complexity: O((m+n)log(min(m,n))) - Creating the rolling hashes
# is O(m+n), the binary search is O(log(min(m,n))), checking for
# duplicate hashes is O(1), the naive check to ensure that we are not
# returning a collision as a false positive is O(min(m,n)).
# Space complexity: O(m) - The hashes dictionary and the subarrays in
# the naive check.
#
# Runtime: 518 ms, faster than 94.29%
# Memory Usage: 14.1 MB, less than 88.72%
class BSandRH:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Use a small prime greater than the values in the array as the
        # base and a large prime as the modulus.
        p, mod = 113, 10**9 + 7
        Pinv = pow(p, mod - 2, mod)

        def check(guess):
            def rolling(arr, length):
                if length == 0:
                    yield 0, 0
                    return

                h, power = 0, 1
                for i, x in enumerate(arr):
                    h = (h + x * power) % mod
                    if i < length - 1:
                        power = (power * p) % mod
                    else:
                        yield h, i - (length - 1)
                        h = (h - arr[i - (length - 1)]) * Pinv % mod

            hashes = defaultdict(list)
            for ha, start in rolling(nums1, guess):
                hashes[ha].append(start)
            for ha, start in rolling(nums2, guess):
                iarr = hashes.get(ha, [])
                if any(
                    nums1[i : i + guess] == nums2[start : start + guess]
                    for i in iarr
                ):
                    return True
            return False

        # Binary search the maximum length of repeated subarray.
        lo, hi = 0, min(len(nums1), len(nums2)) + 1
        while lo < hi:
            mi = (lo + hi) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1


# TODO check for a way to merge both outer loops into one.
# TODO redo this problem, it felt hard for a medium.

# Use a sliding window approach to "slide" one of the input arrays over
# the other, one position at a time, and check what is the longest
# repeated subarray for this relative position of the input arrays.
#
# Time complexity: O(m*n) - For each configuration of m over n, we visit
# all the overlapping positions.
# Space complexity: O(1) - Only constant space used.
#
# Runtime: 1828 ms, faster than 92.02%
# Memory Usage: 14 MB, less than 94.69%
class SlidingWindow:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize the max length seen.
        res = 0
        # Slide nums2 from left to right over nums1.
        for i in range(len(nums1)):
            curr = 0
            for a, b in zip(nums1[i:], nums2):
                if a == b:
                    curr += 1
                else:
                    res = max(res, curr)
                    curr = 0
            res = max(res, curr)

        # Slide nums2 from right to left over nums1.
        for i in range(len(nums2)):
            curr = 0
            for a, b in zip(nums2[i:], nums1):
                if a == b:
                    curr += 1
                else:
                    res = max(res, curr)
                    curr = 0
            res = max(res, curr)
        return res


def test():
    executors = [
        BruteForce,
        DP,
        OptimizedDP,
        BSandRH,
        SlidingWindow,
    ]
    tests = [
        [[0], [0], 1],
        [[0], [1], 0],
        [[1, 2, 3, 2, 1], [3, 7, 1, 4, 7], 1],
        [[1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3],
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5],
        [
            [
                59,
                59,
                59,
                91,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
            ],
            [
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                59,
                94,
            ],
            47,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findLength(t[0], t[1])
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
