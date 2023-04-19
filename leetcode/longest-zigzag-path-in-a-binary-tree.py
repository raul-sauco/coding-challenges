# 1372. Longest ZigZag Path in a Binary Tree
# 🟠 Medium
#
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
#
# Tags: Dynamic Programming - Tree - Depth-First Search - Binary Tree

import timeit
from enum import Enum
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# We could use an enum to make the code easier to read but it makes it
# a little less efficient because it need to create the object.
class Direction(Enum):
    RIGHT = "right"
    LEFT = "left"


# Use any traversal method to visit all nodes, for each node, record the
# direction that we used to travel there and the length of the zig-zag
# path to it, the path will continue to grow for one of its children and
# will restart for the other one.
#
# Time complexity: O(n) - We visit all nodes and do O(1) work for each.
# Space complexity: O(n) - The stack can grow to size n.
#
# Runtime 367 ms Beats 89.1%
# Memory 26.7 MB Beats 95.60%
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Traverse the tree, for each node, keep its position in a zig
        # zag path and the direction that we traveled to get there.
        stack, res = [], 0
        if root.left:
            stack.append((root.left, Direction.LEFT, 1))
        if root.right:
            stack.append((root.right, Direction.RIGHT, 1))
        while stack:
            current, last_dir, path_length = stack.pop()
            if path_length > res:
                res = path_length
            if current.left:
                stack.append(
                    (
                        current.left,
                        Direction.LEFT,
                        path_length + 1 if last_dir == Direction.RIGHT else 1,
                    )
                )
            if current.right:
                stack.append(
                    (
                        current.right,
                        Direction.RIGHT,
                        path_length + 1 if last_dir == Direction.LEFT else 1,
                    )
                )
        return res


def test():
    executors = [Solution]
    tests = [
        [[1], 0],
        [[1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4],
        [
            [
                1,
                None,
                1,
                1,
                1,
                None,
                None,
                1,
                1,
                None,
                1,
                None,
                None,
                None,
                1,
                None,
                1,
            ],
            3,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.longestZigZag(root)
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
