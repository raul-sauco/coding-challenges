# 658. Find K Closest Elements
# 🟠 Medium
#
# https://leetcode.com/problems/find-k-closest-elements/
#
# Tags: Array - Two Pointers - Binary Search - Sorting - Heap (Priority Queue)

import timeit
from collections import deque
from typing import List


# Use binary search to find where x is, or should be if present, in the
# input array, once done, start adding elements from the ones
# surrounding that position based on the conditions given on the problem
# description.
#
# Time complexity: O(log(n) + k) - We can find the insertion position
# for n in log(n) time using binary search, then we add k elements in
# linear time to the result.
# Space complexity: O(k) - The queue will grow to size k.
#
# Runtime: 331 ms, faster than 88.09%
# Memory Usage: 15.7 MB, less than 27.45%
class BinarySearch:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Handle a few edge cases before going into the main logic.
        # If the value is lesser than any in the array, return the first
        # k values.
        if x <= arr[0]:
            return arr[:k]
        # If the value is greater than any in the array, return the last
        # k values.
        if arr[-1] <= x:
            return arr[-k:]
        # Now we know that the value would be in the array, use binary
        # search to find x or the nearest lesser value. Also initialize
        # the mid pointer to handle 2 element arrays.
        l, mid, r = 0, 0, len(arr) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            # If we have a hit.
            if arr[mid] == x:
                break
            if arr[mid] < x:
                l = mid
            else:
                r = mid
        # Mid could be pointing to the first value greater than x.
        while arr[mid] > x:
            mid -= 1
        # The mid index now points to x or the closest lesser value in
        # arr, use a double ended queue to append from both ends and
        # keep the result sorted.
        q = deque()
        # Initialize the left and right pointers to compare values.
        l, r = mid, mid + 1
        # Append elements while below k size.
        while len(q) < k:
            # Check to see if we are at the end of the input on the left.
            if l < 0:
                q.append(arr[r])
                r += 1
                continue
            # Check to see if we are at the end of the input on the right.
            if r >= len(arr):
                q.appendleft(arr[l])
                l -= 1
                continue
            # Compare the elements to see which one we should add.
            a, b = arr[l], arr[r]
            if abs(a - x) <= abs(b - x):
                q.appendleft(a)
                l -= 1
            else:
                q.append(b)
                r += 1
        # Cast the queue to a list.
        return list(q)


# The previous solution is correct but we can do better if we merge its
# two steps, finding where the result elements are located and getting
# them, into one step, we can binary search the left boundary of a
# window of size k.
#
# Time complexity: O(log(n-k) + k) - The binary search happens in
# O(log(n-k)), then we construct the result in k time because we are
# slicing the input.
# Space complexity; O(k) - The size of the output array. If we don't
# take the output into account, then O(1).
#
# Runtime: 770 ms, faster than 17.79%
# Memory Usage: 15.4 MB, less than 80.93%
class SlidingWindowBS:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # We are looking for the left boundary of a window of size k,
        # this can be the 0 to len(arr) -k position, initialize the
        # boundaries for the binary search of this left boundary.
        l, r = 0, len(arr) - k
        # Binary search.
        while l < r:
            # Find the mid point, we are checking this value as the left
            # boundary of the result window of size k.
            mid = (l + r) // 2
            # Check the conditions given on the description.
            # If the value under the left end of the window is further
            # from k than the value under the right end of the window,
            # slide the search window right.
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            # If the value under the right end of the window is as far,
            # or further, than the value under the left end of the
            # search window, slide the search window left.
            else:
                r = mid
        # Use the left pointer found to get the result from the input.
        return arr[l : l + k]


def test():
    executors = [
        BinarySearch,
        SlidingWindowBS,
    ]
    tests = [
        [[1, 3], 1, 2, [1]],
        [[1, 1, 1, 10, 10, 10], 1, 9, [10]],
        [[1, 2, 3, 4, 5], 3, 10, [3, 4, 5]],
        [[1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]],
        [[1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]],
        [[1, 2, 5, 6, 7, 8, 10], 3, 4, [2, 5, 6]],
        [[1, 1, 2, 2, 2, 2, 2, 3, 3], 3, 3, [2, 3, 3]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findClosestElements(t[0], t[1], t[2])
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
