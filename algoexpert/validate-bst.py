# Validate BST
# 🟠 Medium
#
# https://www.algoexpert.io/questions/validate-bst
#
# Tags: Binary Tree - Binary Search Tree

import timeit

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# Validate the binary search tree using its definition, any nodes left
# of the root must have a smaller value, any nodes to the right must
# have the same or greater value.
#
# Time complexity: O(n) - We will visit at most each node once.
# Space complexity: O(h) - Where h is the height of the tree, for the
# height of the call stack.
class Solution:
    def validateBst(self, tree: TreeNode) -> bool:
        # Write your code here.
        def helper(root, min, max):
            if not root:
                return True
            return (
                min <= root.value < max
                and helper(root.left, min, root.value)
                and helper(root.right, root.value, max)
            )

        return helper(tree, float("-inf"), float("inf"))


def test():
    executors = [Solution]
    tests = [
        ["[1,1]", False],
        ["[2,1,3]", True],
        ["[5,1,4,null,null,3,6]", False],
        ["[10,5,15,2,5,13,22,1,null,null,null,null,14]", True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromStringArray(t[0]).getRoot()
                result = sol.validateBst(root)
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
