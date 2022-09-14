# 1457. Pseudo-Palindromic Paths in a Binary Tree
# 🟠 Medium
#
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
#
# Tags: Bit Manipulation - Tree - Depth-First Search -
# Breath-First Search - Binary Tree

import timeit
from typing import Optional, Set

from data import TreeNode, deserializeStringArrayToBinaryTree


# Use DFS to find unique paths between the root and the leaves. While
# traveling down the path, keep track of node values that we have seen
# using a set, each time we see a match for a value, we know that we
# can use it to construct two symmetrical elements in the palindrome and
# we remove the match from the set. When we arrive at a leaf, we must
# have zero or one element left in the set for the path to be a pseudo
# palindrome.
#
# Time complexity: O(n) - We visit each node once and perform O(1)
# operations.
# Space complexity: O(h) - Where h is the height of the tree, for the
# call stack. h could be equal to n if each node had a single child.
# The set uses O(1) because the values in the node can only be 1-9.
#
# Runtime: 1761 ms, faster than 20.88%
# Memory Usage: 85.1 MB, less than 71.65%
class UsingSet:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        # Root is guaranteed to not be null.
        # Define a function that explores the tree using DFS.
        def dfs(node: TreeNode, seen: Set[int]) -> int:
            # Add this value to the seen set.
            if node.val in seen:
                seen.remove(node.val)
            else:
                seen.add(node.val)
            # If the current node is not a leaf, keep exploring and
            # return the result of exploring its children.
            if node.left or node.right:
                res = (dfs(node.left, seen) if node.left else 0) + (
                    dfs(node.right, seen) if node.right else 0
                )
            # If the current node is a leaf, the path formed from the
            # root to it is a pseudo palindrome only if the values
            # found on the way were all matched, or all except for one.
            else:
                res = int(len(seen) < 2)
            # Reset the seen set to the caller's state.
            if node.val in seen:
                seen.remove(node.val)
            else:
                seen.add(node.val)
            return res

        # Initial call.
        return dfs(root, set())


# TODO: add a solution using bits to keep track of the digits seen.


def test():
    executors = [
        UsingSet,
    ]
    tests = [
        ["[2,3,1,3,1,null,1]", 2],
        ["[2,1,1,1,3,null,null,null,null,null,1]", 1],
        ["[9]", 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.pseudoPalindromicPaths(root)
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
