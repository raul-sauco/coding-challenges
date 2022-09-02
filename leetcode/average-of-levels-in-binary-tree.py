# 637. Average of Levels in Binary Tree
# 🟢 Easy
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
#
# Tags: Tree - Depth-First Search - Breath-First Search - Binary Tree

import timeit
from collections import deque
from typing import List, Optional

from data import deserializeStringArrayToBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This problem can be solved using breath first search and computing the
# average of each level as we process them.
#
# Time complexity: O(n) - We visit each node of the tree once.
# Space complexity: O(n) - The queue will hold at most one level at a
# time, one level can hold 2 times more nodes than the previous level
# and it can hold more than half of all the nodes in the tree > O(n/2).
#
# Runtime: 50 ms, faster than 96.56%
# Memory Usage: 16.5 MB, less than 87.46%
class IterativeBFS:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Use a queue for BFS. Root cannot be null.
        q = deque([root])
        # Use an empty list to store the average of each level, initially
        # we have no way of knowing how many levels there will be.
        result = []
        while q:
            # Store the sum of nodes in this level.
            temp, level_length = 0, len(q)
            # Iterate over all elements in one level.
            for _ in range(len(q)):
                # Pop the leftmost element.
                current = q.popleft()
                # Add this element value to the level sum.
                temp += current.val
                # Append existing children to the right.
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            # Calculate the average of this level.
            result.append(temp / level_length)
        return result


def test():
    executors = [IterativeBFS]
    tests = [
        ["[3,9,20,null,null,15,7]", [3.00000, 14.50000, 11.00000]],
        ["[3,9,20,15,7]", [3.00000, 14.50000, 11.00000]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.averageOfLevels(root)
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
