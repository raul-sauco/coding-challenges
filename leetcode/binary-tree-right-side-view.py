# https://leetcode.com/problems/binary-tree-right-side-view/


import timeit
from collections import deque
from typing import List, Optional

from data import TreeNode, deserializeStringArrayToBinaryTree

# Tags: Tree - Depth-First Search - Breath-First Search - Binary Tree

# 1e4 calls:
# » BFSIdiomatic        0.01957   seconds
# » BFS                 0.02014   seconds

# Intuition, the problem asks for the value of the right-most node of each level, ordered by level, this is an almost
# perfect fit for BFS. We can explore the tree and ignore all values except the last one for each level.
#
# Time complexity O(n) - we visit each node once
# Space complexity O(n) - one level at a time in the queue, in a binary tree, this could be a max of n/2 nodes.
#
# Runtime: 70 ms, faster than 9.60% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 13.9 MB, less than 69.82% of Python3 online submissions for Binary Tree Right Side View.
class BFS:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        values = []

        # Initialize a queue with the root node, level 0
        queue = deque([root])

        # While the queue has nodes. At this point it will have exactly the next complete level.
        while queue:
            values.append(queue[-1].val)

            # Empty the queue of the current level's nodes
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # The List contains the right-most value of each level
        return values


# Similar version to BFS but using a more pythonic way to reassign a whole level to the queue
# in one line
#
# Time complexity O(n) - we visit each node once
# Space complexity O(n) - one level at a time in the queue, in a binary tree, this could be a max of n/2 nodes.
#
# Runtime: 74 ms, faster than 5.96% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 13.9 MB, less than 69.82% of Python3 online submissions for Binary Tree Right Side View.
class BFSIdiomatic:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # If we don't have a root node, return an empty array
        if not root:
            return []

        # Store the values of the nodes we visit
        result = []

        # Queue. Since we are not popping left, but reassigning the whole list for each level, we
        # don't need to use a deque(), a regular list works the same
        level = [root]

        # For each loop, we will have exactly one level in the queue
        while level:

            # For each level, push the value of the last node to the result array
            result.append(level[-1].val)

            # The rest of the level does not interest us, overwrite it with the next level
            level = [child for node in level for child in (node.left, node.right) if child]

        # Return the values of the right-most nodes of each level top-bottom
        return result


def test():
    executors = [BFSIdiomatic, BFS]
    tests = [
        [deserializeStringArrayToBinaryTree("[1,2,3,null,5,null,4]"), [1, 3, 4]],
        [deserializeStringArrayToBinaryTree("[1,null,3]"), [1, 3]],
        [deserializeStringArrayToBinaryTree("{}"), []],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e4"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.rightSideView(t[0])
                expected = t[1]
                assert (
                    result == expected
                ), f"\033[93m» {result} <> {expected}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
