# Reconstruct BST
# 🟠 Medium
#
# https://www.algoexpert.io/questions/reconstruct-bst
#
# Tags: Binary Search Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# Recursively call the function with the input array slices that
# correspond to the subtree that needs to be constructed.
#
# Time complexity: O(n^2) - For every subtree, every node, the
# corresponding array values need to be copied into a new array.
# Space complexity: O(n) - The call stack will have the same height as
# the input tree, which could be the same as its size.
class Slicing:
    def reconstructBst(self, preOrderTraversalValues):
        if not preOrderTraversalValues:
            return None
        # Find the first value greater than root, if any.
        less, more = [], []
        for val in preOrderTraversalValues[1:]:
            if val < preOrderTraversalValues[0]:
                less.append(val)
            else:
                more.append(val)
        return TreeNode(
            preOrderTraversalValues[0],
            self.reconstructBst(less),
            self.reconstructBst(more),
        )


# Update the previous solution to use indexes to determine the portion
# of the array that we are assessing while constructing the current
# subtree, this avoids having to copy all the values, instead they are
# only read twice, one to be used as the root value and one to determine
# where to split the arrays for the left and right subtrees.
#
# Time complexity: O(n) - Values are read at most two times.
# Space complexity: O(n) - The call stack will be of the same size as
# the height of the tree. Best case O(log(n)), worst case O(n).
class Indexing:
    def reconstructBst(self, preOrderTraversalValues):
        # Define a nested function that takes two indexes and builds a
        # subtree with the values between these indexes.
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = preOrderTraversalValues[left]
            # Find the index of the first value equal or greater than
            # the root.
            right_subtree_root_idx = right + 1
            while (
                right_subtree_root_idx > left + 1
                and preOrderTraversalValues[right_subtree_root_idx - 1]
                >= root_val
            ):
                right_subtree_root_idx -= 1
            # The left subtree will go from left + 1 to right_root - 1.
            # The right subtree will go from right_root to right.
            return TreeNode(
                root_val,
                build(left + 1, right_subtree_root_idx - 1),
                build(right_subtree_root_idx, right),
            )

        return build(0, len(preOrderTraversalValues) - 1)


def test():
    executors = [
        Slicing,
        Indexing,
    ]
    tests = [
        [[2, 1, 3], [2, 1, 3]],
        [
            [10, 4, 2, 1, 5, 17, 19, 18],
            [10, 4, 17, 2, 5, None, 19, 1, None, None, None, 18],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = sol.reconstructBst(t[0])
                result = BinaryTree(root).toList()
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
