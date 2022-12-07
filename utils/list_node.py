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
