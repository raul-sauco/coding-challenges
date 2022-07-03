# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
from data import ListNode


# Runtime: 95 ms, faster than 33.27% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.5 MB, less than 66.33 % of Python3 online submissions for Linked List Cycle.
class Floyd:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Runtime: 103 ms, faster than 22.79% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.9 MB, less than 10.43 % of Python3 online submissions for Linked List Cycle.
class Set:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        seen = {head}
        while head.next:
            head = head.next
            if head in seen:
                return True
            seen.add(head)
        return False
