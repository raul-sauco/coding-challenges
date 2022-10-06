# 323. Number of Connected Components in an Undirected Graph
# 🟠 Medium
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
#
# Tags: Graph - Depth-First Search - Union Find

import timeit
from collections import Counter
from typing import List


# Use Union Find to group nodes, then return the number of groups found.
#
# Time complexity: O(an) - Amortized n, path compression and union by
# rank optimize the time complexity.
# Space complexity: O(n) - The rank and parents arrays.
class CountParents:
    def countComponents(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]
        rank = [1] * n
        # Find the parent of the given node.
        def find(a: int) -> None:
            if parents[a] == a:
                return a
            # Path compression.
            parents[a] = find(parents[a])
            return parents[a]

        # Union by rank.
        def union(a: int, b: int) -> None:
            # Find the parents.
            pa, pb = find(a), find(b)
            # If pb has a higher rank, make it the parent.
            if rank[pb] > rank[pa]:
                pa, pb = pb, pa
            parents[pb] = pa
            rank[pa] += rank[pb]

        for a, b in edges:
            union(a, b)
        # return len(set(parents)) # High hashing cost.
        return len(Counter(parents).keys())


# Use Union Find to group nodes, then return the number of groups found.
# Similar to the previous solution but optimized to count successful
# union operations to avoid the O(n) counting step at the end.
#
# Time complexity: O(an) - Amortized n, path compression and union by
# rank optimize the time complexity.
# Space complexity: O(n) - The rank and parents arrays.
class CountUnions:
    def countComponents(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]
        rank = [1] * n
        groups = n
        # Find the parent of the given node.
        def find(a: int) -> None:
            if parents[a] == a:
                return a
            # Path compression.
            parents[a] = find(parents[a])
            return parents[a]

        # Union by rank.
        def union(a: int, b: int) -> bool:
            # Find the parents.
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            # If pb has a higher rank, make it the parent.
            if rank[pb] > rank[pa]:
                pa, pb = pb, pa
            parents[pb] = pa
            rank[pa] += rank[pb]
            return True

        # Create the disjoint sets.
        for a, b in edges:
            if union(a, b):
                groups -= 1
        return groups


def test():
    executors = [
        CountParents,
        CountUnions,
    ]
    tests = [
        [3, [], 3],
        [7, [[2, 5], [0, 6]], 5],
        [5, [[0, 1], [1, 2], [3, 4]], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countComponents(t[0], t[1])
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
