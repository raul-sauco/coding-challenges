# 987. Vertical Order Traversal of a Binary Tree
# 🔴 Hard
#
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
#
# Tags: Hash Table - Tree - Depth-First Search - Breath-First Search -
# Binary Tree

import timeit
from collections import defaultdict, deque
from itertools import chain
from typing import List, Optional, Tuple

from data import deserializeStringArrayToBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# We can use a dictionary of dictionaries to store col => row => [values]
# We can do a tree traversal, for example preorder, keeping the node
# values together with their row and column, as we visit the nodes, we
# add their values to the row and column list that corresponds them.
#
# Time complexity: O(n) - We visit each node of the tree adding them to
# their column/row position in the dictionary. Then we need to sort the
# column keys before iterating through them, then sort the row entries,
# and, if a column/row position has multiple entries, sort them, this
# all costs O(n*log(n)) over the number of entries that we are sorting,
# but that number of entries, number of column, number of rows and
# number of values in the same column/row, can grow at most at a
# O(log(n)) over the number of nodes ratio, therefore, the overall
# complexity is bounded to O(n).
# Space complexity: O(n) - The nested default dictionaries have a max of
# n nodes as leafs.
#
# Runtime: 57 ms, faster than 41.65%
# Memory Usage: 14.2 MB, less than 28.65%
class RecursiveDFS:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Define a dictionary of dictionaries with list values.
        d = defaultdict(lambda: defaultdict(list))
        # Define a function that travels the tree using DFS.
        def dfs(node: TreeNode, row: int, col: int) -> None:
            # Add this node to the dictionary in its position.
            d[col][row].append(node.val)
            # Recursively explore the children.
            if node.left:
                dfs(node.left, row + 1, col - 1)
            if node.right:
                dfs(node.right, row + 1, col + 1)

        # Initial call to obtain the dictionary.
        dfs(root, 0, 0)
        # Convert the dictionary to the expected output shape.
        res = []
        # Iterate over the sorted columns.
        for col in sorted(d.keys()):
            # Store all the column values ordered by row.
            vals = []
            for row in sorted(d[col].keys()):
                for val in sorted(d[col][row]):
                    vals.append(val)
            res.append(vals)
        return res


# The method we use to traverse the tree does not really matter, the key
# to this problem is the way we reorder the nodes in the output. We can
# easily translate the recursive DFS solution to an iterative BFS as
# follows.
#
# View previous solution for complexity analysis details.
# Time complexity: O(n)
# Space complexity: O(n)
#
# Using list comprehension to build the result.
# Runtime: 63 ms, faster than 26.21%
# Memory Usage: 14.2 MB, less than 72.74%
#
# Using itertools.chain to build the result.
# Runtime: 45 ms, faster than 72.60%
# Memory Usage: 14.2 MB, less than 72.74%
class IterativeBFS:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Define a dictionary of dictionaries with list values.
        d = defaultdict(lambda: defaultdict(list))
        # Use a double ended queue for the BFS. The items are tuples of
        # the node with the column it belongs to.
        q = deque([(root, 0)])
        # Initialize the row value, we will use the loops to count the
        # row we are visiting.
        row = -1
        # BFS
        while q:
            # Increase the row number.
            row += 1
            # Visit all the nodes in the level.
            for _ in range(len(q)):
                # Visit each node adding their value to the dictionary.
                node, col = q.popleft()
                d[col][row].append(node.val)
                # Append the children to the next level.
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        # Convert the dictionary to the expected output shape.
        return [
            list(chain(*[sorted(rows) for (_, rows) in sorted(cols.items())]))
            for (_, cols) in sorted(d.items())
        ]
        # Alternatively, using list comprehension.
        # return [
        #     [val for (_, rows) in sorted(cols.items()) for val in sorted(rows)]
        #     for (_, cols) in sorted(d.items())
        # ]


def test():
    executors = [
        RecursiveDFS,
        IterativeBFS,
    ]
    tests = [
        ["[1]", [[1]]],
        ["[3,9,20,null,null,15,7]", [[9], [3, 15], [20], [7]]],
        ["[1,2,3,4,5,6,7]", [[4], [2], [1, 5, 6], [3], [7]]],
        ["[1,2,3,4,6,5,7]", [[4], [2], [1, 5, 6], [3], [7]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                root = deserializeStringArrayToBinaryTree(t[0])
                result = sol.verticalTraversal(root)
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
