# 222. Count Complete Tree Nodes
# 🟠 Medium
#
# https://leetcode.com/problems/count-complete-tree-nodes/
#
# Tags: Binary Search - Depth-First Search - Tree - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree
from utils.tree_node import TreeNode


# Counting the number of nodes in the tree can be done in two steps;
# determining the height of the tree and determining how many nodes
# there are on the last level, the first we can do finding the leftmost
# node in the last level, since we know that one will always have to be
# present, then we can do binary search on the last level to find the
# rightmost node.
#
# Time complexity: O(log(n)) - We travel the height of the tree reducing
# the search space in half every time.
# Space complexity: O(1) - Only pointers are used.
#
# Runtime: 83 ms, faster than 93.94%
# Memory Usage: 21.4 MB, less than 46.74%
class BinarySearch:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return 1
        # Find the height of the tree.
        height, current = 0, root
        while current.left:
            height += 1
            current = current.left
        # The minimum and maximum number of nodes in the last level.
        l, r = 0, 2**height - 1

        # Check whether the given index element on the last level of a
        # binary tree of height h is present.
        def dfs(root: Optional[TreeNode], idx: int, h: int) -> bool:
            if h == 0:
                return False if not root else True
            mid = (2**h - 1) // 2
            if idx > mid:
                return dfs(root.right, idx - mid - 1, h - 1)
            else:
                return dfs(root.left, idx, h - 1)

        # Binary search the index of the first missing node on the last
        # level.
        while l <= r:
            mid = (l + r) // 2
            # If this node exists in the tree, adjust the search.
            if dfs(root, mid, height):
                l = mid + 1
            else:
                r = mid - 1
        return l + (2**height) - 1


# The binary search solution is more intuitive, for me at least, but the
# problem can be solved with less code using a divide and conquer
# approach, from the given root, we check if the height traveling always
# left is the same as the height traveling always right, which is an
# easy way to check if the last level of the tree is full, if the level
# is full, we know that the tree is a perfect tree and has 2**h - 1
# nodes. If the tree is not full, we recursively call the function with
# its left and right subtree, since at each level, one of the subtrees
# will be a full tree, we will get a solution for half the problem in
# log(n) and will call the function log(n) times at a log(n) cost.
#
# Time complexity: O(log(n)^2) - Each call costs log(n) and there are
# log(n) calls.
# Space complexity: O(log(n)) - The call stack will grow to the height
# of the tree.
#
# Runtime: 141 ms, faster than 72.51%
# Memory Usage: 21.5 MB, less than 46.74%
#
# https://leetcode.com/problems/count-complete-tree-nodes/solutions/2815375/
class DivideAndConquer:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Compute the height of the leftmost and rightmost branches,
        # this checks if the last level is full.
        left = right = root
        l = r = 1
        while left := left.left:
            l += 1
        while right := right.right:
            r += 1
        # If the last level is full, this is a perfect tree and its size
        # is 2^h - 1 nodes.
        if l == r:
            return 2**l - 1
        # If the tree is not full, the number of nodes can be computed
        # as the number of nodes in its left and right subtrees plus the
        # root node. Since one of the subtrees is guaranteed to be
        # a perfect tree, the algorithm reduces the search space in half
        # at each step.
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


def test():
    executors = [
        BinarySearch,
        DivideAndConquer,
    ]
    tests = [
        [[], 0],
        [[1], 1],
        [[1, 2, 3, 4, 5, 6], 6],
        [[1, 2, 3, 4, 5, 6, 7], 7],
        [[1, 2, 3, 4, 5, 6, 7, 8], 8],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9], 9],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.countNodes(root)
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
