# 1008. Construct Binary Search Tree from Preorder Traversal
# 🟠 Medium
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
#
# Tags: Array - Stack - Tree - Binary Search Tree - Monotonic Stack
# Binary Tree

import timeit
from typing import List, Optional

from data import TreeNode, serializeBinaryTreeToStringArray


# A very intuitive solution is to recursively pick the first element of
# the current array as the root of each (sub)tree, then call the
# function again to build the left subtree with elements smaller than
# the root, and the right subtree, with elements greater than the root.
# This solution is easy to read and understand but its time complexity
# suffers because, for each time that we pick one value as a root, we
# copy all other values into two separate arrays.
#
# Time complexity: O(n^2) - Each time that we pick one single value as
# the root of one tree, or subtree, we copy all the remaining values n
# into one of the two subarrays.
# Space complexity: O(n^2) - Each call to bstFromPreorder has its
# own full copy of the input, and in average there will be O(log(n))
# calls, but there could be as many as O(n).
#
# Runtime: 67 ms, faster than 65.88%
# Memory Usage: 13.9 MB, less than 52.59%
class NaiveRecursive:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return (
            TreeNode(
                preorder[0],
                self.bstFromPreorder([x for x in preorder if x < preorder[0]]),
                self.bstFromPreorder([x for x in preorder if x > preorder[0]]),
            )
            if preorder
            else None
        )


# For anyone that has previously solved the problem "Construct binary
# tree from preorder and inorder traversal", we can directly reuse that
# solution given that the problem gives us the preorder and the inorder
# of a BST results in a sorted list of node values.
#
# Time complexity: O(n*log(n)) - Sorting the values to obtain the
# inorder traversal result has the highest cost.
# Space complexity: O(n) - The inorder array will grow to size n, the
# call stack will, in average be of log(n) height, though it could reach
# a height of n in an unbalanced tree.
#
# Runtime: 77 ms, faster than 37.62%
# Memory Usage: 14 MB, less than 13.79%
class PreorderInorder:
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

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.buildTree(preorder, sorted(preorder))


# Optimize memory usage passing a reference to the preorder array and
# removing from it top value that we are using as the root for the
# current tree, or subtree.
#
# Time complexity: O(n) - There will be one call to buildTree for each
# element on preorder.
# Space complexity: O(n) - The call stack will grow to an average of
# O(log(n)) height, but it could grow to O(n).
#
# Runtime: 72 ms, faster than 53.40%
# Memory Usage: 13.8 MB, less than 90.52%
class LinearTime:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Work with the reversed array to pop from the top. We could
        # also use a deque and pop from the left but there is no need.
        return self.buildTree(preorder[::-1], float("inf"))

    def buildTree(self, preorder: List[int], bound: int) -> Optional[TreeNode]:
        if not preorder or preorder[-1] > bound:
            return None
        node = TreeNode(preorder.pop())
        # Building first the left subtree will remove from the array the
        # next smaller element if it exists, otherwise it will return
        # null and move to the right subtree.
        node.left = self.buildTree(preorder, node.val)
        node.right = self.buildTree(preorder, bound)
        return node


# We can also use an iterative approach, create the root node of the
# resulting tree and push it into a stack, then start iterating over the
# remaining elements of the input. When we see an element that is
# smaller than the last element seen, append it as the left child of
# that element and push it into the stack, when we see an element that
# is greater than the top of the stack, keep popping until we find an
# element with a value greater than it, then append the current node as
# the right child of the last element we popped and push the new node,
# not the last popped element, into the stack.
#
# Time complexity: O(n) - We visit each element once and push it/pop it
# to/from the stack a maximum of one time each.
#
# Runtime: 78 ms, faster than 34.19%
# Memory Usage: 14 MB, less than 52.59%
class Iterative:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            # Left children will have a value smaller than their parents.
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            # Right children will have a value greater than their parents.
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root


def test():
    executors = [
        NaiveRecursive,
        PreorderInorder,
        LinearTime,
        Iterative,
    ]
    tests = [
        [[1, 3], "[1,null,3]"],
        [[8, 5, 1, 7, 10, 12], "[8,5,10,1,7,null,12]"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.bstFromPreorder(t[0])
                serialized_result = serializeBinaryTreeToStringArray(result)
                exp = t[1]
                assert serialized_result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
