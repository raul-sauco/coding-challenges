# 684. Redundant Connection
# 🟠 Medium
#
# https://leetcode.com/problems/redundant-connection/
#
# Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

import timeit
from typing import List


# We can use union find to put elements into disjoint sets, if we find
# an edge between two components that are already in the same set, that
# edge is redundant.
#
# Time complexity: O(n) - We visit each node once, union find runs in
# amortized O(1)
# Space complexity: O(n) - The parents array will grow in size linearly
# with the size of the input.
#
# Runtime: 112 ms, faster than 41.16%
# Memory Usage: 14.3 MB, less than 92.03%
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Construct an array with nodes and their parents, at the
        # start, all the nodes are disconnected and each node is
        # its own parent.
        parents = [i for i in range(len(edges) + 1)]
        # Define a function that finds the parent of a given node.
        def findParent(a: int) -> int:
            if parents[a] == a:
                return a
            # Set the parent, following calls will run in O(1)
            parents[a] = findParent(parents[a])
            return parents[a]

        # Define a function that puts two nodes in the same group.
        def group(a: int, b: int) -> None:
            parents[findParent(b)] = findParent(a)

        # Iterate over the input grouping elements into sets.
        for a, b in edges:
            # If this two edges are in the same group, this is the
            # redundant edge, we have already used the non-redundant
            # edge to group this two nodes in the same set.
            if findParent(a) == findParent(b):
                return [a, b]
            # If this nodes were not connected, connect them.
            group(a, b)
        # No need to return anything, the problem guarantees that there
        # will be one, and only one, redundant node, we found and
        # returned it inside the for loop.


def test():
    executors = [Solution]
    tests = [
        [[[1, 2], [1, 3], [2, 3]], [2, 3]],
        [[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]],
        [[[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [3, 6], [3, 7]], [2, 3]],
        [[[2, 7], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]], [3, 7]],
        [
            [
                [9, 10],
                [5, 8],
                [2, 6],
                [1, 5],
                [3, 8],
                [4, 9],
                [8, 10],
                [4, 10],
                [6, 8],
                [7, 9],
            ],
            [4, 10],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findRedundantConnection(t[0])
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
