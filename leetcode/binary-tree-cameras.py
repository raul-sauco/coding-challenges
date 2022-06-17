# https://leetcode.com/problems/binary-tree-cameras/


from typing import Optional
from data import TreeNode

# Runtime: 72 ms, faster than 42.26% of Python3 online submissions for Binary Tree Cameras.
# Memory Usage: 14.3 MB, less than 22.00 % of Python3 online submissions for Binary Tree Cameras.


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # A node can be in one of three states
        camera = 0
        not_covered = 1
        covered = 2
        self.total_cameras = 0

        def dfs(node: Optional[TreeNode]) -> int:
            # If node is null, return covered, for leafs, both children will be covered
            if not node:
                return covered

            # Calculate the children' state
            left = dfs(node.left)
            right = dfs(node.right)

            # If a child is not_covered, become a camera
            if left == not_covered or right == not_covered:
                self.total_cameras += 1
                return camera

            # Else if a child is a camera, return covered
            if left == camera or right == camera:
                return covered
            else:
                return not_covered

        if dfs(root) == not_covered:
            self.total_cameras += 1

        return self.total_cameras


def test():
    sol = Solution()
    node4 = TreeNode(val=4)
    node3 = TreeNode(val=3)
    node1 = TreeNode(val=1, left=node3, right=node4)
    node0 = TreeNode(val=0, left=node1)

    result = sol.minCameraCover(node0)
    assert result == 1, f'{result} != 1'

    node0 = TreeNode(val=0)
    result = sol.minCameraCover(node0)
    assert result == 1, f'{result} != 1'

    node8 = TreeNode(val=8)
    node5 = TreeNode(val=5, right=node8)
    node3 = TreeNode(val=3, left=node5)
    node1 = TreeNode(val=1, left=node3)
    node1 = TreeNode(val=1, left=node3)
    node0 = TreeNode(val=0, left=node1)
    result = sol.minCameraCover(node0)
    assert result == 2, f'{result} != 2'


test()
