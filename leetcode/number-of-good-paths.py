# 2421. Number of Good Paths
# 🔴 Hard
#
# https://leetcode.com/problems/number-of-good-paths/
#
# Tags: Array - Tree - Union Find - Graph

import sys
import timeit
from collections import Counter, defaultdict
from typing import List


# The brute force solution searches all paths, starting at every node
# and visiting all other nodes until the path is not good while counting
# good paths and adding them to the total result.
#
# Time complexity: O(n^2) - Starting at each node, we do a depth-first
# search that could potentially visit all other nodes.
# Space complexity: O(n) - The neigbors array has one entry per edge in
# the graph, and there are n-1 edges.
#
# This solution fails with time limit exceeded.
class BruteForce:
    def numberOfGoodPaths(
        self, vals: List[int], edges: List[List[int]]
    ) -> int:
        # The number of nodes in the tree.
        n = len(vals)
        # Create an adjacency list to represent the trees.
        nei = [[] for _ in range(n)]
        for a, b in edges:
            nei[a].append(b)
            nei[b].append(a)
        # Find the number of good paths by visiting all neighbors
        # starting at each node O(n^2).
        def dfs(node: int, lim: int, prev: int) -> int:
            # Base case, this path has become invalid.
            if vals[node] > lim:
                return 0
            return (
                # Explore all neighbors except the one we came from.
                sum([dfs(i, lim, node) for i in nei[node] if i != prev])
                # If the current node's value is the same as the limit,
                # and this node is not the first node in the DFS, this
                # is a valid path.
                + (1 if vals[node] == lim and prev is not None else 0)
            )

        # Compute the number of paths, it will double count paths.
        paths = [dfs(i, vals[i], None) for i in range(n)]
        # The result is half the number of (double counted) paths plus
        # the number of nodes because each node is a valid path by
        # itself.
        return sum(paths) // 2 + n


# A better solution uses the union find algorithm, we process the nodes
# in increasing order of value by using their neighbors information to
# add any nodes with equal or inferior values into a series of disjoint
# sets. Once we have created the disjoint groups that contain all nodes
# with a given value, we count the number of nodes in each group, since
# we know that the groups only contain nodes with equal or less value,
# we know that there is a path between any two nodes in that group.
#
# Time complexity: O(n*log(n)) - The highest complexity comes from
# sorting the keys of the value to node dictionary, since all nodes
# could have unique values, that operation costs O(n*log(n)).
# Space complexity: O(n) - The parents, rank and value to node all have
# a linear relation with the number of nodes in the input.
#
# Runtime 1999 ms Beats 95.32%
# Memory 32 MB Beats 94.47%
class UnionFind:
    def numberOfGoodPaths(
        self, vals: List[int], edges: List[List[int]]
    ) -> int:
        # The number of nodes in the tree.
        paths = n = len(vals)
        # A parents array.
        parents, rank = [i for i in range(n)], [1] * n
        # Find the representative of a given node.
        def findParent(a: int) -> int:
            if parents[a] != a:
                parents[a] = findParent(parents[a])
            return parents[a]

        # Union by rank.
        def union(a: int, b: int) -> None:
            pa, pb = findParent(a), findParent(b)
            if rank[pa] > rank[pb]:
                parents[pb] = pa
                rank[pa] += rank[pb]
            else:
                parents[pa] = pb
                rank[pb] += rank[pa]

        # Create an adjacency list to represent the tree.
        neighbors = [[] for _ in range(n)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        # A dictionary of values pointing to all the nodes that have
        # that value.
        valueToNode = defaultdict(list)
        for i in range(n):
            valueToNode[vals[i]].append(i)
        # Iterate over all nodes on each value from smalles to largest.
        for val in sorted(valueToNode.keys()):
            # Iterate over all nodes that have this value.
            for node in valueToNode[val]:
                # Iterate over all this node's neighbors adding the ones
                # with the same or smaller values to the disjoint set.
                for nei in neighbors[node]:
                    if vals[nei] <= val:
                        union(node, nei)
            # Iterate again over all the nodes counting the number of
            # nodes with the current value val in each group. Use a
            # dictionary keyed by representative.
            counts = defaultdict(int)
            for node in valueToNode[val]:
                # Find the node's representative and add one to the
                # count of nodes with this value to this disjoint set.
                counts[findParent(node)] += 1
            # Iterate over all the disjoint sets that have any nodes
            # with this value in them counting the number of good paths.
            for parent in counts.keys():
                # The number of good paths on this disjoint set.
                paths += counts[parent] * (counts[parent] - 1) // 2
        return paths


# A pretty interesting solution by Lee215.
# https://leetcode.com/problems/number-of-good-paths/solutions/2620680
# It uses the same union find idea, but instead of loops and a one
# dimensional rank array, it keeps a multidimensional count array that
# keeps the number of nodes with each value in each disjoint set and
# uses that to compute the result.
#
# Time complexity: O(n*log(n)).
# Space complexity: O(n).
#
# Runtime 3022 ms Beats 57.65%
# Memory 43.4 MB Beats 49.36%
class UnionFind2:
    def numberOfGoodPaths(
        self, vals: List[int], edges: List[List[int]]
    ) -> int:
        # The number of nodes in the tree.
        res = n = len(vals)
        parents = [i for i in range(n)]
        # A count of nodes with the given value in the given group.
        count = [Counter({vals[i]: 1}) for i in range(n)]
        # Mutate the edges array to contain the highest value between
        # both nodes as the first value, and sort using that value.
        edges = sorted([max(vals[i], vals[j]), i, j] for i, j in edges)

        # Find with path compression.
        def findParent(a: int) -> int:
            if parents[a] != a:
                parents[a] = findParent(parents[a])
            return parents[a]

        # Iterate over the graph edges starting by the ones where the
        # highest node value is the smallest.
        for val, a, b in edges:
            pa, pb = findParent(a), findParent(b)
            ca, cb = count[pa][val], count[pb][val]
            res += cb * ca
            parents[pb] = pa
            count[pa] = Counter({val: cb + ca})
        return res


def test():
    executors = [
        BruteForce,
        UnionFind,
        UnionFind2,
    ]
    tests = [
        [[1], [], 1],
        [[1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]], 6],
        [[1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]], 7],
    ]
    sys.setrecursionlimit(15000)
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numberOfGoodPaths(t[0], t[1])
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
