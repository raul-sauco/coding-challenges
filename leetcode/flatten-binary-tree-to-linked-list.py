# 114. Flatten Binary Tree to Linked List
# 🟠 Medium
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
#
# Tags: Linked List - Stack - Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree, serializeTreeToList


# Use recursive DFS to flatten the tree.
# This solution should be slower than the other two but it is faster with the LeetCode tests, it could be due to the
# tests themselves.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 50 ms, faster than 68.94% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.2 MB, less than 47.67% of Python3 online submissions for Flatten Binary Tree to Linked List.
class Recursive:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Recursive function to flatten subtrees.
        def dfs(root):
            if not root:
                return

            # Recursively process the subtrees.
            left_subtree = dfs(root.left)
            right_subtree = dfs(root.right)

            # If the current tree has a left child, update the links.
            if left_subtree:
                left_subtree.right = root.right
                root.right = root.left
                root.left = None

            return right_subtree or left_subtree or root

        dfs(root)


# Explore the tree starting at the root, for each node that has a right and left children, push the right child into
# a stack, make the right pointer point to the left child and set the left pointer to null. If a node only has a right
# child, then process it next.
# If a children does not have either, try to pop from the stack.
#
# Time complexity: O(n) - We visit each node once or twice.
# Space complexity: O(n) - The stack could hold n/2 nodes depending on the shape of the input tree.
#
# Runtime: 86 ms, faster than 5.85% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.2 MB, less than 87.68% of Python3 online submissions for Flatten Binary Tree to Linked List.
class Stack:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        current = root
        queue = []
        while current:
            # If the current node has a left child, try to push the right sub-tree into the queue.
            if current.left:
                if current.right:
                    queue.append(current.right)

                # Update the right pointer to point to the left node and set the left pointer to null
                current.right = current.left
                current.left = None

            # If the current node does not have a right child, pop from the stack, it could be None.
            if not current.right and queue:
                current.right = queue.pop()

            # Move to processing the next node, if None, we will exit from the while loop.
            current = current.right

        # The root of the tree is still the same one and they ask us to not return it.
        # return root


# What the exercise is asking for is almost a Morris traversal of the binary tree. We can make use of that fact to
# provide a solution with O(1) space complexity, no recursion and no stack.
#
# Time complexity: O(n) - We visit each node once, the outer while loop will visit each node once, the inner while
# loop will visit each node none or one time.
# Space complexity: O(1) - We only keep a pointer to the current node we are processing.
#
# Runtime: 67 ms, faster than 31.00% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.2 MB, less than 47.67% of Python3 online submissions for Flatten Binary Tree to Linked List.
class Morris:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        current = root

        # Process the current node.
        while current:
            # If the current node has a left child, travel all the way down its rightmost path and append the
            # current node's right child as its right child.
            if current.left:
                temp = current.left
                while temp.right:
                    temp = temp.right
                temp.right = current.right

                # Now we have the right subtree appended to the rightmost node of the left subtree, update links.
                current.right = current.left
                current.left = None

            # Move to processing the next right node.
            current = current.right


def test():
    executors = [Recursive, Stack, Morris]
    tests = [
        ["[1,2,5,3,4,null,6]", "[1,null,2,null,3,null,4,null,5,null,6]"],
        ["[]", "[]"],
        ["[0]", "[0]"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                # Do not return anything, modify root in-place instead.
                root = deserializeStringArrayToBinaryTree(t[0])
                sol.flatten(root)
                result = serializeTreeToList(root)
                exp = serializeTreeToList(deserializeStringArrayToBinaryTree(t[1]))
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
