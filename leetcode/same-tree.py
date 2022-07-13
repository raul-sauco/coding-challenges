# https://leetcode.com/problems/same-tree/

# Tags: Tree - Depth-First Search - Binary Tree

import timeit
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree


# Recursive approach. For each node, check that their values are the same and the left and right subtrees are also
# the same.
#
#
# Time complexity: O(n) - we will visit each node of the tree once
# Space complexity: O(log(n)) if balanced O(n) if completely unbalanced - the call stack depth maxes at the height of the tree
#
# Runtime: 55 ms, faster than 28.36% of Python3 online submissions for Same Tree.
# Memory Usage: 14 MB, less than 29.45% of Python3 online submissions for Same Tree.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If one of the nodes is null, make sure the other is null as well
        if not p or not q:
            return not p and not q
        # The node values should be the same and the subtrees on each branch should be the same
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def test():
    p1 = deserializeStringArrayToBinaryTree("[1,2,3]")
    q1 = deserializeStringArrayToBinaryTree("[1,2,3]")
    p2 = deserializeStringArrayToBinaryTree("[1,2]")
    q2 = deserializeStringArrayToBinaryTree("[1,null,2]")
    p3 = deserializeStringArrayToBinaryTree("[1,2,1]")
    q3 = deserializeStringArrayToBinaryTree("[1,1,2]")
    executors = [Solution]
    tests = [
        [p1, q1, True],
        [p2, q2, False],
        [p3, q3, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.isSameTree(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
