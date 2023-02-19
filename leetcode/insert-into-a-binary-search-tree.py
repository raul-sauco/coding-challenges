# 701. Insert into a Binary Search Tree
# 🟠 Medium
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
#
# Tags: Tree - Binary Search Tree - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# Travel through the tree choosing to go right or left based on node
# values until we find the leave below which we will need to insert
# the new node.
#
# Time Complexity: Best: O(log(n)) Worst: O(n) - We will travel the
# entire height of the tree, ideally, it would be a well balanced tree
# and its height would be log(n), but a skewed tree could have a height
# of n, since we are not doing any balancing, after multiple inserts,
# depending on the order in which the values were inserted, the tree
# could become skewed.
# Space complexity: Best: O(log(n)) Worst: O(n) - Each node that we
# visit will add one call to the call stack, we could improve it to O(1)
# using an iterative method because we only need to keep a pointer to
# one node.
#
# Runtime 136 ms Beats 73.62%
# Memory 16.9 MB Beats 90.27%
class Solution:
    def insertIntoBST(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node

        def ins(child, parent) -> None:
            if child.val < parent.val:
                if parent.left:
                    ins(child, parent.left)
                else:
                    parent.left = child
            else:
                if parent.right:
                    ins(child, parent.right)
                else:
                    parent.right = child

        ins(node, root)
        return root


def test():
    executors = [Solution]
    tests = [
        [[4, 2, 7, 1, 3], 5, [1, 2, 3, 4, 5, 7]],
        [[40, 20, 60, 10, 30, 50, 70], 25, [10, 20, 25, 30, 40, 50, 60, 70]],
        [
            [4, 2, 7, 1, 3, None, None, None, None, None, None],
            5,
            [1, 2, 3, 4, 5, 7],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result_root = sol.insertIntoBST(root, t[1])
                result = BinaryTree(result_root).inOrderTraverse()
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
