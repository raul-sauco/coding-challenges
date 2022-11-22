# Min Height BST
# 🟠 Medium
#
# https://www.algoexpert.io/questions/min-height-bst
#
# Tags: Binary Search Trees

import timeit

from utils.binary_tree import BinaryTree

# Use a helper function to avoid array slicing. Pick the middle element
# of the array section that we are currently evaluating as the root of
# the tree that we are constructing then use the section to the left to
# construct its left sub-tree and the section to the right to construct
# its right subtree.
#
# Time complexity: O(n) - We assess each node once.
# Space complexity: O(log(n)) - The height of the call stack.
class Solution:
    def minHeightBst(self, array):
        def insert(l, r):
            if l == r:
                return BST(array[l])
            else:
                m = (l + r) // 2
                tree = BST(array[m])
                if l < m:
                    tree.left = insert(l, m - 1)
                if m < r:
                    tree.right = insert(m + 1, r)
            return tree

        return insert(0, len(array) - 1)


# Updated the original tree to have a val attribute instead of a val
# attribute.
class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BST(val)
            else:
                self.right.insert(val)


def test():
    executors = [Solution]
    tests = [
        [[1], [1]],
        [[1, 2], [1, None, 2]],
        [[1, 2, 3], [2, 1, 3]],
        [
            [1, 2, 5, 7, 10, 13, 14, 15, 22],
            [
                10,
                2,
                14,
                1,
                5,
                13,
                15,
                None,
                None,
                None,
                7,
                None,
                None,
                None,
                22,
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = sol.minHeightBst(t[0])
                result = BinaryTree(root).toList()
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
