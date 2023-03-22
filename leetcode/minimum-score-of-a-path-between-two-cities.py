# 2492. Minimum Score of a Path Between Two Cities
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
#
# Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

import timeit
from typing import List


# Use a modified version of union find that, each time that connects
# components, it also keeps the value of the min value edge that has
# been seen between the two components that are being connected and the
# new edge that is being added, then return the minimum edge of the
# set that contains node 1, since we are guaranteed that 1 and n are
# connected, this set also contains n.
#
# Time Complexity: O(e) - Where e is the number of edges, we iterate
# over the edges and, for each, we do a union operation that runs in
# amortized O(1) time.
# Space complexity: O(n) - Where n is the number of nodes, we have three
# structures of size n.
#
# Runtime 1679 ms Beats 85.57%
# Memory 58.7 MB Beats 96.31%
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Parents array, each node starts as an unconnected node.
        parents = [x for x in range(n + 1)]
        rank = [1] * (n + 1)
        scores = [float("inf")] * (n + 1)

        def findParent(a: int) -> int:
            if a != parents[a]:
                parents[a] = findParent(parents[a])
            return parents[a]

        def union(a: int, b: int, dist: int) -> None:
            pa, pb = findParent(a), findParent(b)
            if rank[pb] > rank[pa]:
                return union(b, a, dist)
            parents[pb] = pa
            rank[pa] += rank[pb]
            # The minimum score between both connected graphs and the
            # new edge we are adding.
            scores[pa] = min(scores[pa], dist, scores[pb])

        for a, b, dist in roads:
            union(a, b, dist)
        return scores[findParent(1)]


def test():
    executors = [Solution]
    tests = [
        [4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2],
        [4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5],
        [
            6,
            [
                [4, 5, 7468],
                [6, 2, 7173],
                [6, 3, 8365],
                [2, 3, 7674],
                [5, 6, 7852],
                [1, 2, 8547],
                [2, 4, 1885],
                [2, 5, 5192],
                [1, 3, 4065],
                [1, 4, 7357],
            ],
            1885,
        ],
        [
            20,
            [
                [18, 20, 9207],
                [14, 12, 1024],
                [11, 9, 3056],
                [8, 19, 416],
                [3, 18, 5898],
                [17, 3, 6779],
                [13, 15, 3539],
                [15, 11, 1451],
                [19, 2, 3805],
                [9, 8, 2238],
                [1, 16, 618],
                [16, 14, 55],
                [17, 7, 6903],
                [12, 13, 1559],
                [2, 17, 3693],
            ],
            55,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minScore(t[0], t[1])
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
