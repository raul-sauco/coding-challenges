# Kruskal's Algorithm
# 🔴 Hard
#
# https://www.algoexpert.io/questions/kruskals-algorithm
#
# Tags: Famous Algorithms - Graph - Union Find

import timeit


# Create an implementation of Kruskal's algorithm that returns the
# minimum spanning tree/forest of a graph given its edges.
# https://en.wikipedia.org/wiki/Kruskal's_algorithm
#
# Time complexity: O(e*log(e)) == O(e*log(v))
# Space complexity: O(e) - All edges are copied to the sorted edges
# array.
class Solution:
    def kruskalsAlgorithm(self, edges):
        n = len(edges)
        # Union-Find section.
        parents = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        # Find parent with path compression O(α1)
        def findParent(a: int) -> int:
            if parents[a] != a:
                parents[a] = findParent(parents[a])
            return parents[a]

        def union(a: int, b: int):
            pa, pb = findParent(a), findParent(b)
            if rank[pa] < rank[pb]:
                pa, pb = pb, pa
            parents[pb] = pa
            rank[pa] += rank[pb]

        # Sort the edges by weight.
        sorted_edges = sorted(
            [(w, s, d) for s, edge in enumerate(edges) for d, w in edge]
        )
        res = [[] for _ in range(n)]
        for w, s, d in sorted_edges:
            # If the vertexes are not already connected.
            if findParent(s) != findParent(d):
                union(s, d)
                res[s].append([d, w])
                res[d].append([s, w])
        return res


def test():
    executors = [Solution]
    tests = [
        [
            [
                [[1, 3], [2, 5]],
                [[0, 3], [2, 10], [3, 12]],
                [[0, 5], [1, 10]],
                [[1, 12]],
            ],
            [[[1, 3], [2, 5]], [[0, 3], [3, 12]], [[0, 5]], [[1, 12]]],
        ],
        [
            [
                [[1, 3], [2, 5]],
                [[0, 3], [2, 10], [3, 12], [4, 1]],
                [[0, 5], [1, 10], [4, 7]],
                [[1, 12]],
                [[1, 1], [2, 7]],
            ],
            [
                [[1, 3], [2, 5]],
                [[4, 1], [0, 3], [3, 12]],
                [[0, 5]],
                [[1, 12]],
                [[1, 1]],
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.kruskalsAlgorithm(t[0])
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
