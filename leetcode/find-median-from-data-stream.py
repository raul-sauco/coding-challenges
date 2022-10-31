# 295. Find Median from Data Stream
# 🔴 Hard
#
# https://leetcode.com/problems/find-median-from-data-stream/
#
# Tags: Two Pointers - Design - Sorting - Heap (Priority Queue) - Data Stream

import timeit
from heapq import heappop, heappush

from sortedcontainers import SortedList

# 10e3 calls.
# » MedianFinder        0.01528   seconds
# » UseSortedList       0.02331   seconds

# Use two heaps, a min heap for numbers greater than the median and a
# max heap for numbers smaller than the median, keep them balanced with
# at most 1 element difference between them, when we need to produce the
# median, if one heap has more elements than the other, the median will
# be the element at index 0 on the heap with more elements. If they both
# have the same number of elements, the median will be the mean between
# the elements at index 0 in both heaps.
#
# Time complexity: O(n*log(n)) - Adding an element takes amortized
# log(n) where n is the number of elements currently in the heap.
# Finding the median happens in O(1).
# Space complexity: O(n) - Where n is the number of elements in the
# MedianFinder, each element is stored in one of the heaps.
#
# Runtime: 656 ms, faster than 83.45%
# Memory Usage: 36.2 MB, less than 44.70%
class MedianFinder:
    def __init__(self):
        # Use two heaps, a max heap for values below the median, a min
        # heap for values above the median.
        self.below = []
        self.above = []

    def addNum(self, num: int) -> None:
        # Push into the above heap.
        heappush(self.above, num)
        # Move to the below heap all values that need to be moved.
        while self.above and self.below and self.above[0] < -self.below[0]:
            heappush(self.below, -heappop(self.above))
        # Equalize the heaps.
        while len(self.below) - len(self.above) > 1:
            heappush(self.above, -heappop(self.below))
        while len(self.above) - len(self.below) > 1:
            heappush(self.below, -heappop(self.above))

    def findMedian(self) -> float:
        # If both heaps have the same number of items, return the mean.
        if len(self.below) == len(self.above):
            return (-self.below[0] + self.above[0]) / 2
        # Otherwise check which heap has more elements.
        if len(self.below) > len(self.above):
            return -self.below[0]
        return self.above[0]


# Use a sorted list to store the element.
# https://grantjenks.com/docs/sortedcontainers/sortedlist.html
#
# Time complexity: O(n*log(n)) - Insertion takes approximately
# O(log(n)) according to the documentation, finding the median is O(1).
# Space complexity: O(n) - We store all elements.
#
# Runtime: 831 ms, faster than 75.70%
# Memory Usage: 36.8 MB, less than 5.15%
class UseSortedList:
    def __init__(self):
        # Use two heaps, a max heap for values below the median, a min
        # heap for values above the median.
        self.elements = SortedList()

    def addNum(self, num: int) -> None:
        self.elements.add(num)

    def findMedian(self) -> float:
        if len(self.elements) % 2:
            return self.elements[len(self.elements) // 2]
        i = len(self.elements) // 2
        return (self.elements[i] + self.elements[i - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


def test():
    executors = [
        MedianFinder,
        UseSortedList,
    ]
    tests = [
        [
            [
                "MedianFinder",
                "addNum",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
            ],
            [[], [1], [2], [], [3], []],
            [None, None, None, 1.5, None, 2.0],
        ],
        [
            [
                "MedianFinder",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
            ],
            [[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []],
            [
                None,
                None,
                -1.00000,
                None,
                -1.50000,
                None,
                -2.00000,
                None,
                -2.50000,
                None,
                -3.00000,
            ],
        ],
        [
            [
                "MedianFinder",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
            ],
            [
                [],
                [6],
                [],
                [10],
                [],
                [2],
                [],
                [6],
                [],
                [5],
                [],
                [0],
                [],
                [6],
                [],
                [3],
                [],
                [1],
                [],
                [0],
                [],
                [0],
                [],
            ],
            [
                None,
                None,
                6.00000,
                None,
                8.00000,
                None,
                6.00000,
                None,
                6.00000,
                None,
                6.00000,
                None,
                5.50000,
                None,
                6.00000,
                None,
                5.50000,
                None,
                5.00000,
                None,
                4.00000,
                None,
                3.00000,
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                # The capacity comes wrapped in an array, unwrap it.
                sol = executor()
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    if call == "addNum":
                        result = getattr(sol, call)(t[1][i][0])
                    else:
                        result = getattr(sol, call)()
                    exp = t[2][i]
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
