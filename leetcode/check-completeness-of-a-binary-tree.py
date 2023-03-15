# 958. Check Completeness of a Binary Tree
# 🟠 Medium
#
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
#
# Tags: Tree - Breadth-First Search - Binary Tree

import timeit
from collections import deque
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# Use BFS, for each non-null node, check if we have seen a null position
# before, if we have, return false.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - A level could have up to (n+1) / 2 nodes.
#
# Runtime 27 ms Beats 99.14%
# Memory 13.8 MB Beats 61.14%
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        # A flag that detects whether we have seen a null.
        seen_null = False
        while queue:
            # for _ in range(len(queue)): No need to go a level at a
            current = queue.popleft()
            if current:
                # If we see a node with a value after a null, we
                # found a non-complete level.
                if seen_null:
                    return False
                # Otherwise enqueue the children.
                queue.append(current.left)
                queue.append(current.right)
            else:
                seen_null = True
        return True


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3, 4, 5, 6], True],
        [[1, 2, 3, 4, 5, None, 7], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.isCompleteTree(root)
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
