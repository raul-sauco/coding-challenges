# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
import math
import random
import timeit
from typing import List

# Local execution times for 1e6 calls.
#
# SortedListSolution  0.40849   seconds
# HQPushPopSolution   1.53406   seconds     * Fastest on LeetCode
# FloydRivestSolution 2.86789   seconds
# HQLargestSolution   3.01774   seconds
# QuickSelectSolution 6.20239   seconds

# Sort the list and return the kth element counting from the back.
# O(n*log(n)) to sort * O(1) to access the element.
#
# Runtime: 80 ms, faster than 74.54% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.7 MB, less than 71.94 % of Python3 online submissions for Kth Largest Element in an Array.


class SortedListSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# Create a heap and keep the largest k elements on it.
# It pushes all elements into the heap and pops the smallest one once the queue reaches size k
#
# This solution performs really well in LeetCode, but worst locally, this is probably due to large n and small k
#
# Runtime: 66 ms, faster than 95.12% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.7 MB, less than 96.17 % of Python3 online submissions for Kth Largest Element in an Array.
class HeapQPushPopSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                heapq.heappushpop(heap, n)
        return heap[0]


# Use heapq.nlargest
#
# Runtime: 94 ms, faster than 58.66% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.7 MB, less than 71.94 % of Python3 online submissions for Kth Largest Element in an Array.
#
# SortedListSolution  0.40698   seconds
# FloydRivestSolution 2.88456   seconds
# HeapQSolution       3.009     seconds
class HeapQLargestSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


# Solution using the Floyd-Rivest algorithm.
# https://en.wikipedia.org/wiki/Floyd–Rivest_algorithm
#
# Implementation from
# https://www.geeksforgeeks.org/floyd-rivest-algorithm/
#
#
# Runtime: 90 ms, faster than 63.07% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15 MB, less than 18.88 % of Python3 online submissions for Kth Largest Element in an Array.
#
# With large sets runs a little slower than the SortedListSolution and uses a lot more memory.
# With smaller lists, its performance is a lot worst.
class FloydRivestSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Finds the k-th smallest element in the lists
        def select(arr: list, left: int, right: int, k: int):
            def swap(arr, i, j):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

            def sign(x):
                if x > 0:
                    return 1
                elif x < 0:
                    return -1
                return 0

            while right > left:
                if right-left > 600:
                    n = right - left + 1
                    i = k - left + 1
                    z = math.log(n)
                    s = 0.5 * math.exp(2 * z / 3)
                    sd = 0.5 * math.sqrt(z * s * (n-s)/n) * sign(i-n / 2)
                    newLeft = int(max(left, k-i * s / n + sd))
                    newRight = int(min(right, k + (n - i) * s / n + sd))
                    select(arr, newLeft, newRight, k)
                t = arr[k]
                i = left
                j = right
                swap(arr, left, k)
                if arr[right] > t:
                    swap(arr, left, right)
                while i < j:
                    swap(arr, i, j)
                    i = i + 1
                    j = j-1
                    while arr[i] < t:
                        i = i + 1
                    while arr[j] > t:
                        j = j-1

                if arr[left] == t:
                    swap(arr, left, j)
                else:
                    j = j + 1
                    swap(arr, right, j)

                if j <= k:
                    left = j + 1
                if k <= j:
                    right = j-1
            return arr[k]

        return select(nums, 0, len(nums)-1, len(nums)-k)


# Quick Select, not as performant as naively expected.
#
# Runtime: 114 ms, faster than 39.60% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.6 MB, less than 96.17 % of Python3 online submissions for Kth Largest Element in an Array.
class QuickSelectSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        size_left, size_mid = len(left), len(mid)
        if k <= size_left:
            return self.findKthLargest(left, k)
        elif k > size_left + size_mid:
            return self.findKthLargest(right, k - size_left - size_mid)
        else:
            return mid[0]


def test():
    executor = [
        {'executor': SortedListSolution, 'title': 'SortedListSolution', },
        {'executor': HeapQPushPopSolution, 'title': 'HQPushPopSolution', },
        {'executor': FloydRivestSolution, 'title': 'FloydRivestSolution', },
        {'executor': HeapQLargestSolution, 'title': 'HQLargestSolution', },
        {'executor': QuickSelectSolution, 'title': 'QuickSelectSolution', },
    ]
    tests = [
        [[3, 2, 1, 5, 6, 4], 2, 5],
        [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e6'))):
            for t in tests:
                sol = e['executor']()
                result = sol.findKthLargest(t[0], t[1])
                expected = t[2]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
