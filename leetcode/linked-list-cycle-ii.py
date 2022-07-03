# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

from data import ListNode

# Runtime: 61 ms, faster than 77.22% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 18 MB, less than 9.90 % of Python3 online submissions for Linked List Cycle II.


class Set:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        seen = {current}
        while current.next:
            current = current.next
            if current in seen:
                return current
            seen.add(current)
        return None


# Runtime: 95 ms, faster than 24.21% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.3 MB, less than 57.81 % of Python3 online submissions for Linked List Cycle II.
class Floyd:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
