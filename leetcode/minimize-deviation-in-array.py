# 1675. Minimize Deviation in Array
# 🔴 Hard
#
# https://leetcode.com/problems/minimize-deviation-in-array/
#
# Tags: Array - Greedy - Heap (Priority Queue) - Ordered Set

import timeit
from heapq import heapify, heappushpop
from typing import List


# The problem lets us do two operations on the input array elements,
# for even numbers, it lets us divide them by 2 as long as they remain
# even, for odd numbers, we can multiply them by 2 once, then they
# become even. To simplify the problem, we can start by multiplying all
# odd values by 2, that way each element is at the maximum it can be,
# and them pushing them all into a max heap after checking the value
# of the smallest item in the heap. While we can make the biggest
# current element smaller, that is while the top of the heap is even,
# and we can divide it by 2, we will pop that element and compute the
# current difference between it and the smallest element currently in
# the heap, if the gap is the smallest seen so far, we will record it as
# the temporary result, then we divide the value by 2 and push it back
# into the heap. When we find an odd element as the top of the heap, we
# know that we cannot make it any smaller and so we can stop iterating.
#
# Time complexity: O(n*log(n)) - We may pop and push all elements in the
# input array a certain number of times t, t has a logarithmic relation
# to the value of the element and its upper bound is 30 because of
# log2(10^9), therefore time complexity is n*30*log(n) and we can
# simplify it.
# Space complexity: O(n) - The heap will have the same size as nums.
#
# Runtime 1383 ms Beats 82.61%
# Memory 21.3 MB Beats 97.10%
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Simplify the operations that we can do in the numbers by
        # doubling them all and inserting them into a max heap.
        heap = [-x * 2 if x % 2 else -x for x in nums]
        heapify(heap)
        # Keep tabs on the smallest value that we have seen.
        smallest = max(heap)
        res = float("inf")
        # Pop from the heap while we can make the top element smaller by
        # dividing it by 2.
        while heap and not heap[0] % 2:
            # The maximum current gap is the difference between the
            # smallest element we have seen so far and the biggest one
            # currently in the max heap, the top element.
            # res = min(res, smallest - heap[0])
            if smallest - heap[0] < res:
                res = smallest - heap[0]
            # Divide the current top of the heap by 2, check if that
            # makes it the smallest element that we have seen, and push
            # it back into the heap.
            val = heap[0] // 2
            if val > smallest:
                smallest = val
            heappushpop(heap, val)
        return min(res, smallest - heap[0])


def test():
    executors = [Solution]
    tests = [
        [[10, 4, 3], 2],
        [[2, 10, 8], 3],
        [[1, 2, 3, 4], 1],
        [[4, 1, 5, 20, 3], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimumDeviation(t[0])
                exp = t[1]
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
