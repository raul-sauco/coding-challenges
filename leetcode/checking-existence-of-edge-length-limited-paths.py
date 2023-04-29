# 1697. Checking Existence of Edge Length Limited Paths
# 🔴 Hard
#
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
#
# Tags: Array - Union Find - Graph - Sorting

import json
import os
import timeit
from operator import itemgetter
from typing import List


# Sort both the edges and the queries using the edges weight and the
# queries limit. Use a DSU structure, iterate over the queries, for each
# query, iterate over any edges we have not visited previously and use
# them to update the DSU joining any groups that become available, once
# we do that, we know that if nodes a and b are in the same disjoint
# set, we can travel between a and b using edges with weight < limit.
#
# Time complexity: O(max(q, e)) - Where q is the number of queries and
# e is the number of edges, even though we have a nested for loop, we
# only visit each element of the inner loop once. The union call takes
# amortized O(1) time.
# Space complexity: O(n) - Both parents and rank arrays are size n.
#
# Runtime 2005 ms Beats 53.46%
# Memory 63.5 MB Beats 7.55%
class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        res = [None] * len(queries)
        edgeList.sort(key=itemgetter(2))
        queries = sorted(
            [q + [i] for i, q in enumerate(queries)], key=itemgetter(2)
        )
        parents = [i for i in range(n)]
        rank = [1] * n

        # Find with path compression.
        def findParent(a: int) -> int:
            if parents[a] != a:
                parents[a] = findParent(parents[a])
            return parents[a]

        # Union by rank.
        def union(a: int, b: int):
            pa, pb = findParent(a), findParent(b)
            if pa != pb:
                if rank[pb] > rank[pa]:
                    pa, pb = pb, pa
                parents[pb] = pa

        next_edge = 0
        for a, b, limit, idx in queries:
            # Process all edges with weight < limit.
            while next_edge < len(edgeList) and edgeList[next_edge][2] < limit:
                x, y, _ = edgeList[next_edge]
                union(x, y)
                next_edge += 1
            # True if the nodes ended in the same disjoint set.
            res[idx] = findParent(a) == findParent(b)

        return res


def test():
    executors = [Solution]
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    filename = os.path.splitext(os.path.basename(__file__))[0] + ".json"
    with open(os.path.join(__location__, filename)) as json_file:
        tests = json.load(json_file)
        for executor in executors:
            start = timeit.default_timer()
            for _ in range(1):
                for col, t in enumerate(tests):
                    sol = executor()
                    result = sol.distanceLimitedPathsExist(t[0], t[1], t[2])
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
