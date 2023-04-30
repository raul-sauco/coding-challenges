# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
# 🔴 Hard
#
# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
#
# Tags: Union Find - Graph

import timeit
from typing import List


# We can use two DSU structures, one for Alice and one for Bob, we only
# add the edges that connect previously unconnected components and then
# check how many of them we used and how many we did not use.
#
# Time complexity: O(max(n, e)) - We iterate over the edges twice, we
# iterate over n elements to create the auxiliary structures.
# Space complexity: O(n) - The parents and ranks arrays have size n.
#
# Runtime 2184 ms Beats 63.13%
# Memory 57 MB Beats 18.13%
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # The number of disjoint sets in both DSU.
        cb = n
        parents_bob = [x for x in range(n)]
        # parents_alice = [i for i in range(n + 1)]
        rank_bob = [1] * n
        # rank_alice = [1] * (n + 1)

        # Find the parent of the given node.
        def find(a: int, is_bob: bool) -> int:
            parents = parents_bob if is_bob else parents_alice
            if parents[a] != a:
                # Path compression.
                parents[a] = find(parents[a], is_bob)
            return parents[a]

        # Union by rank. Returns false if the nodes are already
        # connected.
        def union(a: int, b: int, is_bob: bool) -> bool:
            parents = parents_bob if is_bob else parents_alice
            rank = rank_bob if is_bob else rank_alice
            # Find the parents.
            pa, pb = find(a, is_bob), find(b, is_bob)
            if pa == pb:
                return False
            # If pb has a higher rank, make it the parent.
            if rank[pb] > rank[pa]:
                pa, pb = pb, pa
            parents[pb] = pa
            rank[pa] += rank[pb]
            return True

        # Store the number of edges we use.
        res = 0
        # Create the disjoint sets. First only type 3 edges.
        for t, a, b in edges:
            if t == 3:
                if union(a - 1, b - 1, True):
                    cb -= 1
                else:
                    res += 1
        parents_alice = parents_bob[::]
        rank_alice = rank_bob[::]
        ca = cb
        for t, a, b in edges:
            a, b = a - 1, b - 1
            if t == 2:
                if union(a, b, True):
                    cb -= 1
                else:
                    res += 1
            if t == 1:
                if union(a, b, False):
                    ca -= 1
                else:
                    res += 1
        if max(ca, cb) > 1:
            return -1
        return res


def test():
    executors = [Solution]
    tests = [
        [4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]], -1],
        [4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]], 0],
        [
            4,
            [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]],
            2,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxNumEdgesToRemove(t[0], t[1])
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
