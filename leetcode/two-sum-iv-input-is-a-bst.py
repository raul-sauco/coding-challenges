# 653. Two Sum IV - Input is a BST
# 🟢 Easy
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
#
# Tags: Hash Table - Two Pointers - Tree - Depth-First Search -
# Breadth-First Search - Binary Tree - Binary Search Tree

import timeit
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# Use DFS to explore the tree, for each node visited, we put its value
# in a hash set of values that we have seen, we also check if we have
# seen the complement of its value `target-current.val` if we have seen
# it, we return True.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(h) - Where h is the maximum height of the tree,
# it will be O(log(n)) if the tree is well balanced, but it could be
# O(n) if the tree was very unbalanced.
#
# Runtime: 86 ms, faster than 91.87%
# Memory Usage: 16.3 MB, less than 82.46%
class IterativeDFS:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Create a set of nodes that would match.
        seen = set()
        # Use a stack for DFS.
        stack = [root]
        # Keep visiting nodes while the stack is not empty.
        while stack:
            # LIFO
            current = stack.pop()
            # If we have seen the complement of this number, return now.
            if k - current.val in seen:
                return True
            # Otherwise, add this value to the set of values seen.
            seen.add(current.val)
            # Process the children skipping null values.
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        # If we could not find two nodes that constructed the sum.
        return False


# Similar logic to the previous solution but use recursive DFS.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(h) - Where h is the maximum height of the tree,
# it will be O(log(n)) if the tree is well balanced, but it could be
# O(n) if the tree was very unbalanced.
#
# Runtime: 86 ms, faster than 91.87%
# Memory Usage: 18.3 MB, less than 40.47%
class RecursiveDFS:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Create a set of nodes that would match.
        seen = set()
        # Define a recursive function that performs DFS.
        def dfs(node: Optional[TreeNode]) -> bool:
            # Base case, null node.
            if not node:
                return False
            # Base case, found a match.
            if k - node.val in seen:
                return True
            # Otherwise add this value to the seen set.
            seen.add(node.val)
            # Explore the children.
            return dfs(node.left) or dfs(node.right)

        # Initial call.
        return dfs(root)


def test():
    executors = [
        IterativeDFS,
        RecursiveDFS,
    ]
    tests = [
        ["[1]", 1, False],
        ["[5,3,6,2,4,null,7]", 9, True],
        ["[5,3,6,2,4,null,7]", 28, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.findTarget(root, t[1])
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
