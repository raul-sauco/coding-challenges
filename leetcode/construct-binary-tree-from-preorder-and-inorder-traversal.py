# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
# Time complexity: O(n) The number of calls == len(preorder) == len(inorder)
# Space complexity: O(log(n)) if the tree is well balanced to O(n) if it is totally unbalanced
#
# Runtime: 945 ms, faster than 5.01% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 351.7 MB, less than 5.38% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
class Recursive:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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


def test():
    executors = [Recursive]
    tests = [
        [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]],
        [[-1], [-1], [-1]],
        [None, None, []],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = serializeTreeToList(sol.buildTree(t[0], t[1]))
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
