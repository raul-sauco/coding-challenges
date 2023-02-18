# 226. Invert Binary Tree
# 🟢 Easy
#
# https://leetcode.com/problems/invert-binary-tree/
#
# Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree


import timeit
from typing import Optional

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# Use depth-first search to visit all nodes in the tree, for each node,
# swap the position of its children.
#
# Time complexity: O(n) - We visit each node in the tree and, for each,
# do O(1) work.
# Space complexity: O(h) - The call stack can grow to the height of the
# tree, which could be the same as n.
#
# Runtime: 28 ms, faster than 96.89%
# Memory Usage: 13.8 MB, less than 96.89%
class RecursiveDFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        tmp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = tmp
        return root


# Use depth-first search to visit all nodes in the tree, for each node,
# swap the position of its children, recursively call the function on
# the children.
#
# Time complexity: O(n) - We visit each node in the tree and, for each,
# do O(1) work.
# Space complexity: O(h) - The call stack can grow to the height of the
# tree, which could be the same as n.
#
# Runtime 38 ms Beats 33.89%
# Memory 13.8 MB Beats 94.48%
class RecursiveInPlace:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(
            root.left
        )
        return root


# Use depth-first search to visit all nodes in the tree, for each node,
# swap the position of its children.
#
# Time complexity: O(n) - We visit each node in the tree and, for each,
# do O(1) work.
# Space complexity: O(h) - The stack can grow to the height of the tree,
# which could be the same as n.
#
# Runtime 31 ms Beats 92.4%
# Memory 13.8 MB Beats 94.98%
class IterativeDFS:
    def invertTree(self, root):
        stack = [root]
        while stack:
            current = stack.pop()
            if current:
                current.left, current.right = current.right, current.left
                stack.append(current.left)
                stack.append(current.right)
        return root


def test():
    executors = [
        IterativeDFS,
        RecursiveDFS,
        RecursiveInPlace,
    ]
    tests = [
        [[], []],
        [[2, 1, 3], [2, 3, 1]],
        [[4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 2, 7, 6, 5, 4, None, None, None, None, None, None, 9, 8],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = BinaryTree(sol.invertTree(root)).toList()
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
