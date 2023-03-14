# 129. Sum Root to Leaf Numbers
# 🟠 Medium
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
#
# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import TreeNode


# Traverse the tree using preorder DFS, add the value of the current
# node to the path sum, if the node is a leaf, return that value,
# otherwise call the function for any non-null children.
#
# Time complexity: O(n) - We will visit every node in the tree and do
# constant work for each.
# Space complexity: O(h) - The height of the call stack will be the
# height of the tree, worst O(n), best O(log(n)).
#
# Runtime 28 ms Beats 88.93%
# Memory 13.8 MB Beats 95.89%
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, path: int) -> int:
            path *= 10
            path += node.val
            if not node.left and not node.right:
                return path
            return (dfs(node.left, path) if node.left else 0) + (
                dfs(node.right, path) if node.right else 0
            )

        return dfs(root, 0)


def test():
    executors = [Solution]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.methodCall(t[0])
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
