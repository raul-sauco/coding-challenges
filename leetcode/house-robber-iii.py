# 337. House Robber III
# 🟠 Medium
#
# https://leetcode.com/problems/house-robber-iii/
#
# Tags: Dynamic Programming - Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from data import deserializeStringArrayToBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Improve visualization in the debugger.
    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


# A class that holds two return values, the maximum when the node
# that returns the value has been used, and the maximum when the node
# that returns the value has not been used.
class ReturnValue:
    def __init__(self):
        self.max_used = 0
        self.max_unused = 0

    # Improve visualization in the debugger.
    def __repr__(self) -> str:
        return f"ReturnValue({self.max_used},{self.max_unused})"


# The thief needs to visit each node and, for each, decide if it is
# best to rob it or not. The naive solution explores two branches from
# each node, the one that robs that node and the one that does not, at
# a time complexity of O(2^n). We can improve on that solution if we
# explore the tree using postorder DFS and, in each return to the
# parent we pass two values, the max if we had used that node, and the
# max if we had not used that node. The parent then can in turn
# compute the max loot possible using itself and not using itself. The
# solution to the problem is the max of using and not using the root.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 116 ms, faster than 9.11%
# Memory Usage: 16.2 MB, less than 39.52%
class RecursiveDFS:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Define a function that does recursive postorder DFS and
        # returns a ReturnValue object.
        def dfs(node: Optional[TreeNode]) -> ReturnValue:
            # Base case, if the node is null, we cannot rob it (0,0)
            if not node:
                return ReturnValue()
            # Calculate the max right and left profit.
            l = dfs(node.left)
            r = dfs(node.right)
            # Calculate the maximum profits at this point.
            rv = ReturnValue()
            # If we use this node, we cannot use the children.
            rv.max_used = l.max_unused + r.max_unused + node.val
            # If we don't use this node, we can use its children, or not
            # use them, if we can maximize the profit skipping them.
            rv.max_unused = max(l.max_used, l.max_unused) + max(
                r.max_used, r.max_unused
            )
            return rv

        # The result is the max between using and not using the root.
        rv = dfs(root)
        return max(rv.max_used, rv.max_unused)


# Performance optimized version of the previous solution, we avoid
# calling the function for null children and we use tuples instead of
# the ReturnValue class.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - For the call stack.
#
# Runtime: 56 ms, faster than 88.08%
# Memory Usage: 16.1 MB, less than 63.43%
class RecursiveDFSOpt:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Define a function that does recursive postorder DFS and
        # returns a ReturnValue object.
        def dfs(node: TreeNode):
            # Calculate the max right and left profit.
            l = dfs(node.left) if node.left else (0, 0)
            r = dfs(node.right) if node.right else (0, 0)
            return (max(l) + max(r), l[0] + r[0] + node.val)

        # The result is the max between using and not using the root.
        return max(dfs(root))


def test():
    executors = [
        RecursiveDFS,
        RecursiveDFSOpt,
    ]
    tests = [
        ["[4,1,null,2,null,3]", 7],
        ["[3,2,3,null,3,null,1]", 7],
        ["[3,4,5,1,3,null,1]", 9],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.rob(root)
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
