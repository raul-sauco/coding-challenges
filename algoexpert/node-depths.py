# Node Depths
# 🟢 Easy
#
# https://www.algoexpert.io/questions/node-depths
#
# Tags: Binary Tree - Depth-First Search

import timeit

from utils.binary_tree import BinaryTree


# Use depth-first search to travel down the tree adding up the sum of
# the node's depth.
#
# Time complexity: O(n) - We will visit each node once.
# Space complexity: O(h) - Where h is the height of the tree and it
# could be from O(log(n)) to O(n).
class Solution:
    def nodeDepths(self, root):
        def dfs(node, depth) -> int:
            if not node:
                return 0
            return (
                depth + dfs(node.left, depth + 1) + dfs(node.right, depth + 1)
            )

        return dfs(root, 0)


def test():
    executors = [Solution]
    tests = [
        [[], 0],
        [[1], 0],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9], 16],
        [[7, 5, 3, 24, 5, 6, 7, 8, 9, 2, 7, 6], 25],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.nodeDepths(root)
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
