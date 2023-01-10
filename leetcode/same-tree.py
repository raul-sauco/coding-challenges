# 100. Same Tree
# 🟢 Easy
#
# https://leetcode.com/problems/same-tree/
#
# Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

import timeit
from typing import Optional

from utils.binary_tree import BinaryTree, TreeNode


# Recursive approach. For each node, check that their values are the
# same and the left and right subtrees are also the same.
#
# Time complexity: O(n) - We could visit each node of the input.
# Space complexity: O(n) - The memory used will be the call stack, if
# the tree is balanced it will closer to O(log(n)).
#
# Runtime: 24 ms, faster than 98.30%
# Memory Usage: 13.8 MB, less than 72.95%
class Recursive:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If one of the nodes is null, make sure the other is null as well.
        if not p or not q:
            return not p and not q
        # The node values should be the same and the subtrees on each
        # branch should be the same.
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


# Iterative approach, preorder traversal of both trees checking that the
# values that we pop from the stacks match.
#
# Time complexity: O(n) - We could visit each node of the input.
# Space complexity: O(n) - The memory used will be the two stacks, if
# the tree is balanced it will closer to O(log(n)).
#
# Runtime: 35 ms, faster than 73.56%
# Memory Usage: 13.9 MB, less than 27.10%
class Iterative:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        sp, sq = [p], [q]
        while sp and sq:
            a, b = sp.pop(), sq.pop()
            # We should be popping the same value nodes.
            if a is None or b is None:
                if a or b:
                    return False
                continue
            if a.val != b.val:
                return False
            sp.append(a.right)
            sq.append(b.right)
            sp.append(a.left)
            sq.append(b.left)
        # We have consumed one of the stacks at least, make sure we
        # consumed both at the same time.
        return not sp and not sq


def test():
    executors = [
        Recursive,
        Iterative,
    ]
    tests = [
        [[], [], True],
        [[2], [2], True],
        [[1, 2, 3], [1, 2, 3], True],
        [[1, 2, 1], [1, 1, 1], False],
        [[1, 2], [1, None, 3], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root1 = BinaryTree.fromList(t[0]).getRoot()
                root2 = BinaryTree.fromList(t[1]).getRoot()
                result = sol.isSameTree(root1, root2)
                exp = t[2]
                assert result is exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
