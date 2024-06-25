# 538. Convert BST to Greater Tree
# 🟠 Medium
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/
#
# Tags: Tree - Depth-First Search - Binary Search Tree - Binary Tree

import timeit

from utils.binary_tree import BinaryTree, TreeNode


# Do a right-to-left iterative inorder traverse.
#
# Time complexity: O(n)
# Space complexity: O(h)
#
# Runtime 44 ms Beats 8%
# Memory 16.53 MB Beats 31%
class It:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        node, s = root, 0
        while node or stack:
            if node:
                stack.append(node)
                node = node.right
                continue
            node = stack.pop()
            s += node.val
            node.val = s
            node = node.left
        return root


# Do a right-to-left recursive inorder traverse.
#
# Time complexity: O(n)
# Space complexity: O(h)
#
# Runtime 37 ms Beats 52%
# Memory 16.51 MB Beats 31%
class Rec:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
            nonlocal s
            dfs(node.right)
            s += node.val
            node.val = s
            dfs(node.left)

        s = 0
        dfs(root)
        return root


def test():
    executors = [
        It,
        Rec,
    ]
    tests = [
        [[], []],
        [[0, None, 1], [1, None, 1]],
        [
            [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
            [
                30,
                36,
                21,
                36,
                35,
                26,
                15,
                None,
                None,
                None,
                33,
                None,
                None,
                None,
                8,
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                resultRoot = sol.bstToGst(BinaryTree.fromList(t[0]).getRoot())
                result = BinaryTree(resultRoot).toList()
                exp = t[1]
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
