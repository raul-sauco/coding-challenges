# 951. Flip Equivalent Binary Trees
# 🟠 Medium
#
# https://leetcode.com/problems/flip-equivalent-binary-trees/
#
# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# Use recursion, check that the values at the current node match, if
# they do not, we can return false. If they do match, we need to explore
# the right and left subtrees recursively both flipping them and keeping
# them in their original form.
#
# Time complexity: O(n) - At every node, we will check two branches,
# flipping the children and not flipping the children, but one of them
# will fail immediately O(1) because values are unique, otherwise, it
# would be O(2^n)
# Space complexity: O(h) - Where h is the height of the tree, that is
# the space used by the call stack.
#
# Runtime 0 ms Beats 100%
# Memory 16.58 MB Beats 57%
class Solution:
    def flipEquiv(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        return root1.val == root2.val and (
            (
                self.flipEquiv(root1.left, root2.right)
                and self.flipEquiv(root1.right, root2.left)
            )
            or (
                self.flipEquiv(root1.left, root2.left)
                and self.flipEquiv(root1.right, root2.right)
            )
        )


def test():
    executors = [Solution]
    tests = [
        [[], [], True],
        [[], [1], False],
        [
            [1, 2, 3, 4, 5, 6, None, None, None, 7, 8],
            [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7],
            True,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.flipEquiv(
                    BinaryTree.fromList(t[0]).getRoot(),
                    BinaryTree.fromList(t[1]).getRoot(),
                )
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
