# 230. Kth Smallest Element in a BST
# 🟠 Medium
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#
# Tags: Tree - Depth-First Search - Binary Search Tree - Binary Tree

import timeit
from collections import deque
from lib2to3.pgen2.token import OP
from typing import Optional

from data import deserializeStringArrayToBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The inorder traversal of a BST results in a sorted list of its node
# values, therefore, we can explore the tree inorder until we have
# seen k values, and return the value at that node.
#
# Time complexity: O(n) - We may visit each node once.
# Space complexity: O(h) - Where h is the height of the BST. O(n) worst
# case, if the tree is very unbalanced. O(log(n)) best case, with a
# balanced tree.
#
# Runtime: 66 ms, faster than 74.57%
# Memory Usage: 18 MB, less than 89.14%
class IterativeInOrder:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a counter of nodes that we have seen.
        seen = 0
        # Set current to root of binary tree
        current = root
        # Use a stack to push nodes that we need to visit.
        stack = []
        # Keep going while we have nodes to explore in either source.
        while current or stack:

            # While the current node has a left child, keep pushing into
            # the stack
            if current:
                stack.append(current)
                current = current.left

            # If there is no current node, the stack cannot be empty.
            # Pop from the stack and mark one more node as visited.
            else:
                current = stack.pop()
                # Register that we have visited one more node.
                seen += 1
                # If this node is the kth node we visit, this is the
                # kth smallest node in the BST because we are visiting
                # nodes inorder.
                if seen == k:
                    return current.val

                # We have visited this node's full left subtree, get
                # started on the right subtree.
                current = current.right


# As it is common with tree traversals, the recursive version is a bit
# simpler than its iterative counterpart.
#
# Time complexity: O(n) - We may visit every node.
# Space complexity: O(n) - The size of the call stack.
#
# Runtime: 139 ms, faster than 5.19%
# Memory Usage: 18.2 MB, less than 14.39%
class RecursiveInOrder:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Define a function that inorder traverses the tree from root.
        def dfs(node):
            return (
                dfs(node.left) + [node.val] + dfs(node.right) if node else []
            )

        # Initial call
        return dfs(root)[k - 1]


def test():
    executors = [
        IterativeInOrder,
        RecursiveInOrder,
    ]
    tests = [
        ["[3,1,4,null,2]", 1, 1],
        ["[5,3,6,2,4,null,null,1]", 3, 3],
        ["[5,3,10,2,4,null,null,1]", 6, 10],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.kthSmallest(root, t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
