# 261. Graph Valid Tree
# 🟠 Medium
#
# https://leetcode.com/problems/graph-valid-tree/
#
# Tags: Array - Matrix - Depth-First Search - Breadth-First Search -
# Union Find

import timeit
from typing import List


# Use union find to check if the graph is connected and also check if
# the number of edges equals the number of vertex minus one to determine
# if there are any cycles.
#
# Time complexity: O(n) - Where n is the number of edges/nodes. If this
# number is not equal + 1, then the first conditional fails and it
# returns in O(1), if the values are similar, we iterate over the edges
# then over the nodes.
# Space complexity: O(n) - Both the rank and parents array grow to the
# size of the input.
#
# Runtime: 102 ms, faster than 69.0%
# Memory Usage: 6.53 MB, less than 98.53%
class UnionFind:
    def validTree(self, n: int, edges: List[int]) -> bool:
        if len(edges) != n - 1:
            return False
        # Check if the graph is connected, we could use union find.
        parents = [i for i in range(n)]
        # Keep track of the number of nodes under this parent.
        rank = [1] * n
        # Find function.
        def findParent(a: int) -> int:
            if parents[a] == a:
                return a
            # Use path compression, following calls will be O(1)
            parents[a] = findParent(parents[a])
            return parents[a]

        # Union by rank function.
        def union(a: int, b: int) -> None:
            # Find the parents.
            pa, pb = findParent(a), findParent(b)
            if rank[pb] > rank[pa]:
                pa, pb = pb, pa
            parents[pb] = pa
            rank[pa] += rank[pb]

        # Call union find with each edge.
        for a, b in edges:
            union(a, b)
        # Make sure we call findParent for all the elements.
        return len({findParent(i) for i in range(n)}) == 1


# Use an adjecency list to explore the graph using DFS, it could also be
# BFS, save nodes we see in a set, if we ever visit a node that we have
# previously seen, we have found a cycle and we can return false. When
# we get to the end we check if the set is the same size as the total
# count of nodes, if it isn't, the graph is not connected and we can
# return false.
#
# Time complexity: O(n) - At most we visit n nodes, if we ever visit the
# same node a second time we immediately return false.
# Space complexity; O(n) - The adjecency list dictionary and the set
# will grow at max to size n.
#
# Runtime: 101 ms, faster than 88.0%
# Memory Usage: 7.44 MB, less than 92.25%
class AdjecencyList:
    def validTree(self, n: int, edges: List[int]) -> bool:
        if not n:
            return True
        if len(edges) != n - 1:
            return False
        # Adjecency lists.
        adj = {i: [] for i in range(n)}
        # Add neighbors.
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        # Store nodes seen.
        seen = set()

        def dfs(current: int, prev: int) -> bool:
            if current in seen:
                return False
            seen.add(current)
            for neighbor in adj[current]:
                # Skip the current node's parent.
                if neighbor == prev:
                    continue
                if not dfs(neighbor, current):
                    return False
            return True

        # DFS would return false if a cycle is detected.
        # If the graph is connected, we will have visited all nodes.
        return dfs(0, -1) and len(seen) == n


def test():
    executors = [
        UnionFind,
        AdjecencyList,
    ]
    tests = [
        [5, [[0, 1], [0, 2], [0, 3], [1, 4]], True],
        [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.validTree(t[0], t[1])
                exp = t[2]
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
