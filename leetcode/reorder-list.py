# 143. Reorder List
# 🟠 Medium
#
# https://leetcode.com/problems/reorder-list/
#
# Tags: Linked List - Two Pointers - Stack - Recursion

import timeit
from collections import deque
from typing import Optional

from data import ListNode, deserializeListToLinkedList, serializeLinkedList


# If we can use extra memory, store all nodes in a deque and pop
# alternatively from left/right reconnecting the nodes.
#
# Time complexity: O(n) - We travel through the linked list, then the deque.
# Space complexity: O(n) - We store all ListNodes in the deque.
#
# Runtime 56 ms Beats 54%
# Memory 24.86 MB Beats 5%
class Deque:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        deq = deque()
        current = head.next
        while current:
            deq.append(current)
            current = current.next

        i = 0
        current = head
        while deq:
            current.next = deq.popleft() if i % 2 else deq.pop()
            current = current.next
            i += 1
        # The last element should not point to anything
        current.next = None


# If are not allowed to use any extra memory, we can do it by finding
# the middle, reversing the second half of the linked list, then merging
# the non-reversed first half with the second, reversed half.
#
# Time complexity: O(n) - We visit all nodes a linear number of times.
# Space complexity; O(1) - Only a fixed number of variables are kept.
#
# Runtime 43 ms Beats 97%
# Memory 24.1 MB Beats 50%
class NoExtraMemory:
    def _mergeLists(self, head_a, head_b):
        tail = head_a
        head = head_a

        head_a = head_a.next
        while head_b:
            tail.next = head_b
            tail = tail.next
            head_b = head_b.next
            if head_a:
                head_a, head_b = head_b, head_a

        return head

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # Split the lists into first and second halves
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        # Reverse the second half
        last, current = None, middle
        while current:
            next = current.next
            current.next = last
            last = current
            current = next

        tail = last

        # Merge the two halves
        return self._mergeLists(head, tail)


def test():
    executors = [Deque, NoExtraMemory]
    tests = [
        [[1], [1]],
        [[1, 2], [1, 2]],
        [[1, 2, 3], [1, 3, 2]],
        [[1, 2, 3, 4], [1, 4, 2, 3]],
        [[1, 2, 3, 4, 5], [1, 5, 2, 4, 3]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = deserializeListToLinkedList(t[0])
                # Modify in place
                sol.reorderList(head)
                exp = t[1]
                serialized_result = serializeLinkedList(head)
                assert serialized_result == exp, (
                    f"\033[93m» {serialized_result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
