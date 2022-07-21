# Definitions for classes that get used in other files

from collections import defaultdict, deque
from typing import List, Optional


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


# Useful for testing binary tree problems using the strings provided on the description
# https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python


def deserializeStringArrayToBinaryTree(string):
    if string == "{}":
        return None
    nodes = [None if val == "null" else TreeNode(int(val)) for val in string.strip("[]{}").split(",")]
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
#     drawTree(deserializeStringArrayToBinaryTree("[1,2,3,null,null,4,null,null,5]"))
#     drawTree(deserializeStringArrayToBinaryTree("[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]"))

treeString = "[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]"
tree = deserializeStringArrayToBinaryTree(treeString)
result = serializeTreeToList(tree)
# drawTree(tree)
assert result == [2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7], result


# Serialize a linked list where the node values are integers to a list of integers.
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
