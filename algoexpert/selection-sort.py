# Selection Sort
# 🟢 Easy
#
# https://www.algoexpert.io/questions/selection-sort
#
# Tags: Selection Sort

import timeit


# Sort the input using the selection sort algorithm.
#
# Time complexity: O(n^2) - For each element in the input, we scan the
# entire input looking for the smallest element to swap it with.
# Space complexity: O(1) - No extra space is used.
class Solution:
    def selectionSort(array):
        # The array is sorted up to i-1, place the next
        # smaller item at index i.
        for i in range(len(array)):
            smallest_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[smallest_index]:
                    smallest_index = j
            # Swap the elements in place.
            array[i], array[smallest_index] = array[smallest_index], array[i]
        return array


def test():
    executors = [Solution]
    tests = [
        [[1], [1]],
        [[3, 1, 2], [1, 2, 3]],
        [[8, 5, 2, 9, 5, 6, 3], [8, 5, 2, 9, 5, 6, 3]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.selectionSort(t[0])
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
