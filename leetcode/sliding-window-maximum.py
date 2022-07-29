# 239. Sliding Window Maximum
# 🔴 Hard
#
# https://leetcode.com/problems/sliding-window-maximum/
#
# Tags: Array - Queue - Sliding Window - Heap (Priority Queue)
# - Monotonic Queue

import timeit
from collections import deque
from heapq import heappop, heappush
from typing import List


# We can start with the brute-force method, for each position in the
# input list, iterate over all numbers in the window and add the max to
# the result set.
#
# Time complexity: O(n*k) - For each position n, we visit k positions
# trying to find the window maximum. Equivalent to O(n^2) for large k.
# Space complexity: O(n) - We keep the results in a list that will be
# size n-k which simplifies to O(n).
#
# This solution would fail with Time Limit Exceeded.
class BruteForce:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize a list in O(n) to store results in O(1).
        res = [None] * (len(nums) - k + 1)

        # Iterate over the positions from 0 to len(nums) - k + 1.
        for left in range(len(nums) - k + 1):
            window_max = nums[left]
            # Iterate over the values in the current window and find the
            # maximum.
            for idx in range(left + 1, left + k):
                if nums[idx] > window_max:
                    window_max = nums[idx]

            # Store the maximum on the result array.
            res[left] = window_max

        # Return the result.
        return res


# Looking at the brute-force solution above, we can see that the problem
# is that for each value of n, we visit k numbers, for large values of
# k that is O(n^2) time complexity. Since we have to visit at least once
# each value of nums, we need to focus in reducing the complexity of
# obtaining the maximum value in the sliding window. A data structure
# that can help us do that is a heap. By pushing elements that we visit
# into the heap, with O(log(n)) cost, we can fetch the biggest element
# in the heap in O(1) time. We can push the element value together with
# its position in the input array, that way we can check if the top
# element is still within the sliding window before using it.
#
# Time complexity: O(n*log(n)) - We visit each element and push-pop from
# the heap for each.
# Space complexity: O(n) - The result array size depends on the input
# size.
#
# Runtime: 4057 ms, faster than 6.65% of Python3 online submissions for
# Sliding Window Maximum.
# Memory Usage: 36.6 MB, less than 7.51% of Python3 online submissions
# for Sliding Window
class Heap:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Use a heap of tuples to store the maximum value of the current
        # window. Each element will store (-value, index) that way the
        # heap structure itself guarantees that we have the maximum
        # value at the top heap[0], and we can use the index to check
        # that the value is within the sliding window.
        heap = []
        # Store the results in a list. Since we know the size that the
        # results array will have, it is better to initialize the full
        # array with dummy values in O(n) and then insert using indexes
        # in O(1) than to initialize an array of length 0 that will need
        # to grow, in O(n) time, every time it reaches 2^x size.
        res = [None] * (len(nums) - k + 1)
        # Iterate over all values in nums. O(n)
        for idx, num in enumerate(nums):
            # Reverse the value to use it later.
            val = -num
            # If the max value of the heap is smaller than the current
            # value, we are not interested on it any longer, pop it.
            # Popping smaller values from the heap is not necessary but
            # keeping the number of elements in it small helps reduce
            # the cost of reordering it when we push or pop.
            # Make sure that the top element is in the sliding window
            # before we use it. Elements are tuples of (value, index)
            # we need to access the index.
            while heap and (heap[0][0] > val or heap[0][1] <= idx - k):
                heappop(heap)
            # Push the current value into the heap. O(log(n))
            # The heapq module implements a minimum heap, we need to
            # reverse the value to keep the maximum value at the top.
            heappush(heap, (val, idx))
            # This check is necessary because we start iterating from
            # the first index, which means that the window will not have
            # the required length. Wait until it does before adding any
            # results to the result array.
            if idx >= k - 1:
                # Once the sliding window reaches size k, start
                # start calculating results, we can fetch the largest
                # value in the heap in O(1)
                # Insert in O(1) instead of appending in amortized O(1)
                res[idx - k + 1] = -heap[0][0]

        return res


# We can use a monotonic queue to be able to access the max value in the
# sliding window in linear time. The monotonic queue will store a
# maximum of k elements and it guarantees that the order of the elements
# is strictly increasing from left to right.
#
# Since we are managing the monotonic queue manually, i.e. it is not a
# built-in structure like the heap of the previous solution, we can
# store element indexes in the queue and access the element in nums to
# check its value. This has the advantage that we check both value and
# position storing only one value.
#
# https://en.wikipedia.org/wiki/Monotone_priority_queue
#
# Time complexity: O(n) - We only visit each element once, and push/pop
# it from the queue a maximum of 1 time.
# Space complexity: O(n) - The queue is of max size k, but the result
# array size depends on the input size as well.
#
# Runtime: 2147 ms, faster than 80.18% of Python3 online submissions for
# Sliding Window Maximum.
# Memory Usage: 30.8 MB, less than 12.36% of Python3 online submissions
# for Sliding Window Maximum.
class MonotonicQueue:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic queue, we will preserve strictly increasing order
        # from the left to the right so that we guarantee for any i < j
        # q[i] < q[j]
        q = deque()
        # Store the results in a list. Since we know the size that the
        # results array will have, it is better to initialize the full
        # array with dummy values in O(n) and then insert using indexes
        # in O(1) than to initialize an array of length 0 that will need
        # to grow, in O(n) time, every time it reaches 2^x size.
        res = [None] * (len(nums) - k + 1)
        # Iterate over all values in nums. O(n)
        for idx, num in enumerate(nums):
            # Maintain the monotonicity of the queue. If num is greater
            # than the values in queue, then the values don't have any
            # more use for us and we can pop them. We start popping from
            # the left, where the smallest value in the queue resides.
            # Note that the queue stores indexes to nums, not the values
            # themselves, we use the index to access the value in nums
            # to check it.
            while q and nums[q[-1]] <= num:
                q.pop()
            # Once we have popped all values smaller than the current
            # one, append it at the left end of the queue, preserving
            # its monotonicity. If there were any larger values, they
            # will still be in the queue, to the left of the value we
            # just pushed.
            q.append(idx)
            # The furthest left element could be outside the sliding
            # window at this point, check and pop it in that case.
            if q[0] == idx - k:
                q.popleft()
            # This check is necessary because we start iterating from
            # the first index, which means that the window will not have
            # the required length. Wait until it does before adding any
            # results to the result array.
            if idx >= k - 1:
                # Once the sliding window reaches size k, start
                # start calculating results, we can fetch the largest
                # value on the monotonic queue in O(1)
                # Insert in O(1) instead of appending in amortized O(1)
                res[idx - k + 1] = nums[q[0]]

        return res


def test():
    executors = [
        BruteForce,
        Heap,
        MonotonicQueue,
    ]
    tests = [
        [[1], 1, [1]],
        [
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3],
            3,
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1],
        ],
        [[1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxSlidingWindow(t[0], t[1])
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
