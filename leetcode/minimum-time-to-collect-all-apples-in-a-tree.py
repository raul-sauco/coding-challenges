# 1443. Minimum Time to Collect All Apples in a Tree
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
#
# Tags: Hash Table - Tree - Depth-First Search - Breadth-First Search

import timeit
from collections import defaultdict
from typing import List


# Find the parent of each node then travel upwards from any node that
# is an apple until we either get to the root or to a node that we have
# visited already, each edge we travel adds 2 to the result because we
# will need to travel it in two directions when we travel from the root
# to collect all apples.
#
# Time complexity: O(n) - We visit each node several times, to form the
# adjacency list, the parents array and finding the paths to collect
# the apples.
# Space complexity: O(n) - The neighbors set will have as many entries
# as edges in the tree, in a tree, the number of edges is n-1. The
# parents array is size n.
#
# Runtime 711 ms Beats 83.33%
# Memory 60.4 MB Beats 18.59%
class Solution:
    def minTime(
        self, n: int, edges: List[List[int]], hasApple: List[bool]
    ) -> int:
        # An array with the parent of each graph, 0 is the root.
        parents = [None] * n
        # Build an adjacency list of nodes.
        neighbors = [[] for _ in range(n)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        # DFS to find every node's parent.
        stack = [0]
        while stack:
            current = stack.pop()
            for neighbor in neighbors[current]:
                if neighbor == parents[current]:
                    continue
                parents[neighbor] = current
                stack.append(neighbor)
        # Mark nodes that we have visited at some point already.
        visited = [False] * n
        # Number of edges that we have to travel.
        res = 0
        # A function that travels from a given node towards the root
        # We need to visit any nodes that have apples.
        for i in reversed(range(n)):
            if hasApple[i] is False:
                continue
            current = i
            while not visited[current]:
                visited[current] = True
                if current == 0:
                    break
                # We will be coming from this node's parent.
                res += 2
                current = parents[current]
        return res


# Build an adjacency list, then use DFS to travel from each node to its
# children checking the cost of collecting all the apples in each
# subtree, if a node sees that either itself, or one of its subtrees,
# has any apples that need to be collected, it adds 2 to the current
# count to account for the cost of traveling to this node and back to
# its parent.
#
# Time complexity: O(n) - We will visit each edge (n-1) while building
# the adjacency list, and each node during the depth-first search.
# Space complexity: O(n) - The call stack will grow to the height of
# the tree, which could be n.
#
# Runtime 593 ms Beats 100%
# Memory 49.2 MB Beats 99.36%
class DFS:
    def minTime(
        self, n: int, edges: List[List[int]], hasApple: List[bool]
    ) -> int:
        # Build an adjacency list of nodes.
        neighbors = [[] for _ in range(n)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(node: int, parent: int) -> int:
            cost = 0
            for child in neighbors[node]:
                if child == parent:
                    continue
                cost += dfs(child, node)
            # For any node other than the root, if we need to collect
            # any apples in its subtree, we will need to visit it
            # adding 2 to travel to its sub-root and back.
            if node and (cost or hasApple[node]):
                cost += 2
            return cost

        return dfs(0, -1)


def test():
    executors = [
        Solution,
        DFS,
    ]
    tests = [
        [4, [[0, 2], [0, 3], [1, 2]], [False, True, False, False], 4],
        [
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, True, False, True, True, False],
            8,
        ],
        [
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, True, False, False, True, False],
            6,
        ],
        [
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, False, False, False, False, False],
            0,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minTime(t[0], t[1], t[2])
                exp = t[3]
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
