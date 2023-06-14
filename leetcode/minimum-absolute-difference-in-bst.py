# 530. Minimum Absolute Difference in BST
# 🟢 Easy
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
#
# Tags: Tree - Depth-First Search - Breadth-First Search - Binary Search Tree - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# The inorder traversal of a BST will return the nodes sorted by their
# values, we can use that property. We perform the inorder traversal
# comparing each node's value to the previous one while saving the
# minimum difference seen up to that point. Once we have visited all the
# nodes, we return the minimum difference seen.
#
# Time complexity: O(n) - We visit each node and do constant time work
# for each.
# Space complexity: O(h) - Where h is the height of the tree, the stack
# will grow to the height of the tree, which could be equal to n.
#
# Runtime 70 ms Beats 55.81%
# Memory 18.6 MB Beats 42.66%
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res, prev = float("inf"), float("-inf")
        current, stack = root, []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
                continue
            current = stack.pop()
            res, prev = min(res, current.val - prev), current.val
            current = current.right
        return res


def test():
    executors = [Solution]
    tests = [
        [[4, 2, 6, 1, 3], 1],
        [[1, 0, 48, None, None, 12, 49], 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.getMinimumDifference(root)
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
