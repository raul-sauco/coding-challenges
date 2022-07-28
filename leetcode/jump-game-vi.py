# 1696. Jump Game VI
# 🟠 Medium
#
# https://leetcode.com/problems/house-robber-ii/
#
# Tags: Array - Dynamic Programming - Queue - Sliding Window
# - Heap (Priority Queue) - Monotonic Queue

import timeit
from heapq import heappop, heappush
from typing import List


# We can visit each element of nums, for each, calculate the best way to
# reach it from the k elements from which we can jump to this one. To
# avoid having to visit the k elements in each iteration, we can use a
# sliding window to record the best value of the possible ones, on each
# step, we add the value under the right pointer to the pool and remove
# the value under the left pointer.
#
# Time complexity: O(n*log(n)) - We visit each element and, for each,
# push into the heap at O(log(n)). We have no guarantee that the heap
# will stay under size k, it would only if the max element was coming
# out of the sliding window. If the max element gets replaced as the
# top of the heap, it will stay in. The heap could grow to size n.
# Space complexity; O(n) - Same as before, the heap could grow to the
# same size as the input list.
#
# Runtime: 2338 ms, faster than 14.21% of Python3 online submissions for
# Jump Game VI.
# Memory Usage: 33.5 MB, less than 30.88% of Python3 online submissions
# for Jump Game VI.
class ListAndHeap:
    def maxResult(self, nums: List[int], k: int) -> int:
        # If we don't have any values, the max will be 0.
        if not nums:
            return 0

        heap = []
        for i, num in enumerate(nums):
            # Base case, we start at index 0, preserve the value and
            # push it into the heap.
            if i == 0:
                heappush(heap, (-num, i))
                continue
            else:
                # Pop the top element if it is left of the start of the
                # sliding window of values we can use.
                while heap[0][1] < i - k:
                    heappop(heap)

                # Update the current position with the most gain we can
                # obtain jumping here.
                nums[i] -= heap[0][0]

                # Push the current value into the heap.
                heappush(heap, (-nums[i], i))

        return nums[-1]


# Looking at the previous solution, we can see that we are updating the
# list but only using its value to push into the heap, we can simplify
# the solution by using the heap, instead of nums, as our dp.
#
# Time complexity: O(n*log(n)) - We update the heap for each value of
# the input array.
# Space complexety: O(n) - for the heap.
#
# Runtime: 1843 ms, faster than 40.83% of Python3 online submissions for
# Jump Game VI.
# Memory Usage: 33.3 MB, less than 34.29% of Python3 online submissions
# for Jump Game VI.
class Heap:
    def maxResult(self, nums: List[int], k: int) -> int:
        # If we don't have any values, the max will be 0.
        if not nums:
            return 0
        # Base case, we only have one element.
        result = nums[0]

        # Push the first value into the heap.
        heap = [(-nums[0], 0)]
        for i in range(1, len(nums)):
            # Pop the top element if it is left of the start of the
            # sliding window of values we can use.
            while heap[0][1] < i - k:
                heappop(heap)

            # Update the current position with the most gain we can
            # obtain jumping here.
            result = nums[i] - heap[0][0]

            # Push the current value into the heap.
            heappush(heap, (-result, i))

        return result


# TODO add a monotonic deque solution, something similar to this:
# https://leetcode.com/problems/jump-game-vi/discuss/1260696/Python-Monotonic-deque-explained


def test():
    executors = [ListAndHeap, Heap]
    tests = [
        [[-1], 2, -1],
        [[-1, -1], 200, -2],
        [[1, -1, -2, 4, -7, 3], 2, 7],
        [[10, -5, -2, 4, 0, 3], 3, 17],
        [[1, -5, -20, 4, -1, 3, -6, -3], 2, 0],
        [[1, -5, -20, 4, -1, 3, -6, -3], 20, 5],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e4"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxResult([*t[0]], t[1])
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
