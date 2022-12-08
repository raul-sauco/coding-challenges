# 872. Leaf-Similar Trees
# 🟢 Easy
#
# https://leetcode.com/problems/leaf-similar-trees/
#
# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from itertools import zip_longest
from typing import List, Optional

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# We need to explore the entire tree using any type of DFS, we cannot
# use BFS because we want to visit leaves, possibly on different levels,
# on a right-to-left or left-to-right order. We explore the tree and,
# when we find a leave, we add it to the result set. We only need to
# guarantee that the order in which we visit the leaves is the same on
# the first and second tree.
#
# Time complexity: O(n) - We will visit all nodes.
# Space complexity: O(n) - The stack or call stack will grow to the
# height of the tree, if skewed, it could be the same as its size.
#
# Runtime 55 ms Beats 67.10%
# Memory 14 MB Beats 46.25%
class Iterative:
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        # Define an auxiliary function that returns a list of leaves in
        # a given tree.
        def getLeaves(root) -> List[int]:
            res, stack = [], [root]
            while stack:
                node = stack.pop()
                # Add leaves to the result.
                if not node.left and not node.right:
                    res.append(node.val)
                    continue
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return res

        # The list of leaves should be the same.
        return getLeaves(root1) == getLeaves(root2)


# Similar solution to the one above but explore the tree using recursion
# and a generator function instead of storing all values in memory like
# the previous solution.
#
# Time complexity: O(n) - We need to visit all nodes in the worst case.
# Space complexity: O(n) - In the worst case the height of the tree will
# be the same as its size.
#
# Runtime 28 ms Beats 97.68%
# Memory 14 MB Beats 46.25%
class RecursiveGenerator:
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        # Define a function that yields leaves on a given tree.
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
            yield from dfs(root.left)
            yield from dfs(root.right)

        # The values generated should match.
        return all(a == b for a, b in zip_longest(dfs(root1), dfs(root2)))


def test():
    executors = [
        Iterative,
        RecursiveGenerator,
    ]
    tests = [
        [[1, 2, 3], [1, 3, 2], False],
        [
            [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
            True,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.leafSimilar(
                    BinaryTree.fromList(t[0]).getRoot(),
                    BinaryTree.fromList(t[1]).getRoot(),
                )
                exp = t[2]
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
