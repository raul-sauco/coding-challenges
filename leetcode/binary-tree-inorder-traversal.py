# 94. Binary Tree Inorder Traversal
# 🟢 Easy
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/
#
# Tags: Stack - Tree - Depth-First Search - Binary Tree

import timeit
from typing import List, Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# The inorder traversal first explores the left subtree, then the root,
# then the right subtree. It is easy to implement it recursively calling
# the same method on the left, then the right subtree.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The call stack. The best case, with a well
# balanced tree, it would be O(log(n)) but the worst case, a completely
# unbalanced tree, it would be O(n).
#
# Runtime: 62 ms, faster than 13.79%
# Memory Usage: 13.8 MB, less than 60.15%
class RecursiveDFS:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base case
        if not root:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )


# For the iterative version, we use a stack. We keep a reference to a
# current node that we are traveling, but not processing yet, and keep
# traveling downwards through the left branch, pushing nodes into the
# stack, until we get to a leaf, when we do, we pop a node from the
# stack, process it, adding its value to the result, and assign its
# right child as the current node that we are traveling.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The call stack. The best case, with a well
# balanced tree, it would be O(log(n)) but the worst case, a completely
# unbalanced tree, it would be O(n).
#
# Runtime: 30 ms, faster than 95.20%
# Memory Usage: 13.8 MB, less than 60.15%
class IterativeDFS:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Use a stack for DFS.
        stack, res, current = [], [], root
        # Keep going while we have a current node that we are processing
        # or we have elements in the stack.
        while current or stack:
            # If we are traveling through left children, push them into
            # the stack.
            if current:
                stack.append(current)
                # Then visit its left child.
                current = current.left
                continue
            # Else, the last node's left child was null.
            # Pop the last value from the stack, process it and start
            # exploring its right sub-tree.
            node: TreeNode = stack.pop()
            res.append(node.val)
            current = node.right

        return res


# We can also use the Morris Traversal algorithm to obtain the inorder
# traversal values.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(1) - No stack or call stack, we obtain the
# sequence manipulating pointers.
#
# Runtime: 60 ms, faster than 17.62%
# Memory Usage: 13.8 MB, less than 60.15%
class MorrisTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        current = root
        while current:
            # If current does not have a left child, process it.
            if not current.left:
                res.append(current.val)
                current = current.right
            # Else, move current, it becomes the right child of the
            # right-most node of its left subtree.
            else:
                # Explore the left subtree to find the rightmost child.
                rm = current.left
                while rm.right:
                    rm = rm.right
                # rm is the rightmost child, append current as its right
                # child
                rm.right = current
                # Explore from the new root.
                current = current.left
                # Remove the cycle.
                rm.right.left = None

        return res


def test():
    executors = [
        RecursiveDFS,
        IterativeDFS,
        MorrisTraversal,
    ]
    tests = [
        ["[]", []],
        ["[1]", [1]],
        ["[1,null,2,3]", [1, 3, 2]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.inorderTraversal(root)
                exp = t[1]
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
