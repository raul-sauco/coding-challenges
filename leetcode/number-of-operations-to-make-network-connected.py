# 1319. Number of Operations to Make Network Connected
# 🟠 Medium
#
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/
#
# Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

import timeit
from typing import List


# Use union-find to compute the number of disjoint sets and the number
# of redundant connections at the same time in O(e+n), the number of
# connections that we need to make is equal to the number of disjoint
# sets minus one, if the number of redundant connections is less than
# that, we cannot connect the network, return -1.
#
# Time complexity: O(v+e) - We iterate over all existing connections e
# to create the disjoint set structure, then iterate over all vertices v
# to compute the number of unconnected components.
# Space complexity: O(v) - We use two extra structures that are both of
# size v.
#
# Runtime 524 ms Beats 51.79%
# Memory 34.1 MB Beats 65.41%
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parents, rank = [x for x in range(n)], [1] * n
        # Count the number of existing redundant connections.
        redundant_connections = 0
        # Find with path compression.
        def findParent(a: int) -> int:
            if a != parents[a]:
                parents[a] = findParent(parents[a])
            return parents[a]

        # Union by rank.
        def connect(a: int, b: int):
            pa, pb = findParent(a), findParent(b)
            if rank[pb] > rank[pa]:
                return connect(b, a)
            parents[pb] = pa
            rank[pa] += rank[pb]

        # Construct the disjoint set to find the number of redundant
        # connections and the number of unconnected components. O(e)
        for a, b in connections:
            if findParent(a) == findParent(b):
                redundant_connections += 1
            else:
                connect(a, b)
        # Compute the number of disjoint sets. O(v).
        disjoint_sets = set()
        for i in range(n):
            disjoint_sets.add(findParent(i))
        return (
            -1
            if len(disjoint_sets) - 1 > redundant_connections
            else len(disjoint_sets) - 1
        )


def test():
    executors = [Solution]
    tests = [
        [4, [[0, 1], [0, 2], [1, 2]], 1],
        [5, [[0, 1], [0, 2], [3, 4], [2, 3]], 0],
        [6, [[0, 1], [0, 2], [0, 3], [1, 2]], -1],
        [6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.makeConnected(t[0], t[1])
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
