# 108. Convert Sorted Array to Binary Search Tree
# 🟢 Easy
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#
# Tags:

import timeit
from typing import List, Optional

from data import serializeTreeToList


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Since the list is sorted, we can find the middle in O(1) and use it
# as the root of the BST, then recursively use the left and right sides
# of the array to build the left and right subtrees.
#
# Time complexity: O(n*log(n)) - We visit each element of the list to
# return a BST node. Then split the array for the recursive calls,
# splitting the array costs O(log(n))
# Space complexity: O(n) - The call stack will grow in a linear relation
# to the size of the input.
#
# Runtime: 136 ms, faster than 40.30%
# Memory Usage: 15.5 MB, less than 83.29%
class Slicing:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case, empty array.
        if not nums:
            return None
        # Base case, only one node.
        if len(nums) == 1:
            return TreeNode(nums[0])

        # In any other case, split the array by the mid point.
        mid = len(nums) // 2
        # Recursively create the left and right sub-trees, they could be
        # empty.
        return TreeNode(
            nums[mid],
            left=self.sortedArrayToBST(nums[:mid]),
            right=self.sortedArrayToBST(nums[mid + 1 :]),
        )


# To avoid the cost of slicing the array in each call, we can define a
# helper function that works similarly but takes left and right pointers
# instead of a full array.
#
# Time complexity: O(n) - We visit each element but each visit now costs
# O(1) because we are not splitting the array.
# Space complexity: O(n) - The call stack.
#
# Runtime: 133 ms, faster than 44.83%
# Memory Usage: 15.6 MB, less than 32.22%
class Pointers:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            # If the list is empty, return None
            if left == right:
                return None
            if left + 1 == right:
                return TreeNode(nums[left])
            # Create a subtree with mid as root.
            mid = (left + right) // 2
            return TreeNode(nums[mid], dfs(left, mid), dfs(mid + 1, right))

        # Initial call
        return dfs(0, len(nums))


def test():
    executors = [Slicing, Pointers]
    tests = [
        [
            [-10, -3, 0, 5, 9],
            [0, -3, 9, -10, None, 5],
            # [0,-10,5,None,-3,None,9],
        ],
        [
            [1, 3],
            [3, 1],
            # [1, None, 3],
        ],
        [[], []],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.sortedArrayToBST(t[0])
                result = serializeTreeToList(result)
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {i} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
