# 623. Add One Row to Tree
# 🟠 Medium
#
# https://leetcode.com/problems/add-one-row-to-tree/
#
# Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

import timeit
from typing import Optional

from data import (
    TreeNode,
    deserializeStringArrayToBinaryTree,
    serializeBinaryTreeToStringArray,
)


# Use BFS to find the entire level above the insertion, then insert two
# new nodes with the given value below each one.
#
# Time complexity: O(n) - We will visit at most each node once.
# Space complexity: O(n) - For the list of nodes in a level.
#
# Runtime: 130 ms, faster than 9.24%
# Memory Usage: 16.7 MB, less than 93.3%
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        # Edge case depth == 1
        if depth == 1:
            node = TreeNode(val=val, left=root)
            return node
        # Use BFS to collect the entire level above the insertion.
        level = [root]
        while depth > 2:
            depth -= 1
            # Get the next level.
            next = []
            for current in level:
                if current.left:
                    next.append(current.left)
                if current.right:
                    next.append(current.right)
            level = next
        # `level` holds the level above the insertion.
        for node in level:
            node.left = TreeNode(val=val, left=node.left)
            node.right = TreeNode(val=val, right=node.right)
        return root


def test():
    executors = [Solution]
    tests = [
        ["[1]", 4, 1, "[4,1]"],
        ["[1,null,3]", 2, 2, "[1,2,2,null,null,null,3]"],
        ["[4,2,6,3,1,5]", 1, 2, "[4,1,1,2,null,null,6,3,1,5]"],
        ["[4,2,null,3,1]", 1, 3, "[4,2,null,1,1,3,null,null,1]"],
        [
            "[1,2,2,null,null,null,3]",
            2,
            2,
            "[1,2,2,2,null,null,2,null,null,null,3]",
        ],
        [
            "[1,2,2,null,null,null,3]",
            5,
            3,
            "[1,2,2,5,5,5,5,null,null,null,null,null,null,null,3]",
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.addOneRow(root, t[1], t[2])
                result = serializeBinaryTreeToStringArray(result)
                exp = t[3]
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
