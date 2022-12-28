# 1962. Remove Stones to Minimize the Total
# 🟠 Medium
#
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/
#
# Tags: Array - Heap (Priority Queue)

import timeit
from heapq import heapify, heapreplace
from typing import List


# Use a heap, ideally a maximum heap, but in Python we can use a minimum
# heap with negated values to remove half of the stones from the largest
# pile at each step.
#
# Time complexity: O(k*log(n)) - We copy and heapify the input array at
# O(n), then iterate over it k times pushing and popping from the heap
# at O(log(n)) cost.
# Space complexity: O(n) - The values heap has the same size as the
# input. If we can mutate the input, we could use that array and reduce
# the complexity to O(1) extra memory.
#
# Runtime 1604 ms Beats 100%
# Memory 28.6 MB Beats 44.43%
class PriorityQueue:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        vals = [-x for x in piles]
        heapify(vals)
        for _ in range(k):
            heapreplace(vals, vals[0] // 2)
        return -sum(vals)


# Use bucket sort, create an array of size 10^4
#
# Time complexity: O(k*log(n)) - We copy and heapify the input array at
# O(n), then iterate over it k times pushing and popping from the heap
# at O(log(n)) cost.
# Space complexity: O(n) - The values heap has the same size as the
# input. If we can mutate the input, we could use that array and reduce
# the complexity to O(1) extra memory.
#
# Runtime 1404 ms Beats 100%
# Memory 28.3 MB Beats 92.80%
class BucketSort:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Create an array of buckets where we will place the number of
        # piles with that number of elements on them.
        buckets = [0] * 10001
        # The value of the greatest pile and the total sum.
        i = total = 0
        # Store the number of piles of each size on the buckets.
        for j in range(len(piles)):
            buckets[piles[j]] += 1
            if piles[j] > i:
                i = piles[j]
            total += piles[j]
        # Iterate back over the buckets staying at the biggest pile.
        while k and i > 1:
            # If we have cleared all piles size i, move onto the next
            # greatest size.
            if buckets[i] == 0:
                i -= 1
                continue
            # This is the number of elements we need to remove from the
            # current pile of size i.
            removed = i // 2
            # The size of the remaining pile after we remove the
            # elements is j.
            j = i - removed
            # After the update, we have one less pile of size i, one
            # more of size j.
            buckets[j] += 1
            buckets[i] -= 1
            # After the update we have `removed` less elements.
            total -= removed
            # We have consumed one update.
            k -= 1
        return total


def test():
    executors = [
        PriorityQueue,
        BucketSort,
    ]
    tests = [
        [[5, 4, 9], 2, 12],
        [[10000], 10000, 1],
        [[4, 3, 6, 7], 3, 12],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minStoneSum(t[0], t[1])
                exp = t[2]
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
