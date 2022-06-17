# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 28 ms, faster than 96.89% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.9 MB, less than 55.55 % of Python3 online submissions for Invert Binary Tree.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        tmp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = tmp
        return root


def test():
    node1 = TreeNode(val=1)
    node3 = TreeNode(val=3)
    node2 = TreeNode(val=2, left=node1, right=node3)
    node6 = TreeNode(val=6)
    node9 = TreeNode(val=9)
    node7 = TreeNode(val=7, left=node6, right=node9)
    node4 = TreeNode(val=4, left=node2, right=node7)
    sol = Solution()
    result = sol.invertTree(node4)
    assert result == node4
    assert node4.left == node7
    assert node2.right == node1

    result2 = sol.invertTree(None)
    assert result2 == None

    node1 = TreeNode(val=1)
    node3 = TreeNode(val=3)
    node2 = TreeNode(val=2, left=node1, right=node3)
    result3 = sol.invertTree(node2)
    assert result3.right == node1
    assert result3.left == node3

    node1 = TreeNode(val=1, left=node3)
    result4 = sol.invertTree(node1)
    assert result4.right == node3


test()
