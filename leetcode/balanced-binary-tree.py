# https://leetcode.com/problems/balanced-binary-tree/

# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# Recursively explore the left and right branches from the current node. If either of them
# has a non-balanced subtree, return False up the call chain, otherwise check the height of
# the left and right subtrees, if the height difference is < 2, return the height of the subtree starting at
# this node.
#
# Time complexity: O(n) - we will visit each node of the tree once on the DFS algorithm
# Space complexity: O(log(n)) - the call stack depth maxes at the height of the tree
#
# Runtime: 87 ms, faster than 42.91% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 18.6 MB, less than 61.49% of Python3 online submissions for Balanced Binary Tree.
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            if left is False or right is False or abs(left - right) > 1:
                return False
            if node == root:
                return True
            return 1 + max(left, right)

        return dfs(root)


def test():
    root1 = deserializeStringArrayToBinaryTree("[3,9,20,null,null,15,7]")
    root2 = deserializeStringArrayToBinaryTree("[1,2,2,3,3,null,null,4,4]")
    root3 = deserializeStringArrayToBinaryTree("[null]")
    root4 = deserializeStringArrayToBinaryTree("[4]")
    root5 = deserializeStringArrayToBinaryTree("[4,2,null,2]")
    executors = [Solution]
    tests = [
        [root1, True],
        [root2, False],
        [root3, True],
        [root4, True],
        [root5, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.isBalanced(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
