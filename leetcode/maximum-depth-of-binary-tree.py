# 104. Maximum Depth of Binary Tree
# 🟢 Easy
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree


import timeit
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# We can use a recursive call that computes the height of the left and
# right child and returns the maximum between them plus one for the
# current level.
#
# Time complexity: O(n) - We will visit each node in the tree.
# Space complexity: O(n) - The height of the call stack, it could go
# from O(n) in the worst case, a skewed tree, to O(log(n)) best case if
# the tree was well balanced.
#
# Runtime: 41 ms, faster than 93.90%
# Memory Usage: 16.2 MB, less than 74.04%
class Recursive:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# Iteratively process each level of the tree while keeping count of how
# many levels we have seen.
#
# Time complexity: O(n) - We will visit each node in the tree.
# Space complexity: O(n) - The stack will contain one level at a time,
# a level could have more than half the nodes in the tree.
#
# Runtime 43 ms Beats 71.87%
# Memory 15.3 MB Beats 89.39%
class IterativeBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Initialize to 0 to account for an empty level created by the
        # leave nodes.
        res, stack = -1, [root]
        while stack:
            res += 1
            # Create a new level that contains the children of the
            # current level.
            stack = [
                child
                for node in stack
                if node
                for child in (node.left, node.right)
            ]
        return res


def test():
    executors = [
        Recursive,
        IterativeBFS,
    ]
    tests = [
        [[1, None, 2], 2],
        [[3, 9, 20, None, None, 15, 7], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.maxDepth(root)
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
