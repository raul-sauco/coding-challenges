# Binary Trees
# 🟠 Medium
#
# https://www.algoexpert.io/questions/merge-binary-trees
#
# Tags: Binary Tree - Recursion - Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# Use a recursive function that adds up the value of the current nodes
# and, if both nodes are not null, recursively merges its left and right
# subtrees.
#
# Time complexity: O(n) - We will visit each node once.
# Space complexity: O(h) - The call stack can grow to the size of the
# tree, which could be equal to the size of the tree for skewed trees.
class MergeRecursive:
    def mergeBinaryTrees(self, tree1: TreeNode, tree2: TreeNode) -> TreeNode:
        def mergeRecursive(
            a: Optional[TreeNode], b: Optional[TreeNode]
        ) -> Optional[TreeNode]:
            if not a:
                return b
            if not b:
                return a
            return TreeNode(
                a.value + b.value,
                mergeRecursive(a.left, b.left),
                mergeRecursive(a.right, b.right),
            )

        return mergeRecursive(tree1, tree2)


def test():
    executors = [MergeRecursive]
    tests = [
        [[1, 2, 3], [1], [2, 2, 3]],
        [[1, 3, 2, 7, 4], [1, 5, 9, 2, None, 7, 6], [2, 8, 11, 9, 4, 7, 6]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root1 = BinaryTree.fromList(t[0]).getRoot()
                root2 = BinaryTree.fromList(t[1]).getRoot()
                result = BinaryTree(
                    sol.mergeBinaryTrees(root1, root2)
                ).toList()
                exp = t[2]
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
