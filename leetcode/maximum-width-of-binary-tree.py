# 662. Maximum Width of Binary Tree
# 🟠 Medium
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/
#
# Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

import timeit
from collections import deque
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# Use breadth-first search, visit all the nodes in one level enqueueing
# children that are not null together with the index they would be at
# inside their own level, after processing each level, check the index
# difference between the left and right-most nodes and use that to
# compute the result.
#
# Time complexity: O(n) - We will visit all nodes in the tree but will
# not do work for positions that hold a None value.
# Space complexity: O(n) - The queue will hold one entire level which
# could be O(n/2) in size.
#
# Runtime 43 ms Beats 81.19%
# Memory 14.7 MB Beats 81.19%
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        # Push nodes together with their index in the level.
        q = deque([(root, 0)])
        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, idx * 2))
                if node.right:
                    q.append((node.right, idx * 2 + 1))
        return res


def test():
    executors = [Solution]
    tests = [
        ["[1,3,2,5]", 2],
        ["[1,3,2,5,3,null,9]", 4],
        ["[1,3,2,5,null,null,9,6,null,7]", 7],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromStringArray(t[0]).getRoot()
                result = sol.widthOfBinaryTree(root)
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
