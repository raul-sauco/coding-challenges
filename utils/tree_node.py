from __future__ import annotations

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        # Compatibility with LeetCode naming.
        self.val = val
        # Compatibility with AlgoExpert naming.
        self.value = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "TreeNode({})".format(self.val)
