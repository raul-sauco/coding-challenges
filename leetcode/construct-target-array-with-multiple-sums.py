# https://leetcode.com/problems/construct-target-array-with-multiple-sums/


import timeit
from heapq import heapify, heappushpop
from typing import List


# Use a heap to keep track of the biggest element.
# The two hints on the exercise description are very helpful, even more so the discussion about using % instead of `-`
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510256/JavaC%2B%2BPython-Backtrack-OJ-is-wrong
#
# When the max value is significantly larger than the sum of the rest of the values, we end up iterating the loop too many
# times, that can be avoided using the modulus operation due to the fact that:
# max-n*(a1+a2) = max % (a1+a2)
#
# Runtime: 345 ms, faster than 61.18% of Python3 online submissions for Construct Target Array With Multiple Sums.
# Memory Usage: 19.9 MB, less than 55.29 % of Python3 online submissions for Construct Target Array With Multiple Sums.
class HeapAndModulus:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        # Reverse the sign of all elements
        heap = [-1 * x for x in target]
        # heapify O(n) performs better than individually pushing into the heap O(n*log(n))
        heapify(heap)
        while True:
            prev = -heap[0]
            s -= prev
            # If the maximum value in the heap is 1 or the remaining sum is 1, we are done
            if prev == 1 or s == 1:
                return True
            # Check if we have reached a dead end
            if prev < s or s == 0 or prev % s == 0:
                return False
            # Calculate the value to be pushed into the heap and push it
            prev %= s
            heappushpop(heap, -prev)
            # Update the current sum of the values in the array/heap
            s += prev


# This solution is almost the same but runs slower because we are using `-` instead of `%`
class Heap:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        # Reverse the sign of all elements
        heap = [-1 * x for x in target]
        # heapify O(n) performs better than individually pushing into the heap O(n*log(n))
        heapify(heap)
        while True:
            prev = -heap[0]
            s -= prev
            # If the maximum value in the heap is 1 or the remaining sum is 1, we are done
            if prev == 1 or s == 1:
                return True
            # Check if we have reached a dead end
            if prev < s or s == 0 or prev - s == 0:
                return False
            # Calculate the value to be pushed into the heap and push it
            prev -= s
            heappushpop(heap, -prev)
            # Update the current sum of the values in the array/heap
            s += prev


def test():
    executor = [
        {'executor': HeapAndModulus, 'title': 'HeapAndModulus', },
        {'executor': Heap, 'title': 'Heap', },
    ]
    tests = [
        [[1], True],
        [[1, 1, 1, 2], False],
        [[1, 1, 2], False],
        [[1, 2], True],
        [[1, 1000000000], True],
        [[2], False],
        [[5, 50], False],
        [[8, 5], True],
        [[9, 3, 5], True],
        [[12, 5], True],
        [[13, 5], True],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.isPossible([*t[0]])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
