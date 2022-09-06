# 814. Binary Tree Pruning
# 🟠 Medium
#
# https://leetcode.com/problems/binary-tree-pruning/
#
# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from data import (
    TreeNode,
    deserializeStringArrayToBinaryTree,
    serializeBinaryTreeToStringArray,
)


# We can use postorder DFS, each subtree returns whether it contains or
# not a 1, the parent prunes any child subtree that does not contain a 1.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 62 ms, faster than 19.19%
# Memory Usage: 13.7 MB, less than 97.77%
class RecursiveDFS:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case.
        if not root:
            return None
        # DFS function returns wether the child contains a 1.
        def containsOne(node: TreeNode) -> bool:
            # Unlink the children if they exist and do not contain a 1.
            if node.left and not containsOne(node.left):
                node.left = None
            if node.right and not containsOne(node.right):
                node.right = None
            # If this node val is 1 or has either child, there is a 1.
            return node.val or node.left or node.right

        # Check if we need to prune the entire tree.
        if not containsOne(root):
            return None
        return root


# Making the observation that we are really just recursively pruning
# the left and right subtrees, we can eliminate the helper function and
# recursively call `pruneTree`.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 52 ms, faster than 46.04%
# Memory Usage: 13.7 MB, less than 100.00%
class RecursiveDFS2:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case.
        if not root:
            return None
        # Recursively prune left and right subtrees.
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        # Return the root if this subtree contains a 1 somewhere.
        return root if root.left or root.right or root.val else None


def test():
    executors = [
        RecursiveDFS,
        RecursiveDFS2,
    ]
    tests = [
        ["[0,null,0,0,0]", "[]"],
        ["[1,null,0,0,1]", "[1,null,0,null,1]"],
        ["[1,0,1,0,0,0,1]", "[1,null,1,null,1]"],
        ["[1,1,0,1,1,0,1,0]", "[1,1,0,1,1,null,1]"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = serializeBinaryTreeToStringArray(sol.pruneTree(root))
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
