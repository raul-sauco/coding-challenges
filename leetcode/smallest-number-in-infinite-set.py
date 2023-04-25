# 2336. Smallest Number in Infinite Set
# 🟠 Medium
#
# https://leetcode.com/problems/smallest-number-in-infinite-set/
#
# Tags: Hash Table - Design - Heap (Priority Queue)

import json
import os
import timeit
from heapq import heapify, heappop, heappush


# Use a heap to access the smallest element in O(log(n)) and a set to
# check whether a given element is found in the set in O(1). We use
# an array to implement the set because the number of elements is a
# maximum of 1000 and using and array will save us the hashing cost.
#
# Time complexity: O(n*log(m)) - Where n is the number of operations and
# m is the size of the object, since the size maxes out at 1000, it
# could be considered also O(n*log(1000)) ≈ O(n).
# Space complexity: O(m) - The object is instantiated with size 2*1000.
#
# Runtime 124 ms Beats 68.96%
# Memory 14.6 MB Beats 56.4%
class SmallestInfiniteSet:
    def __init__(self):
        self.nums = [x for x in range(1, 1001)]
        self.d = [True] * 1001
        heapify(self.nums)

    def popSmallest(self) -> int:
        if not self.nums:
            return -1
        self.d[self.nums[0]] = False
        return heappop(self.nums)

    def addBack(self, num: int) -> None:
        if not self.d[num]:
            self.d[num] = True
            heappush(self.nums, num)


# Keep track of numbers added and the minimum value above any removed
# one. This solution should be inefficient because it needs to iterate
# the entire set to find the minimum in pop. It turns out to be more
# efficient than the previous ones in the online Leetcode judge, but
# that is probably due to the tests.
#
# Time complexity: O(n*m) - Where n is the number of operations and
# m is the size of the object, on the pop, we need to find the minimum
# value on the set, which is linear time.
# Space complexity: O(n) - The will grow by one with each insert.
#
# Runtime 108 ms Beats 96.98%
# Memory 14.4 MB Beats 99.45%
class SmallestInfiniteSet2:
    def __init__(self):
        self.smallest = 1
        self.d = set()

    def popSmallest(self) -> int:
        if self.d:
            res = min(self.d)
            self.d.remove(res)
            return res
        self.smallest += 1
        return self.smallest - 1

    def addBack(self, num: int) -> None:
        if num < self.smallest:
            self.d.add(num)


# Optimize the pop operation on the previous solution using a heap. With
# big input sizes this solution should be more performant.
#
# Time complexity: O(n*log(m)) - Where n is the number of operations and
# m is the size of the object, since the size maxes out at 1000, it
# could be considered also O(n*log(1000)) ≈ O(n).
# Space complexity: O(m) - The can grow by one with each insert.
#
# Runtime 116 ms Beats 86.54%
# Memory 14.4 MB Beats 88.19%
class SmallestInfiniteSet3:
    def __init__(self):
        self.smallest = 1
        self.d = set()
        self.h = []

    def popSmallest(self) -> int:
        if self.d:
            res = heappop(self.h)
            self.d.remove(res)
            return res
        self.smallest += 1
        return self.smallest - 1

    def addBack(self, num: int) -> None:
        # Ignore numbers already in the object.
        if num < self.smallest and num not in self.d:
            self.d.add(num)
            heappush(self.h, num)


def test():
    executors = [
        SmallestInfiniteSet,
        SmallestInfiniteSet2,
        SmallestInfiniteSet3,
    ]
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    filename = os.path.splitext(os.path.basename(__file__))[0] + ".json"
    with open(os.path.join(__location__, filename)) as json_file:
        tests = json.load(json_file)
        for executor in executors:
            start = timeit.default_timer()
            for _ in range(1):
                for col, t in enumerate(tests):
                    # The first element is an empty array
                    sol = executor()
                    for i in range(1, len(t[0])):
                        call = t[0][i]
                        if call == "addBack":
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
