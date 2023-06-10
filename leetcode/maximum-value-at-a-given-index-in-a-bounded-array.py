# 1802. Maximum Value at a Given Index in a Bounded Array
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
#
# Tags: Binary Search - Greedy

import timeit


# The problem is asking us for the maximum value, to compute the sum of the
# array, we need to try different values, if we do that sequentially, we will
# need O(n*o) where n is the number of possible values and o is the cost of
# computing the sum given a value. If we use binary search, we can reduce that
# to O(log(n)*o) where n is again the number of possible values that we need to
# try. In this problem, we can choose to construct the minimum possible array
# given the value that we are trying, that array will be, given the conditions,
# a decreasing by 1 sequence in both sides of the value that we are trying
# because we want to maximize that one value while minimizing the sum of
# values in the array. We can use the arithmetic progression formula to compute
# the sum of values in the array in O(1)
#
# Time complexity: O(log(k)) - Where k is the number of possible values that
# we need to try and it is equal to maxSum.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 63 ms Beats 12.21%
# Memory 16.2 MB Beats 66.41%
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # A function that computes the sum of an array given the problem
        # requirements and a value at the given index.
        def computeSum(val: int) -> int:
            m = min(index, val)
            a = max(val - m, 0)
            toLeft = (m / 2) * (2 * a + (m - 1))
            if index >= val:
                toLeft += index - val + 1
            k = n - (index + 1)
            m = min(val, k)
            a = max(val - m, 0)
            toRight = (m / 2) * (2 * a + (m - 1))
            if k >= val:
                toRight += k - val + 1

            return toLeft + val + toRight

        # Binary search the ideal value.
        l, r = 1, maxSum
        while l < r:
            mid = (l + r + 1) // 2
            s = computeSum(mid)
            if computeSum(mid) <= maxSum:
                l = mid
            else:
                r = mid - 1
        return l


def test():
    executors = [Solution]
    tests = [
        [4, 0, 4, 1],
        [4, 2, 6, 2],
        [6, 1, 10, 3],
        [9, 5, 24, 4],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxValue(t[0], t[1], t[2])
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
