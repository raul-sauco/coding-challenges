# 912. Sort an Array
# 🟠 Medium
#
# https://leetcode.com/problems/sort-an-array/
#
# Tags: Array - Divide and Conquer - Sorting - Heap (Priority Queue)
# - Merge Sort - Bucket Sort - Radix Sort - Counting Sort

import timeit
from typing import List


# Given the conditions of the problem description, merge sort seems to
# be a good option, it won't use any extra memory and it guarantees
# O(n*log(n)) time complexity.
#
# Time complexity: O(n*log(n))
# Space complexity: O(n) - We use one copy of the input array to
# alternately move elements from one to the other. The call stack will
# be of height log(n), that is an extra O(log(n)).
#
# Runtime 1690 ms Beats 72.17%
# Memory 21.4 MB Beats 90.91%
class MergeSort:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Define an internal function that sorts a section of the input
        # array to avoid passing copies of the array between calls.
        def mergeSort(a: List[int], b: List[int], l: int, r: int) -> None:
            # Base case, the array has only one element.
            if l == r:
                return
            mid = l + ((r - l) // 2)
            # Swap the function of each array in each call level.
            mergeSort(b, a, l, mid)
            mergeSort(b, a, mid + 1, r)
            merge(a, b, l, mid, r)

        def merge(destination, source, l, mid, r):
            # The halves are sorted, merge them. Define i and j, two
            # read pointers that read the next unused element in each of
            # the sorted halves, and one insert pointer of the index at
            # which we want to insert the next value in the result.
            i, j, ins = l, mid + 1, l
            while i <= mid and j <= r:
                if source[j] < source[i]:
                    destination[ins] = source[j]
                    j += 1
                else:
                    destination[ins] = source[i]
                    i += 1
                ins += 1
            # Use up any remaining elements from either half.
            while i <= mid:
                destination[ins] = source[i]
                i += 1
                ins += 1
            while j <= r:
                destination[ins] = source[j]
                j += 1
                ins += 1

        # A copy of the input array that we use to alternate between
        # sorted and unsorted sections.
        helper = nums[:]
        mergeSort(nums, helper, 0, len(nums) - 1)
        return nums


def test():
    executors = [
        MergeSort,
    ]
    tests = [
        [[0], [0]],
        [[1, 0], [0, 1]],
        [[5, 2, 1], [1, 2, 5]],
        [[5, 2, 3, 1], [1, 2, 3, 5]],
        [[5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.sortArray(t[0])
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
