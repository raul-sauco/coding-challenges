# 144. Binary Tree Preorder Traversal
# 🟢 Easy
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/
#
# Tags: Stack - Tree - Depth-First Search - Binary Tree

import timeit
from typing import List, Optional

from utils.binary_tree import BinaryTree, TreeNode


# Iterative version of the solution, process the current node, add the
# right child to the stack, then the left child, to make sure we
# process the left subtree before the right subtree.
#
# Time complexity: O(n) - We will visit each node once.
# Space complexity: O(n) - The stack will grow in size linearly with the
# size of the input.
#
# Runtime 26 ms Beats 97.9%
# Memory 13.8 MB Beats 96.79%
class Iterative:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            current = stack.pop()
            res.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return res


# Recursive version, similar to the previous solution but use the
# implied call stack.
#
# Time complexity: O(n) - We will visit each node once.
# Space complexity: O(n) - The call stack will grow in size linearly
# with the size of the input.
#
# Runtime 29 ms Beats 92.53%
# Memory 13.8 MB Beats 96.79%
class Recursive:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: TreeNode):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        res = []
        dfs(root)
        return res


# Improve the space complexity of the previous solutions using the
# Morris Traversal algorithm, when a node has a right subtree, instead
# of adding its root to the stack, we slice it from its current
# position and add it as the right child of the rightmost child of the
# left subtree, that guarantees that we will visit that node only after
# we have visited all nodes of the left subtree.
#
# Time complexity: O(n) - We visit each node once or twice.
# Space complexity: O(1) - We only keep two pointers in memory.
#
# Runtime 39 ms Beats 61.74%
# Memory 13.8 MB Beats 57.18%
class MorrisTraversal:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, current = [], root
        while current:
            if not current.left:
                res.append(current.val)
                current = current.right
            else:
                last = current.left
                while last.right and last.right != current:
                    last = last.right
                if not last.right:
                    res.append(current.val)
                    last.right = current
                    current = current.left
                else:
                    last.right = None
                    current = current.right
        return res


def test():
    executors = [
        Iterative,
        Recursive,
        MorrisTraversal,
    ]
    tests = [
        [[], []],
        [[1], [1]],
        [[1, None, 2, 3], [1, 2, 3]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.preorderTraversal(root)
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
