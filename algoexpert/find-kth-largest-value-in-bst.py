# Find Kth Largest Value In BST
# 🟠 Medium
#
# https://www.algoexpert.io/questions/find-kth-largest-value-in-bst
#
# Tags: Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# We can use iterative inorder right-to-left DFS.
#
# Time complexity: O(n) - We may end up visiting all the nodes in the
# tree.
# Space complexity: O(n) - The stack may end up holding all nodes.
class Iterative:
    def findKthLargestValueInBst(
        self, tree: Optional[TreeNode], k: int
    ) -> bool:
        count, stack, current = 0, [], tree
        while current or stack:
            if current:
                stack.append(current)
                current = current.right
                continue
            node = stack.pop()
            count += 1
            if count == k:
                return node.value
            current = node.left
        raise Exception(f"No {k}-th largest value found")


# We can use tho Morris traversal but appending the left subtree to the
# rightmost node.
#
# Time complexity: O(n) - We may end up visiting all the nodes in the
# tree.
# Space complexity: O(1) - We manipulate pointers, no extra memory used.
class MorrisTraversal:
    def findKthLargestValueInBst(
        self, tree: Optional[TreeNode], k: int
    ) -> bool:
        count, current = 0, tree
        while current:
            if not current.right:
                count += 1
                if count == k:
                    return current.value
                current = current.left
                continue
            leftmost = current.right
            while leftmost.left:
                leftmost = leftmost.left
            leftmost.left = current
            current = current.right
            leftmost.left.right = None
        raise Exception(f"No {k}-th largest value found")


def test():
    executors = [
        Iterative,
        MorrisTraversal,
    ]
    tests = [
        [[5], 1, 5],
        [[5, 4, 6, 3, None, None, 7], 1, 7],
        [[15, 5, 20, 2, 5, 17, 22, 1, 3], 8, 2],
        [[15, 5, 20, 2, 5, 17, 22, 1, 3], 3, 17],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.findKthLargestValueInBst(root, t[1])
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
