# 4. Median of Two Sorted Arrays
# 🔴 Hard
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Tags: Array - Binary Search - Divide and Conquer

import timeit
from statistics import median
from typing import List

# 1_000 calls
# » Naive               0.01636   seconds
# » NaiveO1             0.01746   seconds
# » BinarySearch        0.00990   seconds
# » DivideAndConquer    0.01648   seconds
# » StatisticsMedian    0.00491   seconds

# The naive solution merges the two arrays into one sorted array and
# returns the median.
#
# Time complexity: O(m+n) - Where m and n are the length of the two
# input arrays.
# Space complexity: O(m+n) - We store the values of both arrays into a
# new one.
#
# Runtime: 108 ms, faster than 84.51%
# Memory Usage: 14.1 MB, less than 67.86%
class Naive:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        merged, i, j = [None] * (len(nums1) + len(nums2)), 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged[i + j] = nums1[i]
                i += 1
            else:
                merged[i + j] = nums2[j]
                j += 1
        # Append leftover nums.
        while i < len(nums1):
            merged[i + j] = nums1[i]
            i += 1
        while j < len(nums2):
            merged[i + j] = nums2[j]
            j += 1
        if len(merged) % 2:
            return merged[len(merged) // 2]
        else:
            mid = len(merged) // 2
            return (merged[mid - 1] + merged[mid]) / 2


# A memory optimization of the naive solution, instead of merging the
# arrays, compute which indexes we need and return the values at these
# indexes. This solution is not valid because the exercise asks for a
# O(log(n)) time complexity, but it still passes the tests.
#
# Time complexity: O(m+n) - Where m and n are the length of the two
# input arrays, we visit half the elements of both arrays combined.
# Space complexity: O(1) - We only store pointers.
#
# Runtime: 214 ms, faster than 41.96%
# Memory Usage: 14.3 MB, less than 6.49%
class NaiveO1:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        L = len(nums1) + len(nums2)
        # The indexes we are looking for.
        k, l = (L - 1) // 2, L // 2
        # The values at these indexes in the merged input.
        med1, med2 = None, None
        # Pointers to the indexes that we are evaluating.
        i, j = 0, 0
        while med1 is None or med2 is None:
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    if i + j == k:
                        med1 = nums1[i]
                    if i + j == l:
                        med2 = nums1[i]
                    i += 1
                else:
                    if i + j == k:
                        med1 = nums2[j]
                    if i + j == l:
                        med2 = nums2[j]
                    j += 1
            # Append leftover nums.
            while i < len(nums1):
                if i + j == k:
                    med1 = nums1[i]
                if i + j == l:
                    med2 = nums1[i]
                i += 1
            while j < len(nums2):
                if i + j == k:
                    med1 = nums2[j]
                if i + j == l:
                    med2 = nums2[j]
                j += 1
        return (med1 + med2) / 2


# Use a divide and conquer algorithm, compute the positions on the
# merged array that we are looking for and have an auxiliary function
# return them. Each iteration of the function discards half of one of
# the input arrays at each iteration until there is only one element
# left between both of them.
#
# Time complexity: O(log(m+n)) - At each iteration the algorithm
# discards half of one of the current arrays.
# Space complexity:  O(log(m+n)) - The call stack will have one call for
# each time that we can discard half of one of the arrays.
#
# Runtime: 201 ms, faster than 54.32%
# Memory Usage: 14.2 MB, less than 24.81%
class DivideAndConquer:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        # Store the length of both arrays combined.
        N1, N2 = len(nums1), len(nums2)
        L = N1 + N2
        # Left and right indexes of both arrays.
        l1, l2, r1, r2 = 0, 0, N1 - 1, N2 - 1
        # For uneven length input size, return the median.
        if L % 2:
            return self.kthSmallest(nums1, nums2, l1, r1, l2, r2, L // 2)
        # For event length input size, return the average of the two
        # values around the middle.
        else:
            return (
                self.kthSmallest(nums1, nums2, l1, r1, l2, r2, L // 2)
                + self.kthSmallest(nums1, nums2, l1, r1, l2, r2, L // 2 - 1)
            ) / 2

    # Return the kth smallest element between two given arrays.
    def kthSmallest(
        self,
        a: List[int],
        b: List[int],
        la: int,
        ra: int,
        lb: int,
        rb: int,
        k: int,
    ) -> int:
        # If one of the lists is empty, return the kth element on the
        # other list, counting from the current left start index.
        if la > ra:
            return b[k - la]
        if lb > rb:
            return a[k - lb]
        ma, mb = (la + ra) // 2, (lb + rb) // 2
        # If we have less than k values to the left of the indices, we
        # want to move one of them right, check which one and adjust its
        # left pointer.
        if ma + mb < k:
            # If the value under ma is greater than the value under mb,
            # and we need to move one of the pointers right, we need to
            # update mb because we know that all the values to the left
            # will be smaller than a[ma].
            if a[ma] > b[mb]:
                return self.kthSmallest(a, b, la, ra, mb + 1, rb, k)
            else:
                return self.kthSmallest(a, b, ma + 1, ra, lb, rb, k)
        # The opposite case, we have too many values left of the mid
        # pointers, we need to move one of them left adjust one of the
        # right pointers.
        else:
            if a[ma] > b[mb]:
                return self.kthSmallest(a, b, la, ma - 1, lb, rb, k)
            else:
                return self.kthSmallest(a, b, la, ra, lb, mb - 1, k)


# Use binary search, we choose the smaller input array, or either if the
# same size, and do binary search for the edge of the partition, we try
# positions and adjust the boundary left or right based on whether we
# still have greater values on the left partition or lesser values on
# the right partition than the values at the boundaries.
#
# Time complexity: O(log(min(m, n))) - We do binary search on the
# smaller array.
# Space complexity: O(1) - We use constant space.
#
# Runtime: 230 ms, faster than 26.10%
# Memory Usage: 14.2 MB, less than 24.83%
class BinarySearch:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        # Shorten the array names.
        a, b = nums1, nums2
        K = (len(a) + len(b)) // 2
        # Make sure that a is the shorter array, we will be doing binary
        # search in a.
        if len(a) > len(b):
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            mid = (l + r) // 2
            # Compute the position on b that gives us a K-sized split.
            # K is the number of elements that the left partition should
            # have, but k is the index of the rightmost element on the
            # combination that we are trying, -2 to make up for 0
            # indexed arrays.
            k = K - mid - 2
            # Compute the values to the right and left of the current
            # partition. Use +- inf to handle cases when we have
            # exhausted one of the arrays' values.
            la = a[mid] if mid >= 0 else float("-inf")
            ra = a[mid + 1] if mid + 1 < len(a) else float("inf")
            lb = b[k] if k >= 0 else float("-inf")
            rb = b[k + 1] if k + 1 < len(b) else float("inf")
            # Check the partition obtained for correctness. If the
            # smallest value on the greater-than partition in a is
            # smaller than the largest value in the smaller-than
            # partition in b, we need to try the right side of a.
            if lb > ra:
                l = mid + 1
            # If the smallest value on the greater-than partition in b
            # is smaller than the largest value in the smaller than
            # partition in a, we need to try the left side of a.
            elif la > rb:
                r = mid - 1
            # If la <= rb and lb <=ra we have a correct partition.
            else:
                # If the input had an uneven number of values, the
                # median will be the smallest value on the right side.
                if (len(a) + len(b)) % 2:
                    return min(ra, rb)
                # If the input had an even number of values, the median
                # will be the average of the maximum value on the
                # left partition and the minimum value on the right
                # partition.
                else:
                    return (max(la, lb) + min(ra, rb)) / 2


# This solution would not be what is expected in an interview, but
# probably still worth mentioning it since, even though it is not a
# valid solution given the constraints of the description, because its
# time complexity is O(n*log(n)), it does run faster than the O(log(n))
# solutions. It probably runs faster because it is implemented in C.
#
# Time complexity: O((m+n)*log(m+n)) - I didn't check the implementation,
# but it is safe to assume that it sorts the array, then picks the median.
# Space complexity: O(m+n) - We use an array that contains all the
# values in both input arrays.
#
# Runtime: 104 ms, faster than 86.91%
# Memory Usage: 14.2 MB, less than 24.83%
class StatisticsMedian:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        return median(nums1 + nums2)


def test():
    executors = [
        Naive,
        NaiveO1,
        BinarySearch,
        DivideAndConquer,
        StatisticsMedian,
    ]
    tests = [
        [[], [2], 2.0],
        [[1, 3], [2], 2.0],
        [[0, 0], [0, 0], 0.0],
        [[1, 2], [3, 4], 2.5],
        [
            [1, 1, 2, 2, 3, 3, 5, 6],
            [4, 5, 8, 10, 12, 15, 18, 20, 21, 23, 24, 30],
            7,
        ],
        [
            [1, 1, 2, 2, 3, 3, 5, 6, 8],
            [4, 5, 8, 10, 12, 15, 18, 20, 21, 23, 24, 30],
            8,
        ],
        [
            [-16, -16, -16, -16, -16, -14, -13, -12, -11, -10, -9, -8],
            [1, 1, 1, 1, 1, 1],
            -10.5,
        ],
        [
            [2, 3, 4, 8, 18, 28],
            [-16, -12, -4, -3, -2, -1, 0, 3, 8, 10, 15, 23],
            3.0,
        ],
        [
            [-12, -4, -3, -2, -1, 0, 3, 8, 10, 15, 23],
            [2, 3, 4, 8, 18, 28, 45],
            3.5,
        ],
        [
            [2, 3, 4, 8, 18, 28, 35, 42, 43],
            [-16, -12, -4, -3, -2, -1, 0, 3, 8, 10, 15, 23],
            4.0,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findMedianSortedArrays(t[0], t[1])
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
