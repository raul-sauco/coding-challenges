# 105. Construct Binary Tree from Preorder and Inorder Traversal
# 🟠 Medium
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# Tags: Array - Hash Table - Divide and Conquer - Tree - Binary Tree

import timeit
from typing import List, Optional

from data import TreeNode, serializeTreeToList


# We can use the preorder array to find the root of the current tree.
# We can use that value to split the inorder array:
# - values left of the root belong to the left subtree
# - values right of the root belong to the right subtree
# Keep doing it recursively for the right and left trees
#
# Time complexity: O(n^2) - The number of calls is the same as the
# number of elements in the input, but for each call, we slice the input
# array into two at a O(n) cost.
# Space complexity: O(n*log(n)) - If the tree is well balanced its height
# will be log(n), each call has its own copy of the input arrays at O(n),
# if the tree is not well balanced, then up to O(n) calls for a space
# complexity of O(n^2).
#
# Runtime: 945 ms, faster than 5.01%
# Memory Usage: 351.7 MB, less than 5.38%
class Recursive:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        # Base case
        if not preorder:
            return None
        # Find the root of the tree
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        # Recursively call with sliced lists
        root.left = self.buildTree(preorder[1 : idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1 :], inorder[idx + 1 :])
        return root


# Optimize the previous solution using a hashmap to find the index of
# an element in the inorder array and by passing indexes, instead of
# slicing the arrays, to recursive calls.
#
# Time complexity: O(n) - Now each recursive call does O(1) work and
# there are n calls, where n is the number of elements in the input.
# Space complexity: O(1) - The hashmap has as many elements as there
# are in the input, the call stack will have log(n) to n calls,
# depending on how well balanced the tree is.
#
# Runtime: 111 ms, faster than 88.92%
# Memory Usage: 18.9 MB, less than 88.33%
class RecursiveOptimized:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder:
            return None
        # Find the order of an element in O(1)
        lookup = {x: i for i, x in enumerate(inorder)}
        it = iter(preorder)
        # Define a function that builds a subtree using the array slices
        # between the given boundaries and an iterator to find the root.
        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:  # If not inorder
                return None
            # Root value is at the next position in preorder. O(1)
            val = next(it)
            # Find the index of the root value in the inorder array. O(1)
            idx = lookup[val]
            # Recursive call with modified boundaries.
            return TreeNode(val, build(l, idx - 1), build(idx + 1, r))

        return build(0, len(inorder) - 1)


def test():
    executors = [
        Recursive,
        RecursiveOptimized,
    ]
    tests = [
        [None, None, []],
        [[-1], [-1], [-1]],
        [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = serializeTreeToList(sol.buildTree(t[0], t[1]))
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
