# 378. Kth Smallest Element in a Sorted Matrix
# 🟠 Medium
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
#
# Tags: Array - Binary Search - Sorting - Heap (Priority Queue) - Matrix

import timeit
from collections import defaultdict
from heapq import heappush, heappushpop
from typing import List

# If the matrix is sorted by row and column and also the last element of
# each row is smaller than the first element of the next row, we could
# use div and mod to find the k-th smallest element.
#
# row, col = divmod(k - 1, len(matrix[0]))
# return matrix[row][col]

# Start at the smallest element and move to the next smallest, which
# will be either i+1 or j+1
# TODO could this solution work?
class Failing:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Base case, the smallest element is the top-left one.
        if k == 1:
            return matrix[0][0]
        # Create a dict of candidate next smallest elements and add
        # the element that we know to be the smallest.
        candidates = defaultdict(set)
        candidates[matrix[0][0]].add((0, 0))
        while k:
            k -= 1
            # Get the smallest key in the dictionary, the next smallest
            # value in the matrix.
            next_smallest = min(candidates)
            # Otherwise get the element row and col. There could be
            # multiple elements with the same value, if they are all
            # candidates, it does not matter which one we get.
            row, col = candidates[next_smallest].pop()
            # Remove this key if we have consumed all its elements.
            if not candidates[next_smallest]:
                del candidates[next_smallest]
            # If we are not on the last column, the element to the
            # right is a candidate.
            if col < len(matrix[0]) - 1:
                candidates[matrix[row][col + 1]].add((row, col + 1))
            # If we are not on the last row, the element below is a
            # candidate.
            if row < len(matrix) - 1:
                candidates[matrix[row + 1][col]].add((row + 1, col))

        return next_smallest


# Use a min heap of size k, push all matrix elements in, the result will
# be heap[0]
# We can optimize if we stop pushing row elements in once the elements
# value is > than heap[0]
#
# Time complexity: O(n*log(k)) - For each element we may replace the
# min element of the heap.
# Space complexity: O(k) - The heap has size k.
#
# Runtime: 227 ms, faster than 82.66%
# Memory Usage: 18.7 MB, less than 80.82%
class Heap:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Use a heap to store the k smallest elements.
        heap = []
        # Iterate over every element of the matrix.
        for row in matrix:
            for val in row:
                if len(heap) < k:
                    # If we have less than k elements, push.
                    heappush(heap, -val)
                else:
                    # Heap already has size k. push&pop
                    heappushpop(heap, -val)
        return -heap[0]


# TODO add the O(n), and a binary search O(n*log(n)) solution.


def test():
    executors = [
        Heap,
        # Failing,
    ]
    tests = [
        [[[3, 8, 8], [3, 8, 8], [3, 9, 13]], 8, 9],
        [[[1, 50, 90], [10, 51, 93], [12, 130, 175]], 4, 50],
        [[[1, 50, 90], [10, 51, 93], [12, 130, 175]], 3, 12],
        [[[1, 50, 90], [10, 51, 93], [12, 130, 175]], 9, 175],
        [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 1, 1],
        [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13],
        [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 3, 9],
        [[[-5]], 1, -5],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.kthSmallest(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
