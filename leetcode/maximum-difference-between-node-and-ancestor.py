# 1026. Maximum Difference Between Node and Ancestor
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
#
# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# Explore the tree using a recursive DFS function that passes as
# parameters the highest and lowest values seen up to that moment.
#
# Time complexity: O(n) - We will visit each node once.
# Space complexity: O(n) - The call stack will be of the height of the
# tree.
#
# Runtime 32 ms Beats 99.31%
# Memory 19.9 MB Beats 91.9%
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node: Optional[TreeNode], highest: int, lowest: int) -> None:
            if not node:
                return
            self.res = max(
                self.res, abs(highest - node.val), abs(node.val - lowest)
            )
            highest, lowest = max(highest, node.val), min(lowest, node.val)
            dfs(node.left, highest, lowest)
            dfs(node.right, highest, lowest)

        dfs(root, root.val, root.val)
        return self.res


def test():
    executors = [Solution]
    tests = [
        ["[1,null,2,null,0,3]", 3],
        ["[8,3,10,1,6,null,14,null,null,4,7,13]", 7],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromStringArray(t[0]).getRoot()
                result = sol.maxAncestorDiff(root)
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
