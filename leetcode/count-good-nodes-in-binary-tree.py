# 1448. Count Good Nodes in Binary Tree
# 🟠 Medium
#
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#
# Tags: Tree - Depth-First Search - Breath-First Search - Binary Tree

import timeit

from data import deserializeStringArrayToBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Use iterative DFS to travel the tree keeping track of the highest
# value that we have seen in the current branch of the exploration.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - Worst case would be a completely unbalanced
# tree, in which case we would push all nodes into the stack.
#
# Runtime: 307 ms, faster than 78.29%
# Memory Usage: 32.6 MB, less than 46.30%
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS stack keeps tuples of (node, largest value seen)
        stack = [(root, root.val)]
        # Keep track of the number of good nodes that we have seen.
        good_nodes = 0
        while stack:
            current, max_seen = stack.pop()
            # If there are no greater nodes between this node and root
            if current.val >= max_seen:
                good_nodes += 1
            # Push the children into the stack.
            if current.left:
                stack.append((current.left, max(max_seen, current.left.val)))
            if current.right:
                stack.append((current.right, max(max_seen, current.right.val)))
        return good_nodes


def test():
    executors = [Solution]
    tests = [
        ["[3,1,4,3,null,1,5]", 4],
        ["[3,3,null,4,2]", 3],
        ["[1]", 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.goodNodes(root)
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
