# 106. Construct Binary Tree from Inorder and Postorder Traversal
# 🟠 Medium
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#
# Tags: Array - Hash Table - Divide and Conquer - Tree - Binary Tree

import timeit
from typing import List, Optional

from utils.binary_tree import BinaryTree, TreeNode


# We know that the root of the tree is the value at the end of the
# postorder array, we can use that value to find the root in the
# inorder array, any value to its left belongs to the left sub-tree, any
# value to the right, to the right sub-tree. The naive way to use that
# is to find the root, its position in the inorder array, and call the
# function recursively using array slices.
#
# Time complexity: O(n^2) - For each call, we iterate the elements to
# find the position of root in inorder, and iterate them to create the
# array slices.
# Space complexity: O(h) - The call stack will have the same height as
# the tree, best O(log(n)), worst O(n).
#
# Runtime 177 ms Beats 43.9%
# Memory 88.6 MB Beats 35.61%
class Solution:
    def buildTree(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        # If we only have one node, return that.
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        # The root is the last element of the postorder.
        # Find that element in the inorder.
        idx = inorder.index(postorder[-1])
        return TreeNode(
            postorder[-1],
            left=self.buildTree(inorder[:idx], postorder[:idx]),
            right=self.buildTree(
                inorder[idx + 1 :], postorder[idx : len(postorder) - 1]
            ),
        )


# Improve the previous solution avoiding having to iterate the array to
# find the position of the root value in the inorder array by using a
# hashmap, then pass indexes instead of slicing the arrays. This
# completely avoids iterating the arrays in each call and only does O(1)
# operations instead.
#
# Time complexity: O(n) - For each call, we access one value in a
# hashmap and pop one value from the end of an array, all of them O(1).
# Space complexity: O(h) - The call stack will have the same height as
# the tree, best O(log(n)), worst O(n).
#
# Runtime 51 ms Beats 97.18%
# Memory 18.8 MB Beats 93.60%
class Optimized:
    def buildTree(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        # A dictionary of value to index in the inorder array.
        d = {val: idx for idx, val in enumerate(inorder)}
        # A helper function that builds a subtree using the array
        # elements between l and r in inorder.
        def helper(l: int, r: int) -> Optional[TreeNode]:
            # If we don't have any elements, return null.
            if l > r:
                return None
            idx = d[postorder[-1]]
            return TreeNode(
                postorder.pop(),
                right=helper(idx + 1, r),
                left=helper(l, idx - 1),
            )

        return helper(0, len(inorder) - 1)


def test():
    executors = [
        Solution,
        Optimized,
    ]
    tests = [
        [[-1], [-1], [-1]],
        [[9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.buildTree(t[0], t[1])
                result = BinaryTree(result).toList()
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
