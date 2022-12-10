# 1339. Maximum Product of Splitted Binary Tree
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
#
# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# Do one DFS pass to compute the sum of the entire tree, do a second
# pass to find the maximum product of two sections.
#
# Time complexity: O(n) - We will visit each node twice.
# Space complexity: O(h) - The call stack will grow to the height of the
# tree, best case O(log(n)), worst case O(n).
#
# Runtime 599 ms Beats 68.4%
# Memory 75.6 MB Beats 45.15%
class TwoFunctions:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # One first pass to get the sum of all node's values.
        def getTotal(node: Optional[TreeNode]):
            if not node:
                return 0
            return node.val + getTotal(node.left) + getTotal(node.right)

        total = getTotal(root)
        if not total:
            return 0
        res = 0
        # Second pass to find the maximum product.
        def findMaximum(node: Optional[TreeNode]):
            if not node:
                return 0
            subtree_sum = (
                node.val + findMaximum(node.left) + findMaximum(node.right)
            )
            nonlocal res
            nonlocal total
            res = max(res, (total - subtree_sum) * subtree_sum)
            return subtree_sum

        findMaximum(root)
        return res % (10**9 + 7)


# Simplify the previous solution reusing the same function to compute
# the total and maximum product.
#
# Time complexity: O(n) - We will visit each node twice.
# Space complexity: O(h) - The call stack will grow to the height of the
# tree, best case O(log(n)), worst case O(n).
#
# Runtime 963 ms Beats 24.96%
# Memory 75.6 MB Beats 45.15%
class SingleFunction:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        res = total = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            subtree_sum = node.val + dfs(node.left) + dfs(node.right)
            if total:
                nonlocal res
                res = max(res, (total - subtree_sum) * subtree_sum)
            return subtree_sum

        total = dfs(root)
        dfs(root)
        return res % (10**9 + 7)


def test():
    executors = [
        TwoFunctions,
        SingleFunction,
    ]
    tests = [
        [[], 0],
        [[1, 2, 3, 4, 5, 6], 110],
        [[1, None, 2, 3, 4, None, None, 5, 6], 90],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.maxProduct(root)
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
