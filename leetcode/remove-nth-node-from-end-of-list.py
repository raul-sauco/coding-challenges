# 19. Remove Nth Node From End of List
# 🟠 Medium
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
# Tags: Linked List - Two Pointers


import timeit
from typing import Optional

from data import LinkedList, ListNode


# Two pointers a fast one moves n positions ahead of a slow one.
# When the fast pointer reaches the end of the linked list, remove the
# node right after the slow pointer. This handles the case when n == 1.
# Handle separately the case when the node to be removed is the head.
#
# Time complexity: O(n) - we visit each node once.
# Space complexity: O(1) - we only store pointers in memory.
#
# Runtime: 34 ms, faster than 94.01%
# Memory Usage: 13.8 MB, less than 69.55%
class TwoPointers:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        i = 0
        # Keep two pointers, one to the current node we visit, one to
        # the deletion target
        current, prev = head, None
        while current:
            current = current.next
            if i == n:
                prev = head
            # Once the index is ahead of target by n, move them forward
            # in tandem
            if i > n:
                prev = prev.next
            i += 1
        # Prev is the previous node to target. Move that pointer
        # forward, if n == 1 it will set it to null
        if prev:
            prev.next = prev.next.next
        else:
            # The pointer has not moved forward, remove the head
            head = head.next
        return head


def test():
    executors = [TwoPointers]
    tests = [
        [[1], 1, []],
        [[1, 2], 1, [1]],
        [[1, 2], 2, [2]],
        [[1, 2, 3, 4, 5], 2, [1, 2, 3, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                # Create a linked list from the test array
                ll = LinkedList.fromList(t[0])
                # The solution receives the head of a linked list and
                # returns the head of the solution linked list.
                result = sol.removeNthFromEnd(ll.getHead(), t[1])
                exp = t[2]
                # The result is a ListNode, create a linked list and
                # serialize it to list.
                serialized_result = LinkedList(result).toList()
                assert serialized_result == exp, (
                    f"\033[93m» {serialized_result} <> {exp}\033[91m "
                    + f"for test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
