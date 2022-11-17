# Dijkstra's Algorithm
# 🔴 Hard
#
# https://www.algoexpert.io/questions/dijkstra's-algorithm
#
# Tags: Famous Algorithms

import timeit
from heapq import heappop, heappush


# This is a template that can be used as the starting point of a
# solution with minimal changes.
#
# Time complexity: O((v + e)*log(v))
# Space complexity: O(v) - All vertexes could end up in the heap.
class Solution:
    def dijkstrasAlgorithm(self, start, edges):
        shortest_paths = [-1] * len(edges)
        heap = [(0, start)]
        while heap:
            distance, source = heappop(heap)
            if shortest_paths[source] != -1:
                continue
            shortest_paths[source] = distance
            for v, d in edges[source]:
                # If we haven't visited this edge yet, visit it.
                if shortest_paths[v] == -1:
                    heappush(heap, (distance + d, v))
        return shortest_paths


def test():
    executors = [Solution]
    tests = [
        [
            0,
            [
                [[1, 1], [7, 8]],
                [[2, 1]],
                [[3, 1]],
                [[4, 1]],
                [[5, 1]],
                [[6, 1]],
                [[7, 1]],
                [],
            ],
            [0, 1, 2, 3, 4, 5, 6, 7],
        ],
        [
            7,
            [
                [[1, 1], [3, 1]],
                [[2, 1]],
                [[6, 1]],
                [[1, 3], [2, 4], [4, 2], [5, 3], [6, 5]],
                [[5, 1]],
                [[4, 1]],
                [[5, 2]],
                [[0, 7]],
            ],
            [7, 8, 9, 8, 10, 11, 10, 0],
        ],
        [
            0,
            [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []],
            [0, 7, 13, 27, 10, -1],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.dijkstrasAlgorithm(t[0], t[1])
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
