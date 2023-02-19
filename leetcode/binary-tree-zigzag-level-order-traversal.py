# 103. Binary Tree Zigzag Level Order Traversal
# 🟠 Medium
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# Tags: Tree - Breadth-First Search - Binary Tree

import timeit
from typing import List, Optional

from utils.binary_tree import BinaryTree, TreeNode


# Use a breadth-first traversal combined with a flag to determine which
# levels need to be reversed. Keep a stack that contains an entire level
# at a time, first get the values of the current level and append them
# to the result, then use the nodes to obtain the next level.
#
# Time complexity: O(n) - We will visit every node and do constant work
# for each.
# Space complexity: O(n) - The stack will hold one level of the tree at
# any given point.
#
# Runtime 31 ms Beats 85.17%
# Memory 14.1 MB Beats 94.5%
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base case no root.
        if not root:
            return []
        res, stack, reverse_level = [], [root], False
        while stack:
            vals = [node.val for node in stack if node]
            if reverse_level:
                vals.reverse()
            reverse_level = not reverse_level
            # Do not append the last empty level.
            if vals:
                res.append(vals)
            stack = [
                child
                for node in stack
                if node
                for child in (node.left, node.right)
            ]
        return res


def test():
    executors = [Solution]
    tests = [
        [[], []],
        [[1], [[1]]],
        [[3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.zigzagLevelOrder(root)
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
