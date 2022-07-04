# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import List
from heapq import heapify, heappush, heappushpop


# Runtime: 163 ms, faster than 41.37% of Python3 online submissions for Kth Largest Element in a Stream.
# Memory Usage: 18.2 MB, less than 62.66 % of Python3 online submissions for Kth Largest Element in a Stream.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Store the k value
        self.k = k
        # Sorting and trimming the list is quicker than popping from the heap
        # while it is bigger than k
        if len(nums) > k:
            nums.sort(reverse=True)
            nums = nums[:k]
        heapify(nums)
        self.heap = nums

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappushpop(self.heap, val)
        return self.heap[0]

        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)


def test():
    sol = KthLargest(3, [4, 5, 8, 2])
    assert sol.add(3) == 4
    assert sol.add(5) == 5
    assert sol.add(10) == 5
    assert sol.add(9) == 8
    assert sol.add(4) == 8

    sol = KthLargest(1, [])
    assert sol.add(-3) == -3
    assert sol.add(-2) == -2
    assert sol.add(-4) == -2
    assert sol.add(0) == 0
    assert sol.add(4) == 4

# [[1,[]],[-3],[-2],[-4],[0],[4]]


test()
