# Branch Sums
# 🟢 Easy
#
# https://www.algoexpert.io/questions/branch-sums
#
# Tags: Binary Tree - Depth-First Search

import timeit

from utils.binary_tree import BinaryTree


# Use recursive depth-first search to travel down the branches keeping
# the sum of the values seen so far on the current branch. If we use
# inorder traversal the branch values will be ordered left-to-right as
# expected by the question.
#
# Time complexity: O(n) - Each node will be visited.
# Space complexity: O(h) - The call stack will grow to the height of the
# tree, which could match O(n).
class Solution:
    def branchSums(self, root):
        res = []

        def dfs(node, total):
            total += node.value
            if not node.left and not node.right:
                res.append(total)
            else:
                if node.left:
                    dfs(node.left, total)
                if node.right:
                    dfs(node.right, total)

        dfs(root, 0)
        return res


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [15, 16, 18, 10, 11]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = BinaryTree.fromList(t[0]).getRoot()
                result = sol.branchSums(root)
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
