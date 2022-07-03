# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from data import ListNode

# Keep two pointers, head and middle, each two head moves move middle one.
#
# Runtime: 32 ms, faster than 91.11% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 95.69 % of Python3 online submissions for Middle of the Linked List.


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        middle = head
        current = head
        shuffle = True
        while current.next:
            current = current.next
            if shuffle:
                middle = middle.next
            shuffle = not shuffle
        return middle
