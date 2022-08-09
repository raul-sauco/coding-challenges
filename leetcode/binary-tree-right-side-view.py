# 199. Binary Tree Right Side View
# 🟠 Medium
#
# https://leetcode.com/problems/binary-tree-right-side-view/
#
# Tags: Tree - Depth-First Search - Breath-First Search - Binary Tree

import timeit
from collections import deque
from typing import List, Optional

from data import TreeNode, deserializeStringArrayToBinaryTree

# 1e4 calls:
# » BFSIdiomatic        0.02233   seconds
# » BFS                 0.02276   seconds
# » BFSLC               0.02193   seconds

# Intuition, the problem asks for the value of the right-most node of
# each level, ordered by level, this is an almost perfect fit for BFS.
# We can explore the tree and ignore all values except the last one for
# each level.
#
# Time complexity O(n) - we visit each node once.
# Space complexity O(n) - one level at a time in the queue, in a binary
# tree, this could be a max of n/2 nodes.
#
# Runtime: 70 ms, faster than 9.60%
# Memory Usage: 13.9 MB, less than 69.82%
class BFS:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case.
        if not root:
            return []
        values = []
        # Initialize a queue with the root node, level 0.
        queue = deque([root])
        # While the queue has nodes. At this point it will have exactly
        # the next complete level.
        while queue:
            values.append(queue[-1].val)
            # Empty the queue of the current level's nodes.
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        # The List contains the right-most value of each level.
        return values


# Similar version to BFS but using a more pythonic way to reassign a
# whole level to the queue in one line.
#
# Time complexity O(n) - we visit each node once
# Space complexity O(n) - one level at a time in the queue, in a binary
# tree, this could be a max of n/2 nodes.
#
# Runtime: 74 ms, faster than 5.96%
# Memory Usage: 13.9 MB, less than 69.82%
class BFSIdiomatic:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If we don't have a root node, return an empty array
        if not root:
            return []
        # Store the values of the nodes we visit
        result = []
        # Queue. Since we are not popping left, but reassigning the
        # whole list for each level, we don't need to use a deque(), a
        # regular list works the same.
        level = [root]
        # For each loop, we will have exactly one level in the queue
        while level:
            # For each level, push the value of the last node to the
            # result array.
            result.append(level[-1].val)
            # The rest of the level does not interest us, overwrite it
            # with the next level.
            level = [
                child
                for node in level
                for child in (node.left, node.right)
                if child
            ]
        # Return the values of the right-most nodes of each level
        # from top to bottom.
        return result


# Similar to the two previous solution but use list comprehension to
# build the tree levels.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - We store one level at a time in the queue.
#
# Runtime: 48 ms, faster than 61.68%
# Memory Usage: 13.8 MB, less than 98.06%
class BFSLC:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            level = [root]
            while level:
                result += (level[-1].val,)
                level = [
                    child
                    for node in level
                    for child in (node.left, node.right)
                    if child
                ]
        return result


def test():
    executors = [
        BFSIdiomatic,
        BFS,
        BFSLC,
    ]
    tests = [
        [
            deserializeStringArrayToBinaryTree("[1,2,3,null,5,null,4]"),
            [1, 3, 4],
        ],
        [deserializeStringArrayToBinaryTree("[1,null,3]"), [1, 3]],
        [deserializeStringArrayToBinaryTree("{}"), []],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.rightSideView(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
