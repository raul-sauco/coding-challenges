# Merge Sort
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/merge-sort
#
# Tags: Design - Sorting - Merge Sort

import timeit
from typing import List


# Start with a non optimal solution that copies the array every time it
# splits it and merges it.
#
# Time complexity: O(n*log(n)) - This could actually be higher if
# slicing the array takes O(n) per call.
# Space complexity; O(n)? - Python garbage collection supposedly cleans
# after each call, at any one time, the call stack will be using:
# O(n) + O(n/2) + O(n/4) + O(n/8) ... => O(2n) => O(n) space, instead of
# the O(n*log(n)) that intuitively could seem.
class Naive:
    def mergeSort(self, array: List[int]) -> List[int]:
        # If the array has only one element, it is trivially merged.
        if len(array) < 2:
            return array
        # Define a function that merges two sorted arrays into one.
        def merge(a: List[int], b: List[int]) -> List[int]:
            # Initialize the result array to avoid list expansion.
            res = [None] * (len(a) + len(b))
            # Initialize the pointers.
            i = j = 0
            # While we still have elements in both arrays, pick the
            # smallest element, if they are the same, pick the element
            # in a to preserve natural ordering.
            while i < len(a) and j < len(b):
                if b[j] < a[i]:
                    res[i + j] = b[j]
                    j += 1
                else:
                    res[i + j] = a[i]
                    i += 1
            # We have exhausted one of the lists, use the other one.
            while i < len(a):
                res[i + j] = a[i]
                i += 1
            while j < len(b):
                res[i + j] = b[j]
                j += 1
            # Return the result.
            return res

        # Otherwise, mergeSort each half and then merge them together.
        mid = len(array) // 2
        return merge(self.mergeSort(array[:mid]), self.mergeSort(array[mid:]))


# Use pointers to determine the section of the array that we are sorting
# instead of slicing the array. This reduces both the time and space
# complexity because array slicing leads to copies of the array made in
# O(n) time and using O(n) space.
#
# Time complexity: O(n*log(n)) - Merge sort complexity without the extra
# work derived from slicing the array.
# Space complexity: O(n) - We only make one copy of the array using O(n).
#
# This solution does not include type declarations because they
class Pointers:
    # Define a function that sorts, using the merge sort algorithm, a
    # section of array a between left and right pointers.
    def helper(self, a: List[int], left: int, right: int, b: List[int]):
        # Base case, the single element is trivially sorted.
        if left == right:
            return
        # If we haven't reached the base case, divide and conquer.
        mid = left + ((right - left) // 2)
        # Sort each half of the array in the auxiliary array at this
        # call level, this alternates sorting between the main and
        # auxiliary array.
        self.helper(b, left, mid, a)
        self.helper(b, mid + 1, right, a)
        # Merge the two sorted array sections into one.
        self.merge(a, left, mid, right, b)

    def merge(
        self, a: List[int], left: int, mid: int, right: int, b: List[int]
    ):
        # Define two pointers used to read b and one used to write to a.
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            # Check which element is smaller.
            # The sorted sections are in the auxiliary array.
            if b[j] < b[i]:
                a[k] = b[j]
                j += 1
            else:
                a[k] = b[i]
                i += 1
            # Always moke the write pointer forward.
            k += 1
        # Use up the remaining elements in either section of b.
        while i <= mid:
            a[k] = b[i]
            i += 1
            k += 1
        while j <= right:
            a[k] = b[j]
            j += 1
            k += 1

    # Method publicly exposed, consumers should call this method with
    # an array to get the sorted version of that array.
    # The method uses Merge Sort at O(n*log(n)) cost.
    def mergeSort(self, array: List[int]):
        # Base case.
        if len(array) < 2:
            return array
        # Initial call passing the input array and a copy. These two
        # arrays will be used alternately by the helper function to
        # sort sections of the array and merge them into the other array
        # to form longer sorted sections.
        self.helper(array, 0, len(array) - 1, array[:])
        return array


def test():
    executors = [
        Naive,
        Pointers,
    ]
    tests = [
        [[], []],
        [[1], [1]],
        [[1, 2, 3], [1, 2, 3]],
        [[3, 2, 1], [1, 2, 3]],
        [
            [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1],
            [-10, -6, -5, -5, -4, -4, -4, -2, -1, 3, 5, 5, 8, 10],
        ],
        [
            [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8],
            [-10, -10, -9, -7, -7, -6, -5, -2, 2, 2, 3, 3, 4, 5, 8, 8, 9, 10],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1000):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.mergeSort(t[0])
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
