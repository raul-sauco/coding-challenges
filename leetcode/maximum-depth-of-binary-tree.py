# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional

from leetcode.data import TreeNode


# Runtime: 41 ms, faster than 93.90% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.2 MB, less than 74.04 % of Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
