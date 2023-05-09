# Merge Sorted Arrays
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/merge-sorted-arrays
#
# Tags: Array - Sorting - Divide And Conquer

import timeit
from heapq import heapify, heappop, heappush


# Use a heap to store the first unused element of each array together
# with its position in the array and the array position in the input.
# This gives us all the smallest unpicked elements in a heap, which lets
# us pick the next smallest element in O(log(k)) where k is the number
# of lists in the input, and also the number of elements in the heap.
# When we pop an element out of the heap, we add it to the result, since
# we know that it is the next smallest element, and we check if the list
# it came from has any more element, if it does, we add the next element
# to the heap.
#
# Time complexity: O(n*log(k)+k) - We pop n elements from the heap at a
# cost of log(k) each, we also build a list with the first item on each
# list at a cost of k.
# Space complexity: O(k+n) - Where k is the number of lists in the input
# and n is the total number of elements in the input. The heap has size
# k and the result array that we build gradually has size n.
class Solution:
    def heapSort(self, array):
        heap = [(array[i][0], 0, i) for i in range(len(array))]
        heapify(heap)
        res = []
        while heap:
            val, pos, list_index = heappop(heap)
            res.append(val)
            # If the list that this element came from still has elements
            # add the next one to the heap.
            if pos < len(array[list_index]) - 1:
                heappush(
                    heap, (array[list_index][pos + 1], pos + 1, list_index)
                )
        return res


def test():
    executors = [Solution]
    tests = [
        [
            [[1, 5, 9, 21], [-1, 0], [-124, 81, 121], [3, 6, 12, 20, 150]],
            [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150],
        ],
        [
            [
                [-92, -78, -68, 43, 46, 46, 79, 79],
                [-66, -49, -26, -16, 21, 28, 33, 50],
                [-40, -8, 12, 20, 36, 38, 81],
                [-76, -74, -62, -46, -23, 33, 42, 48, 55, 94],
            ],
            # fmt: off
            [
                -92, -78, -76, -74, -68, -66, -62, -49, -46, -40, -26, -23,
                -16, -8, 12, 20, 21, 28, 33, 33, 36, 38, 42, 43, 46, 46, 48,
                50, 55, 79, 79, 81, 94
            ],
            # fmt: on
        ],
        [
            [
                [-93, -83, -43, -32, -32, -15, -14, 12, 78, 80],
                [-83],
                [-82, -51, -29, 40, 60, 76, 80],
                [50],
                [-33, -16],
                [-100],
                [-33, -11, 23, 29, 29, 43],
                [0, 70],
                [-57, -43, -41, -18, -5, 74],
            ],
            # fmt: off
            [
                -100, -93, -83, -83, -82, -57, -51, -43, -43, -41, -33, -33,
                -32, -32, -29, -18, -16, -15, -14, -11, -5, 0, 12, 23, 29,
                29, 40, 43, 50, 60, 70, 74, 76, 78, 80, 80,
            ],
            # fmt: on
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.heapSort(t[0])
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
