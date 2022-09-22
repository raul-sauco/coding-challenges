# 21. Merge Two Sorted Lists
# 🟢 Easy
#
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# Tags: Linked List - Recursion

import timeit
from typing import Optional

from data import LinkedList

# 1e4 calls
# » Iterative           0.04869   seconds
# » Recursive           0.04495   seconds


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Use a dummy node as the start of the result list, iterate over the
# nodes in both list, at each step, choose the node with the smaller
# vale and move that pointer forward.
#
# Time complexity: O(n) - Where n is the combined number of nodes in
# both lists, we will visit each node once.
# Space complexity: O(1) - Constant extra space used.
#
# Runtime: 40 ms, faster than 89.68%
# Memory Usage: 14 MB, less than 32.07%
class Iterative:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Use a dummy node as the head.
        head_pointer = temp = ListNode()
        # Iterate over the input lists.
        while list1 is not None and list2 is not None:
            # Choose the smaller value node and move that pointer.
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        # Once we exhaust one of the lists, append the remaining nodes
        # to the end of the result list.
        temp.next = list1 or list2
        # Remove the dummy node and return the next node as the head.
        return head_pointer.next


# Select the lower value node in the input and recursively call the
# function with that node removed from its list.
#
# Time complexity: O(n) - We process each node once.
# Space complexity: O(n) - The call stack will grow linearly with the
# size of the input.
#
# Runtime: 70 ms, faster than 33.31%
# Memory Usage: 13.8 MB, less than 98.78%
class Recursive:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # If one of the lists is empty, return the other one.
        if not list1 or not list2:
            return list1 or list2
        # Choose the node with the smaller value as the head of the
        # partial result, add the result of recursively calling merge
        # two lists with this node removed as its next and return that.
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def test():
    executors = [
        Iterative,
        Recursive,
    ]
    tests = [
        [[], [], []],
        [[], [0], [0]],
        [[1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head1 = LinkedList.fromList(t[0]).head
                head2 = LinkedList.fromList(t[1]).head
                result = LinkedList(sol.mergeTwoLists(head1, head2)).toList()
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
