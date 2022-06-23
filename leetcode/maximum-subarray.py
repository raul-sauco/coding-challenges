# https://leetcode.com/problems/maximum-subarray/

from functools import cache
import timeit
from typing import List


# This solution with O(n) complexity uses the following intuition:
# the sum of the array marked by [i,j] will always follow:
# sum[i,j] = sum[0,j] - sum[0,i-1] for any i > 0 and sum[0,j] for i==0
# If we calculate sum[0,j] for all elements of the array, we can find the solution in O(n)
#
# Runtime: 849 ms, faster than 74.31% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28.8 MB, less than 9.68 % of Python3 online submissions for Maximum Subarray.
class TwoPointers:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        min_found = 0   # We can always not take any numbers starting at i=0
        for j in range(len(nums)):
            if j == 0:
                max_sum = nums[j]
                if nums[j] < min_found:
                    min_found = nums[j]
            else:
                nums[j] += nums[j-1]
                best_sum = nums[j] - min_found
                if nums[j] < min_found:
                    min_found = nums[j]
                if best_sum > max_sum:
                    max_sum = best_sum

        return max_sum


# This solution with complexity O(n) uses the intuition that we can discard any array prefixes that
# contribute a negative sum. This is Kadane's algorithm not using if instead of max()
#
# Runtime: 984 ms, faster than 55.29% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28.5 MB, less than 9.68 % of Python3 online submissions for Maximum Subarray.
class SlidingWindow:
    def maxSubArray(self, nums: List[int]) -> int:
        max_found = nums[0]
        current_sum = 0
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            if current_sum > max_found:
                max_found = current_sum
        return max_found


# This is a memory optimization on the sliding window approach where we store the computed values
# in the array itself.
#
# When the sum of the array up to i-1 is negative, we do not take it into account.
# When the sum of the array up to i-1 is positive, we add it, and store it, at nums[i]
class OptimizedSlidingWindow:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


# Below are two dynamic programming solutions
# The tabulation solution is pretty efficient, memoization not so much
#
# Runtime: 1131 ms, faster than 36.20% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 27.9 MB, less than 38.89 % of Python3 online submissions for Maximum Subarray.
class Tabulation:
    def maxSubArray(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)


class Memoization:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums):
                return 0 if must_pick else float('-inf')
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)


# Divide and conquer works on O(n*log(n)) not the best approach.
# Interesting to practice divide and conquer problems.
class DivideAndConquer:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)):
            pre[i] += max(0, pre[i-1])
        for i in range(len(nums)-2, -1, -1):
            suf[i] += max(0, suf[i+1])

        def maxSubArray(array, left, right):
            if left == right:
                return array[left]
            mid = (left + right) // 2
            return max(maxSubArray(array, left, mid), maxSubArray(array, mid+1, right), pre[mid] + suf[mid+1])
        return maxSubArray(nums, 0, len(nums)-1)


# This is the naive solution where we recursively calculate the sum of elements
# between i and j multiple times. O(n^3)


class BruteForce:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(len(nums)):
            for j in range(len(nums)-1, i-1, -1):
                local_sum = 0
                for n in range(i, j+1):
                    local_sum += nums[n]
                max_sum = max(local_sum, max_sum)
        return max_sum


def test():
    executor = [
        {'executor': SlidingWindow, 'title': 'SlidingWindow', },
        {'executor': OptimizedSlidingWindow, 'title': 'OptimizedSW', },
        {'executor': Tabulation, 'title': 'Tabulation', },
        {'executor': TwoPointers, 'title': 'TwoPointers', },
        {'executor': DivideAndConquer, 'title': 'DivideAndConquer', },
        {'executor': Memoization, 'title': 'Memoization', },
        {'executor': BruteForce, 'title': 'BruteForce', },
    ]
    tests = [
        [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
        [[1], 1],
        [[5, 4, -1, 7, 8], 23],
        [[-2, -1], -1],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.maxSubArray([*t[0]])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
