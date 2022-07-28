# Definitions for classes that get used in other files

from __future__ import annotations

from collections import defaultdict, deque
from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "TreeNode({})".format(self.val)


# Definition for a trie node
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Useful for testing binary tree problems using the strings provided on
# the description
# https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python


def deserializeStringArrayToBinaryTree(string):
    if string == "{}" or string == "[]":
        return None
    nodes = [
        None if val == "null" else TreeNode(int(val))
        for val in string.strip("[]{}").split(",")
    ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def serializeTreeToList(root: TreeNode) -> List[Optional[int]]:
    result = []
    if not root:
        return []
    queue = deque([root])
    # While we have elements and the current level is not all nulls
    while queue and set(queue) != {None}:
        # Process the next level
        for _ in range(len(queue)):
            current = queue.popleft()
            if not current:
                result.append(None)
            else:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)

    # Clean all trailing Nones from the result
    while result and result[-1] is None:
        result.pop()

    return result


def drawTree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align="center", font=("Arial", 12, "normal"))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle

    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


# if __name__ == "__main__":
#     drawTree(
#         deserializeStringArrayToBinaryTree("[1,2,3,null,null,4,null,null,5]")
#     )
#     drawTree(
#         deserializeStringArrayToBinaryTree(
#             "[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]"
#         )
#     )


# Serialize a linked list where the node values are integers to a list
# of integers.
def serializeLinkedList(head: ListNode) -> List[int]:
    result = []
    if not head:
        return result
    current = head
    if current.next:
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


# deserialize a list of int to a linked list and return the head node
def deserializeListToLinkedList(list: List[int]) -> Optional[ListNode]:
    if not list:
        return None
    current = ListNode(list[0])
    head = current
    for val in list[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Linked List data structure.
# The structure is immutable and most methods return the head to a new,
# or several new, linked lists.
#
# It contains a link to the head ListNode as well as some utility
# methods to perform common operations on the list.
class LinkedList:
    # Construct a LinkedList object with an optional head node.
    def __init__(self, head: Optional[ListNode]) -> None:
        self.head = head

    # Get the ListNode at the head of this linked list
    def getHead(self) -> Optional[ListNode]:
        return self.head

    # Construct a LinkedList from a list, if the list is empty, it will
    # return a LinkedList with a None head.
    def fromList(list: List) -> LinkedList:
        if not list:
            return LinkedList(None)
        current = ListNode(list[0])
        head = current
        for val in list[1:]:
            current.next = ListNode(val)
            current = current.next
        return LinkedList(head)

    # Serialize this linked list to an list containing the values in
    # each node.
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
    # If the linked list has an uneven number of nodes, it will return
    # the middle node.
    #   [1, 2, 3, 4, 5].findMiddle() => ListNode(3)
    # If the linked list has an even number of nodes, it will return the
    # last node on the first half.
    #   [1, 2, 3, 4, 5, 6, 7, 8].findMiddle() => ListNode(4)
    def findMiddle(self) -> ListNode:
        fast, slow = self.head, self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Split the current Linked List into two by the middle. If the
    # linked list has an uneven number of nodes, the
    # first half will be of greater length than the second half.
    #   [1, 2, 3, 4, 5].split() => ([1, 2, 3], [4, 5])
    def split(self) -> Tuple(LinkedList, Optional(LinkedList)):
        fast, slow = self.head, self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow
        # Split the lists
        slow = slow.next
        prev.next = None
        return (LinkedList(self.head), LinkedList(slow))

    # Return a new LinkedList created by reversing the elements on this
    # LinkedList.
    def reverse(self) -> LinkedList:
        last = None
        current = self.head
        while current:
            nextNode = current.next
            current.next = last
            last = current
            current = nextNode
        return LinkedList(last)
