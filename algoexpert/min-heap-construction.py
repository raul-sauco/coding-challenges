# Min Heap Construction
# 🟠 Medium
#
# https://www.algoexpert.io/questions/min-heap-construction
#
# Tags: Heap (Priority Queue)

import timeit
from typing import List


# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeapRecursive:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # Heapify assumes that the leaves are correct heaps and starts
    # building heaps from the first non-leaf node in reverse to the
    # root node.
    # Time complexity: O(n)
    # Space O(log(n)) - The call could potentially reach the height of
    # the binary heap.
    def buildHeap(self, array):
        for i in range(len(array) // 2 - 1, -1, -1):
            self.siftDown(array, i)
        return array

    # Time complexity: O(log(n))
    # Space O(log(n)) - recursive call
    def siftDown(self, arr: List[int], i: int):
        smallest, l, r = i, 2 * i + 1, 2 * i + 2
        # If left child is smaller than root.
        if l < len(arr) and arr[l] < arr[smallest]:
            smallest = l
        # If right child is smaller than smallest so far.
        if r < len(arr) and arr[r] < arr[smallest]:
            smallest = r
        # If largest is not root, swap their position.
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            # Recursively heapify the affected left or right sub-tree.
            self.siftDown(arr, smallest)

    # Time complexity: O(log(n))
    # Space O(log(n)) - recursive call
    def siftUp(self, arr: List[int], i: int):
        parent_idx = (i - 1) >> 1
        if arr[parent_idx] > arr[i]:
            arr[i], arr[parent_idx] = arr[parent_idx], arr[i]
            self.siftUp(arr, parent_idx)
        return arr

    # Time complexity: O(1)
    # Space O(1)
    def peek(self):
        return self.heap[0]

    # Time complexity: O(log(n))
    # Space O(log(n))
    def remove(self):
        val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftDown(self.heap, 0)
        return val

    # Time complexity: O(log(n))
    # Space O(log(n))
    def insert(self, value):
        self.heap.append(value)
        self.heap = self.siftUp(self.heap, len(self.heap) - 1)


def test():
    executors = [
        MinHeapRecursive,
    ]
    tests = [
        [
            [
                "MinHeap",
                "insert",
                "peek",
                "remove",
                "peek",
                "remove",
                "peek",
                "insert",
                "remove",
                "remove",
                "remove",
                "peek",
            ],
            [
                [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41],
                [76],
                [],
                [],
                [],
                [],
                [],
                [83],
            ],
            [None, None, -5, -5, 2, 2, 6, None, 6, 7, 8, 8],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor(t[1][0])
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    if call == "insert":
                        argument = t[1][i][0]
                        result = getattr(sol, call)(argument)
                    else:
                        result = getattr(sol, call)()
                    exp = t[2][i]
                    assert result == exp, (
                        f"\033[93m» {result} <> {exp}\033[91m for"
                        + f" test {col}.{i} {call}({argument}) using "
                        + f"\033[1m{executor.__name__}"
                    )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
