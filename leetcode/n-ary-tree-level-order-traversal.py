# 429. N-ary Tree Level Order Traversal
# 🟠 Medium
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
#
# Tags: Tree - Breath-First Search

import timeit
from collections import deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# We want all children in a level inside the same list, the requirements
# match perfectly BFS.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - If we don't consider the input and output and
# only look at the queue, it can grow to the size of a level. The last
# level of the tree could contain half the nodes of the tree O(n/2).
#
# Runtime: 74 ms, faster than 61.90%
# Memory Usage: 16.1 MB, less than 50.08%
class IterativeBFS:
    def levelOrder(self, root: Node) -> List[List[int]]:
        # Root could be null, pushing None into the deque would make it
        # not null.
        if not root:
            return []
        # Store the result in an array of arrays. Initially we don't
        # know the number of nested arrays, the height of the tree, or
        # their size, the n-grade of the tree.
        res = []
        # Use a double ended queue for BFS. Add the root.
        q = deque([root])
        # While we have a level in the queue.
        while q:
            # Use a fresh array for each level.
            level = []
            # Iterate over the current number of nodes in the queue.
            for _ in range(len(q)):
                # Get the next node in the queue.
                current = q.popleft()
                # Append its value to the level values.
                level.append(current.val)
                # Iterate over its children appending them to the queue
                # to be processed as part of the next level.
                q.extend(current.children)
            # Append the current level to the result.
            res.append(level)
        return res


# Similar to the previous solution but use list comprehension to
# simplify the logic.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The queue will hold a full level at a time.
#
# Runtime: 91 ms, faster than 35.15%
# Memory Usage: 16 MB, less than 94.71%
class IdiomaticBFS:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        # We can use a regular list instead of queue because we are not
        # popping from the left.
        res, q = [], [root]
        while q:
            # Append the entire level's values to the result.
            res.append([node.val for node in q])
            # Construct a new list with the current nodes children.
            q = [child for node in q for child in node.children if child]
        return res


def test():
    executors = [
        IterativeBFS,
        IdiomaticBFS,
    ]
    tests = [
        ["[]", []],
        ["[1,null,3,2,4,null,5,6]", [[1], [3, 2, 4], [5, 6]]],
        [
            "[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,"
            + "11,null,12,null,13,null,null,14]",
            [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.levelOrder(t[0])
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
