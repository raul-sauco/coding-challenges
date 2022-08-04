# 173. Binary Search Tree Iterator
# 🟠 Medium
#
# https://leetcode.com/problems/binary-search-tree-iterator/
#
# Tags: Stack - Tree - Design - Binary Search Tree - Binary Tree - Iterator

import timeit
from collections import deque
from typing import List, Optional

from data import deserializeStringArrayToBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# If we are not asked to maintain the BST structure internally, and are
# ever only going to be asked to iterate over the tree, there is no
# reason to. The easiest way is to get a list of the tree values inorder
# and pop elements when the next method is called.
#
# Time complexity: O(n) - for the init method, O(1) for the next and
# hasNext methods.
# Space complexity: O(n) - We keep all elements in memory.
#
# Runtime: 107 ms, faster than 61.24%
# Memory Usage: 20.1 MB, less than 70.78%
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # Store the values of the tree in inorder using a deque. If
        # we couldn't use a deque it would be the same to store the
        # elements reversed in a list and pop from the right.
        self.nums = deque(self.getValues(root))

    # Get the values of a tree inorder.
    def getValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return (
            self.getValues(root.left) + [root.val] + self.getValues(root.right)
        )

    def next(self) -> int:
        return self.nums.popleft()

    def hasNext(self) -> bool:
        return len(self.nums) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


def test():
    executors = [BSTIterator]
    tests = [
        [
            "[7,3,15,null,null,9,20]",
            [
                "next",
                "next",
                "hasNext",
                "next",
                "hasNext",
                "next",
                "hasNext",
                "next",
                "hasNext",
            ],
            [3, 7, True, 9, True, 15, True, 20, False],
        ],
        ["[]", ["hasNext"], [False]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                root = deserializeStringArrayToBinaryTree(t[0])
                sol = executor(root)
                for i, call in enumerate(t[1]):
                    result = getattr(sol, call)()
                    exp = t[2][i]
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
