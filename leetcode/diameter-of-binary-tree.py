# https://leetcode.com/problems/diameter-of-binary-tree/

# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# We need to find the longest possible path between nodes, from each sub-tree root, we check if the longest path is in the subtree
# or it would come from the parent node
#
# Time complexity O(n) - we need to visit every node once
# Space complexity O(log(n)) - At most, the call stack will be as long as the tree is deep
#
# Runtime: 70 ms, faster than 52.49% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16.4 MB, less than 10.03% of Python3 online submissions for Diameter of Binary Tree.
class DFS:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            # If this node is not null, return the sum of the longest path found in each sub-tree plus the node
            # traveled to get here
            left, right = dfs(root.left), dfs(root.right)

            # If the subtree with this node as root has a longer path between nodes than from the root,
            # update it
            combined = left + right
            if combined > self.max_length:
                self.max_length = combined

            # The longest path from the parent through this node will be going through the longest branch
            return 1 + max(left, right)

        dfs(root)
        return self.max_length


def test():
    root1 = deserializeStringArrayToBinaryTree("[1,2,3,4,5]")
    root2 = deserializeStringArrayToBinaryTree("[1,2]")
    executors = [DFS]
    tests = [
        [root1, 3],
        [root2, 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.diameterOfBinaryTree(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
# drawTree(deserializeStringArrayToBinaryTree("[6,2,8,0,4,7,9,null,null,3,5]"))
