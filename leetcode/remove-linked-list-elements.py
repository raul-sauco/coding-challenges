# 203. Remove Linked List Elements
# 🟢 Easy
#
# https://leetcode.com/problems/remove-linked-list-elements/
#
# Tags: Linked List - Recursion

import timeit
from typing import Optional

from data import LinkedList, ListNode


# Start by eliminating the value from the list head by skipping the
# pointer to head.next, if after this step we still have a head, travel
# through the list nodes checking the value of the next node, if it
# matches the search value, delete that node updating the linked list
# pointers.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity; O(1) - We only keep pointers in memory.
#
# Runtime: 126 ms, faster than 54.5%
# Memory Usage: 17.8 MB, less than 38.78%
class Solution:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        # Remove val from the head.
        while head:
            if head.val == val:
                dup = head
                head = head.next
                del dup
            else:
                break
        if not head:
            return None
        # Remove val from the middle/end.
        current = head
        while current.next:
            next = current.next
            # Skip the value or move the pointer.
            if next.val == val:
                current.next = next.next
                del next
            else:
                current = current.next
        return head


# Since the head could be null or it could contain the value we want to
# remove from the list, use a dummy node as the temporary head, then we
# can treat the head as any other node and iterate over the nodes
# removing duplicate values. Once done, we return dummy.next.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity; O(1) - We only keep pointers in memory.
#
# Runtime: 149 ms, faster than 30.30%
# Memory Usage: 17.8 MB, less than 38.78%
class Dummy:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        # Create a dummy node that points to the head.
        dummy = ListNode(next=head)
        current = dummy
        while current.next:
            # If we need to remove the next node, do it.
            if current.next.val == val:
                next = current.next
                current.next = next.next
                del next
            # If we don't need to remove the next node, move the pointer.
            else:
                current = current.next
        # Return the head of the result list, it could be null.
        return dummy.next


def test():
    executors = [
        Solution,
        Dummy,
    ]
    tests = [
        [[], 1, []],
        [[7, 7, 7, 7], 7, []],
        [[1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result_head = sol.removeElements(head, t[1])
                result = LinkedList(result_head).toList()
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
