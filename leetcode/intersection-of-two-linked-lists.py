# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Cool method and explanation found here:
        # https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/2116127/Python-oror-Easy-2-approaches-oror-O(1)-space
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = headB if pointer_a is None else pointer_a.next
            pointer_b = headA if pointer_b is None else pointer_b.next
        return pointer_a
