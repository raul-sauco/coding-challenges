# Invert Binary Tree
# 🟠 Medium
#
# https://www.algoexpert.io/questions/invert-binary-tree
#
# Tags: Binary Tree

import timeit

from utils.binary_tree import BinaryTree


# Use depth-first search to visit all nodes in the tree, for each node,
# swap the position of its children.
#
# Time complexity: O(n) - We visit each node in the tree and, for each,
# do O(1) work.
# Space complexity: O(h) - The stack can grow to the height of the tree,
# which could be the same as n.
class Iterative:
    def invertBinaryTree(self, root):
        stack = [root]
        while stack:
            current = stack.pop()
            if current:
                current.left, current.right = current.right, current.left
                stack.append(current.left)
                stack.append(current.right)
        return root


def test():
    executors = [Iterative]
    tests = [
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 2, 7, 6, 5, 4, None, None, None, None, None, None, 9, 8],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = BinaryTree(sol.invertBinaryTree(root)).toList()
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
