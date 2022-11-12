# Representation of a binary tree. The tree can be, but it is not
# guaranteed to be, a binary search tree.
from __future__ import annotations

from collections import deque
from typing import List, Optional

from .tree_node import TreeNode


class BinaryTree:
    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def getRoot(self) -> Optional[TreeNode]:
        return self.root

    # Factory method that constructs and returns
    def fromStringArray(string: str) -> BinaryTree:
        if not string or string == "{}" or string == "[]":
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
        return BinaryTree(root)

    # Serialize this binary tree to a list of integers.
    def toList(self) -> List[Optional[int]]:
        result = []
        if not self.root:
            return []
        queue = deque([self.root])
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

    # Draw this tree using turtle.
    def drawTree(self) -> None:
        if not self.root:
            return

        def height(root):
            return (
                1 + max(height(root.left), height(root.right)) if root else -1
            )

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
        h = height(self.root)
        jumpto(0, 30 * h)
        draw(self.root, 0, 30 * h, 40 * h)
        t.hideturtle()
        turtle.mainloop()
