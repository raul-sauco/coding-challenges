from __future__ import annotations

from typing import List, Optional, Tuple

from typing_extensions import Self


# Definition for a Linked List, or Doubly Linked List, node
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "ListNode({})".format(self.val)

    @property
    def value(self):
        return self.val


# Linked List data structure.
# The structure is immutable and most methods return the head to a new, or several new, linked lists.
#
# It contains a link to the head ListNode as well as some utility methods to perform common operations on the list.
class LinkedList:
    def __init__(self, head: ListNode) -> None:
        self.head = head

    # Get the ListNode at the head of this linked list
    def getHead(self) -> ListNode:
        return self.head

    def fromList(list: List) -> LinkedList:
        if list is None:
            raise Exception(
                "LinkedList.fromList needs a list argument, None received"
            )
        if not list:
            return LinkedList(None)
        current = ListNode(list[0])
        head = current
        for val in list[1:]:
            current.next = ListNode(val)
            current = current.next
        return LinkedList(head)

    # Serialize this linked list to an list containing the values in each node.
    def toList(self) -> List:
        result = []
        current = self.head
        if current and current.next:
            cycle_detect = current.next.next
        else:
            cycle_detect = None
        while current:
            result.append(current.val)
            current = current.next
            if cycle_detect:
                if cycle_detect == current:
                    raise Exception("LinkedList has a cycle", result)
                if cycle_detect.next:
                    cycle_detect = cycle_detect.next.next
                else:
                    cycle_detect = None
        return result

    # Return the middle node in a linked list.
    # If the linked list has an uneven number of nodes, it will return the middle node.
    #   [1, 2, 3, 4, 5].findMiddle() => ListNode(3)
    # If the linked list has an even number of nodes, it will return the last node on the first half.
    #   [1, 2, 3, 4, 5, 6, 7, 8].findMiddle() => ListNode(4)
    def findMiddle(self) -> ListNode:
        fast, slow = self.head, self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Split the current Linked List into two by the middle. If the linked list has an uneven number of nodes, the
    # first half will be of greater length than the second half.
    #   [1, 2, 3, 4, 5].split() => ([1, 2, 3], [4, 5])
    def split(self) -> Tuple(Self, Optional(Self)):
        fast, slow = self.head, self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow
        # Split the lists
        slow = slow.next
        prev.next = None
        return (LinkedList(self.head), LinkedList(slow))

    # Return a new LinkedList created by reversing the elements on this LinkedList.
    def reverse(self) -> LinkedList:
        last = None
        current = self.head
        while current:
            nextNode = current.next
            current.next = last
            last = current
            current = nextNode
        return LinkedList(last)
