# 124. Binary Tree Maximum Path Sum
# 🔴 Hard
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
#
# Tags: Dynamic Programming - Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# Explore the tree using DFS, consider each node two different ways,
# as the root of a tree and as part of a path. Compute the maximum path
# sum for each of these situations, use the maximum path sum as the root
# of a tree to update a global result variable, and the maximum path
# value as part of a path to return to the caller, parent, node, since
# the parent will use this value to compute its own maximum values.
#
# Time complexity: O(n) - We will visit each node on the tree.
# Space complexity: O(h) - The call stack will reach the same height as
# the number of levels on the tree, if the tree is balanced it will be
# O(log(n)), if it is skewed, it will be O(n).
#
# Runtime: 87 ms, faster than 96.22%
# Memory Usage: 21.3 MB, less than 63.83%
class DFS:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the result.
        self.res = float("-inf")
        # Define a function that explores the subtree that has the given
        # node as a root and returns the maximum path sum using that
        # node as part of a path. It will also update a global result
        # variable that stores the best result using any node as the
        # root of the tree that would contain the path.
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            max_as_path = max(node.val, node.val + l, node.val + r)
            # If we decided to use the current node as the root of the
            # tree that contains the path, then we can add both branches
            # or choose one of them.
            # max_as_tree = max(max_as_path, node.val + l + r)
            self.res = max(self.res, max_as_path, node.val + l + r)
            # If we decide to use this node as part of a path, then we
            # have to choose one of its children's result since we
            # cannot use both.
            return max_as_path

        dfs(root)
        return self.res


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass


def test():
    executors = [
        DFS,
        # Solution,
    ]
    tests = [
        ["[3]", 3],
        ["[-3]", -3],
        ["[1,2,3]", 6],
        ["[-10,9,20,null,null,15,7]", 42],
        ["[-10,3,8,-4,6,7,9,null,null,-2,-3,2,9,-15]", 33],
        ["[-10,3,8,-4,6,7,9,null,null,-2,-3,2,9,-15,7]", 40],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.maxPathSum(root)
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
