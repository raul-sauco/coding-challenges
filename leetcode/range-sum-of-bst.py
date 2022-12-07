# 938. Range Sum of BST
# 🟢 Easy
#
# https://leetcode.com/problems/range-sum-of-bst/
#
# Tags: Tree - Depth-First Search - Binary Search Tree - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# We can use the value of the root node to determine which subtrees need
# to be explored and wether the current node's value needs to be added.
# The recursive function calls itself, it could also have a nested
# recursive function that performed the search, if we wanted to avoid
# having to pass the low and high parameters in each call.
#
# Time complexity: O(n) - Each node is visited, at most, once.
# Space complexity: O(n) - The call stack can grow to the size of the
# height of the tree, if skewed, it could be the same as its size.
#
# Runtime 534 ms Beats 51.32%
# Memory 23 MB Beats 50.66%
class Recursive:
    def rangeSumBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> int:
        # Base case, there is no root.
        if not root:
            return 0
        # Avoid computing anything we don't need, compute subtree sums
        # depending on the position of the root regarding low and high.
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val == low:
            return self.rangeSumBST(root.right, low, high) + root.val
        if low < root.val < high:
            return (
                self.rangeSumBST(root.left, low, high)
                + root.val
                + self.rangeSumBST(root.right, low, high)
            )
        if root.val == high:
            return self.rangeSumBST(root.left, low, high) + root.val
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)


# We can use the value of the root node to determine which subtrees need
# to be explored and wether the current node's value needs to be added.
# The iterative version uses a stack to push subtrees that need to be
# explored.
#
# Time complexity: O(n) - Each node is visited, at most, once.
# Space complexity: O(n) - The stack can grow to the size of the height
# of the tree, if skewed, it could be the same as its size.
#
# Runtime 215 ms Beats 96.10%
# Memory 23 MB Beats 92.23%
class Iterative:
    def rangeSumBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> int:
        res, stack = 0, [root]
        while stack:
            current = stack.pop()
            if not current:
                continue
            if low <= current.val <= high:
                res += current.val
            if current.val > low:
                stack.append(current.left)
            if current.val < high:
                stack.append(current.right)
        return res


def test():
    executors = [
        Recursive,
        Iterative,
    ]
    tests = [
        [[], 5, 10, 0],
        [[10, 5, 15, 3, 7, None, 18], 7, 15, 32],
        [[10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.rangeSumBST(root, t[1], t[2])
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
