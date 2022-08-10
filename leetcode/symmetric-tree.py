# 101. Symmetric Tree
# 🟢 Easy
#
# https://leetcode.com/problems/symmetric-tree/
#
# Tags: Tree - Depth-First Search - Breath-First Search - Binary Tree

import timeit
from collections import deque
from typing import List, Optional

from data import deserializeStringArrayToBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# If the tree is symmetrical, we can recursively explore both left and
# right sub trees comparing the symmetrical values of one to the other,
# if at any point they differ, the tree is not symmetrical.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - Up to one call per node in the call stack.
#
# Runtime: 64 ms, faster than 25.64%
# Memory Usage: 14.1 MB, less than 21.41%
class RecursiveDFS:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Check two nodes situated in symmetrical positions in the tree.
        def dfs(left, right):
            # If both nodes are not null and their value is the same,
            # recursively compare their outer and inner children.
            if left and right and left.val == right.val:
                return dfs(left.left, right.right) and dfs(
                    left.right, right.left
                )
            # If only one of the nodes is null, return False
            return left == right

        return dfs(root.left, root.right)


# We can explore the tree using BFS, for each two symmetrical nodes that
# we visit, we can push their outer, then inner children to the queue,
# when we recover them, they should be the same.
#
# Time complexity: O(n) - We push and pop each node once from the queue.
# Space complexity: O(log(n)) - The queue can grow in a logarithmic
# relation to the size of the tree.
#
# Runtime: 64 ms, faster than 25.64%
# Memory Usage: 14.1 MB, less than 21.41%
class IterativeBFS:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Push the root's children into a queue, they could be null.
        queue = deque([root.left, root.right])
        # Process elements in the queue while there are any.
        while queue:
            # Pop the first two elements, they should have the same
            # values and reversed children.
            left = queue.popleft()
            right = queue.popleft()
            # If they are both null, continue.
            if not left and not right:
                continue
            # If one of the nodes is null or their values differ, the
            # tree is not symmetrical.
            if not left or not right or left.val != right.val:
                return False
            # Push the outer children.
            queue.append(left.left)
            queue.append(right.right)
            # Push the inner children.
            queue.append(left.right)
            queue.append(right.left)
        # If we have explored each level and they were all symmetrical,
        # the tree is symmetrical.
        return True


def test():
    executors = [
        RecursiveDFS,
        IterativeBFS,
    ]
    tests = [
        ["[1]", True],
        ["[1,null,2]", False],
        ["[1,2,2,3,4,4,3]", True],
        ["[1,2,2,null,3,null,3]", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.isSymmetric(root)
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
