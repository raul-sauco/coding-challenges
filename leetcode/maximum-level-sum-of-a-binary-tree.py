# 1161. Maximum Level Sum of a Binary Tree
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
#
# Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

import timeit
from collections import deque
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# This is a template that can be used as the starting point of a
# solution with minimal changes.
#
# Time complexity: O(n) - We do a BFS in which we compute the sum of the
# values of the nodes in each level as we visit them.
# Space complexity: O(n) - The queue holds one level at a time, in a
# binary tree, that can be more than half the total nodes in the tree.
#
# Runtime 310 ms Beats 56.78%
# Memory 21 MB Beats 68.44%
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = (root.val, 1)
        level = 0
        queue = deque([root])
        while queue:
            level_sum = 0
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > res[0]:
                res = (level_sum, level)
        return res[1]


def test():
    executors = [Solution]
    tests = [
        [[1, 7, 0, 7, -8, None, None], 2],
        [[989, None, 10250, 98693, -89388, None, None, None, -32127], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.maxLevelSum(root)
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
