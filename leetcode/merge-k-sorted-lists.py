# 23. Merge k Sorted Lists
# 🔴 Hard
#
# https://leetcode.com/problems/merge-k-sorted-lists/
#
# Tags: Linked List - Divide and Conquer - Heap (Priority Queue) -
# Merge Sort

import timeit
from heapq import heapify, heappop, heappushpop
from typing import List, Optional

from data import LinkedList, ListNode

# 10e3 calls
# » Tuples              0.00998   seconds
# » ComparableNodes     0.01333   seconds
# » DaCIterative        0.01009   seconds
# » DaCRecursive        0.00994   seconds

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Use a min heap to store the heads of all the lists, carefully handling
# edge cases like no lists and empty lists. Use a dummy node as the head
# of the result and start appending the elements we pop from the heap
# to the result linked list, when we pop an element, if it has a next,
# we push it into the heap. Since we are popping the heads of sorted
# lists from a heap, they will be sorted in non-descending order.
#
# Time complexity: O(m*log(n)) - Where m is the combined number of
# elements in all the heaps and m is the number of lists, which will be
# the number of nodes in the heap.
# Space complexity: O(m) - The heap will have m elements.
#
# Runtime: 215 ms, faster than 44.57%
# Memory Usage: 18.1 MB, less than 38.26%
class Tuples:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # Base case, no lists.
        if not lists:
            return None
        # Create a list of tuples (val, ListNode)
        tuples = [
            (lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]
        ]
        # Heapify the tuples in O(n)
        heapify(tuples)
        # Use a dummy node as the temp head.
        head = current = ListNode()
        # Use a tie-breaker index.
        tb = len(lists)
        while tuples:
            _, _, top = tuples[0]
            # If the top node on the heap has a next, push&pop.
            if top.next:
                next = top.next
                tb += 1
                _, _, current.next = heappushpop(tuples, (next.val, tb, next))
            # If the top node is the last node of its list, just pop.
            else:
                _, _, current.next = heappop(tuples)
            # Shift the pointer.
            current = current.next
        return head.next


# Improve the solution above using comparable nodes that can be added
# and popped directly from the heap. This gives a much easier to read
# solution.
#
# Time complexity: O(m*log(n)) - Where m is the combined number of
# elements in all the heaps and m is the number of lists, which will be
# the number of nodes in the heap.
# Space complexity: O(m) - The heap will have m elements.
#
# Runtime: 214 ms, faster than 45.53%
# Memory Usage: 17.7 MB, less than 61.11%
class ComparableNodes:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # Base case, no lists, gets handled automatically, head.next
        # will always be None.
        # Extending ListNode does not work because the nodes are
        # constructed in code outside this scope. Instead dynamically
        # add the required functionality.
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        # Create a list of comparable nodes, skip null roots.
        heap = [root for root in lists if root]
        # Heapify the tuples in O(n)
        heapify(heap)
        # Use a dummy node as the temp head.
        head = current = ListNode()
        while heap:
            top = heap[0]
            # If the top node on the heap has a next, push&pop else pop.
            current.next = (
                heappushpop(heap, (top.next)) if top.next else heappop(heap)
            )
            # Shift the pointer.
            current = current.next
        return head.next


# A divide and conquer approach will merge lists two at a time, it will
# result in m//2 number of lists of average double the length, we keep
# doing this until we only have one list and return that list,
# effectively reducing the problem to multiple instances of merge 2
# sorted lists.
#
# Time complexity: O(n*log(m)) - With n the number of items and m the
# initial number of lists, on each step we run over all the items in
# two lists and we halve the number of lists at each step.
# Space complexity: O(1) - If we don't take into account input/output
# list nodes.
#
# Runtime: 253 ms, faster than 28.23%
# Memory Usage: 17.6 MB, less than 93.45%
class DaCIterative:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # Base case, we don't have any lists.
        if not lists:
            return None
        # Base case, there is only one list in the input, since the
        # lists are sorted, the input is sorted, return it unchanged.
        if len(lists) == 1:
            return lists[0]
        # If we have 2 or more lists, recursively divide the input into
        # two halves and merge them, notice that if we only have two
        # lists, the recursive calls will return without doing anything.
        mid = len(lists) // 2
        l1, l2 = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        # Once we know that we only have two lists, merge them.
        return self.merge(l1, l2)

    # This is equivalent to merge-two-sorted-lists.py
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Use a dummy node as the head.
        head = temp = ListNode()
        # Iterate over the input lists.
        while l1 and l2:
            # Choose the smaller value node and move that pointer.
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        # Once we exhaust one of the lists, append the remaining nodes
        # to the end of the result list.
        temp.next = l1 or l2
        # Remove the dummy node and return the next node as the head.
        return head.next


# Similar to the previous version but using the recursive algorithm to
# merge two lists.
#
# Runtime: 245 ms, faster than 31.08%
# Memory Usage: 26.4 MB, less than 5.15%
class DaCRecursive:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # Base case, we don't have any lists.
        if not lists:
            return None
        # Base case, there is only one list in the input, since the
        # lists are sorted, the input is sorted, return it unchanged.
        if len(lists) == 1:
            return lists[0]
        # If we have 2 or more lists, recursively divide the input into
        # two halves and merge them, notice that if we only have two
        # lists, the recursive calls will return without doing anything.
        mid = len(lists) // 2
        l1, l2 = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        # Once we know that we only have two lists, merge them.
        return self.merge(l1, l2)

    # This is equivalent to merge-two-sorted-lists.py
    def merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # If one of the lists is empty, return the other one.
        if not l1 or not l2:
            return l1 or l2
        # Choose the node with the smaller value as the head of the
        # partial result, add the result of recursively calling merge
        # two lists with this node removed as its next and return that.
        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        l2.next = self.merge(l1, l2.next)
        return l2


def test():
    executors = [
        Tuples,
        ComparableNodes,
        DaCIterative,
        DaCRecursive,
    ]
    tests = [
        [[], []],
        [[[]], []],
        [[[1, 2, 2], [1, 1, 2]], [1, 1, 1, 2, 2, 2]],
        [
            [[1, 4, 5], [1, 3, 4], [2, 6]],
            [1, 1, 2, 3, 4, 4, 5, 6],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                lists = [LinkedList.fromList(l).head for l in t[0]]
                result = sol.mergeKLists(lists)
                result = LinkedList(result).toList()
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
