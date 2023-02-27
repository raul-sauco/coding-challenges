# 427. Construct Quad Tree
# 🟠 Medium
#
# https://leetcode.com/problems/construct-quad-tree/
#
# Tags: Array - Divide and Conquer - Tree - Matrix

import timeit
from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(
        self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# We can create an internal function that takes the boundaries of a
# section of the input matrix, can be the entire matrix, and returns the
# quad node that represents the root of the section. One way to do it
# would be to iterate all the cells in the given section checking if
# they all contain the same value, if they do, the current node is a
# leaf. Another way to do it, is to recursively divide the grid in
# nodes until we get to sections of size 1, which by definition must be
# leaves, then start reconstructing the tree from the roots, when a node
# has all leaf children and they all have the same value, that node
# becomes a leave itself.
#
# Time complexity: O(n^2) - We will visit each cell in the matrix once.
# Space complexity: O(n^2) - We may create a node for each cell in the
# matrix. The call stack will be log(n) as well but that is simplified.
#
# Runtime 130 ms Beats 38.29%
# Memory 14.8 MB Beats 69.97%
class AllocateMemory:
    def construct(self, grid: List[List[int]]) -> Node:
        # A function that takes a top corner and a size and returns the
        # quad node for the section of the matrix that it defines.
        def getNode(top: int, l: int, n: int) -> Node:
            # Base case, a node with a single cell is a leaf.
            if n == 1:
                return Node(bool(grid[top][l]), True)
            # Otherwise split in 4 and compute its leaves.
            s = n // 2
            tl = getNode(top, l, s)
            tr = getNode(top, l + s, s)
            bl = getNode(top + s, l, s)
            br = getNode(top + s, l + s, s)

            # Check if we can convert this node to a leave.
            children = (tl, tr, bl, br)
            if all([c.isLeaf for c in children]) and (
                all([c.val for c in children])
                or all([not c.val for c in children])
            ):
                return Node(tl.val, True)
            return Node(True, False, tl, tr, bl, br)

        return getNode(0, 0, len(grid))


# Similar approach to the previous solution but, instead of creating a
# node instance for each leave, we create two, false and true, and
# reuse one of them for each leave node.
#
# Time complexity: O(n^2) - We will visit each cell in the matrix once.
# Space complexity: O(n^2) - We may create a node each for non-leave
# cell in the matrix, which still has a linear relation with the number
# of cells, even though we are reusing nodes for leaves.
#
# Runtime 109 ms Beats 89.53%
# Memory 14.8 MB Beats 69.97%
class ReuseMemory:
    def construct(self, grid: List[List[int]]) -> Node:
        # Create two leaf nodes that can be reused.
        falseLeaf = Node(False, True)
        trueLeaf = Node(True, True)
        # A function that takes a top corner and a size and returns the
        # quad node for the section of the matrix that it defines.
        def getNode(top: int, l: int, n: int) -> Node:
            # Base case, a node with a single cell is a leaf.
            if n == 1:
                return trueLeaf if grid[top][l] else falseLeaf
            # Otherwise split in 4 and compute its leaves.
            s = n // 2
            tl = getNode(top, l, s)
            tr = getNode(top, l + s, s)
            bl = getNode(top + s, l, s)
            br = getNode(top + s, l + s, s)

            # Check if we can convert this node to a leave.
            children = (tl, tr, bl, br)
            if all([c.isLeaf for c in children]) and (
                all([c.val for c in children])
                or all([not c.val for c in children])
            ):
                return trueLeaf if tl.val else falseLeaf
            return Node(True, False, tl, tr, bl, br)

        return getNode(0, 0, len(grid))


def test():
    executors = [
        AllocateMemory,
        ReuseMemory,
    ]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.construct(t[0])
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


# test()
print(f"\033[93m» This file does not have any tests!\033[0m")
