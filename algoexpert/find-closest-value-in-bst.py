# Find Closest Value In BST
# 🟢 Easy
#
# https://www.algoexpert.io/questions/find-closest-value-in-bst
#
# Tags: Binary Tree - Binary Search Tree

import timeit

from utils.binary_tree import BinaryTree


# Check the difference of each node visited with the closest value found
# up to that point, also use that value to know if we want to explore
# the left or right subtree.
#
# Time complexity: O(h) - Where h is the height of the tree and it will
# be O(n) in the worst case and O(log(n)) in the best case.
# Space complexity: O(1) - We use constant memory.
class Solution:
    def findClosestValueInBst(self, tree, target):
        closest = tree.value
        current = tree
        while current:
            if abs(current.value - target) < abs(closest - target):
                if current.value == target:
                    return current.value
                closest = current.value
            if current.value > target:
                current = current.left
            else:
                current = current.right
        return closest


def test():
    executors = [Solution]
    tests = [
        [[10, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14], 12, 13],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.findClosestValueInBst(root, t[1])
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
