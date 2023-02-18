# 783. Minimum Distance Between BST Nodes
# 🟢 Easy
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#
# Tags: Tree - Depth-First Search - Breadth-First Search
#       Binary Search Tree - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# The inorder traversal of a BST results in a list of its values in
# sorted order, we can use that inorder traversal property to traverse
# the values in sorted order comparing each value with the previous one.
#
# Time complexity: O(n) - We will visit each node once.
# Space complexity: O(n) - The stack will grow to the height of the tree
# which is worst case n and best case log(n).
#
# Runtime 25 ms Beats 97.45%
# Memory 13.8 MB Beats 98.73%
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # The minimum difference seen and the previous value.
        res, prev = float("inf"), float("-inf")
        node, stack = root, []
        while node or stack:
            # Push all left children into the stack.
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                # Process this node.
                res, prev = min(res, node.val - prev), node.val
                node = node.right
        return res


def test():
    executors = [Solution]
    tests = [
        [[4, 2, 6, 1, 3], 1],
        [[1, -20, 48, -100, -14, 12, 62], 6],
        [[1, 0, 48, None, None, 12, 49], 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.minDiffInBST(root)
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
